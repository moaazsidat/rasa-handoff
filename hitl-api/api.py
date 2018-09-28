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


if __name__ == "__main__":
    app.run(host=app.config.get("HOST"), port=app.config.get("PORT"))
