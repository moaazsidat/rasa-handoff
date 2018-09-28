import time
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello, bots"


meetup_store = {"toronto": {"tech": [251176370]}}


@app.route("/meetup/<location>/<m_type>", methods=["GET", "POST"])
def meetup(location, m_type):
    if request.method == "POST":
        """
        POST
        add meetup id to meetup store
        """
        if location in meetup_store:
            if m_type in meetup_store[location]:
                meetup_store[location][m_type].append(request.data.meetup_id)
            else:
                meetup_store[location][m_type] = []
                meetup_store[location][m_type].append(request.data.meetup_id)
        else:
            meetup_store[location] = {}
            meetup_store[location][m_type] = []
            meetup_store[location][m_type].append(request.data.meetup_id)
    else:
        """
        GET
        retry 10 times with 10 sec sleeps to fetch info
        """
        # emulate slow response
        time.sleep(5)
        if location in meetup_store and m_type in meetup_store[location]:
            return jsonify({"meetup_id": meetup_store[location][m_type]})
        else:
            return jsonify({"error": "no meetups found"})


"""
stores senders and state of chat
{
    [sender_id]: {
        paused: True | False,
        replies: [],
    }
}
"""
sender_store = {"123": {"paused": True, "replies": []}}


@app.route("/handoff/<sender_id>", methods=["GET", "POST"])
def handoff(sender_id):
    if request.method == "POST":
        """
        POST
        add sender id to sender store
        """
        if sender_id in sender_store:
            sender_store[sender_id]["replies"].append(request.get_json()["message"])
            return jsonify(sender_store[sender_id])
        else:
            return jsonify({"error": "sender_id not found"})
    else:
        """
        GET
        retry 10 times with 10 sec sleeps to fetch info
        """
        if sender_id not in sender_store:
            sender_store[sender_id] = {"paused": True, "replies": []}

        ## poll on replies to fetch the message
        while len(sender_store[sender_id]["replies"]) == 0:
            time.sleep(1)

        message = sender_store[sender_id]["replies"].pop(0)
        return jsonify({"message": message})


if __name__ == "__main__":
    app.run(host=app.config.get("HOST"), port=app.config.get("PORT"))

