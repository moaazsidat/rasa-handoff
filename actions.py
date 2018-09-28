from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import (
    SlotSet,
    AllSlotsReset,
    ConversationPaused,
    ConversationResumed,
)
import requests
import json
from random import randint
import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

# load env variables
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


# class ActionMeetup(Action):
# 	def name(self):
# 		return 'action_meetup'

# 	def run(self, dispatcher, tracker, domain):
# 		# get slot data
# 		location = tracker.get_slot('location')
# 		type = tracker.get_slot('type')

# 		r = requests.get('https://api.meetup.com/find/groups?key={}&location={}&text={}&upcoming_events=true'.format(os.environ['MEETUP_KEY'], location, type))
# 		response = json.loads(r.text)

#     # get a random meetup from the list returned by the api
# 		meetup = response[randint(0,len(response)-1)]

# 		meetup_name = meetup['name']
# 		url_name = meetup['urlname']
# 		next_event = meetup['next_event']
# 		next_event_id = meetup['next_event']['id']
# 		next_event_name = meetup['next_event']['name']
# 		next_event_time = meetup['next_event']['time']/1000
# 		next_event_time1 = datetime.datetime.fromtimestamp(int(next_event_time)).strftime('%Y-%m-%d %H:%M:%S')

# 		response = "There is a {} meetup in {}. They are having an event called {} on {}. Would you like to join the meetup?".format(meetup_name, location, next_event_name, next_event_time1)

# 		dispatcher.utter_message(response)

#     # set slot data
# 		return [SlotSet('meetup_id',url_name), SlotSet('next_event_id', next_event_id)]


class ActionMeetup(Action):
    """
	human in the loop version of ActionMeetup
	"""

    def name(self):
        return "action_meetup"

    def run(self, dispatcher, tracker, domain):
        # get slot data
        location = tracker.get_slot("location")
        type = tracker.get_slot("type")

        response = "passing info to human – location: {}, type: {}".format(
            location, type
        )
        dispatcher.utter_message(response)

        """
		seems like rasa will stop listening once conversation
		is paused, which means no actions are attempted, therefore
		preventing triggering ConversationResumed() in a straightforward way.
		"""
        tracker.update(ConversationPaused())
        url = "http://127.0.0.1:5000/meetup/{}/{}".format(location, type)
        req = requests.get(url)
        resp = json.loads(req.text)
        if "error" not in resp:
            resp_message = "meetups found with ids: {}".format(resp["meetup_id"])
            dispatcher.utter_message(resp_message)
        tracker.update(ConversationResumed())

        """
		I'm looking for tech meetups in Toronto
		"""
        # return [ConversationPaused()]


class ActionJoinMeetup(Action):
    def name(self):
        return "action_join_meetup"

    def run(self, dispatcher, tracker, domain):
        print(self.name(), tracker)
        meetup_id = tracker.get_slot("meetup_id")

        r = requests.post(
            "https://api.meetup.com/2/profile?key={}&group_urlname={}".format(
                os.environ["MEETUP_KEY"], meetup_id
            )
        )
        response = json.loads(r.text)

        if "code" in response.keys():
            dispatcher.utter_message(
                "Sorry, this meetup requires to fill a questionnaire before you can join. Unfortunately, I haven't been taught the skill of filling the questionnaires yet :("
            )
        elif response["group"]["join_mode"] != "open":
            dispatcher.utter_message(
                "Unfortunately only approved members can join this meetup"
            )
        else:
            dispatcher.utter_message(
                "Done! You have joined the meetup. Would you like to attend their nearest event?"
            )


class ActionJoinEvent(Action):
    def name(self):
        return "action_join_event"

    def run(self, dispatcher, tracker, domain):
        print(self.name(), tracker)
        next_event_id = tracker.get_slot("next_event_id")

        r = requests.post(
            "https://api.meetup.com/2/rsvp?key={}&event_id={}&rsvp=yes".format(
                os.environ["MEETUP_KEY"], next_event_id
            )
        )
        response = json.loads(r.text)

        try:
            lon = response["venue"]["lon"]
            lat = response["venue"]["lat"]
            event_name = response["event"]["name"]
            event_time = datetime.datetime.fromtimestamp(
                int(response["event"]["time"]) / 1000
            ).strftime("%Y-%m-%d %H:%M:%S")

            dispatcher.utter_message(
                "All done. I have booked you a spot at the event {} which is happening at {}".format(
                    event_name, event_time
                )
            )
            return [SlotSet("lon", lon), SlotSet("lat", lat)]

        except (KeyError, UnboundLocalError) as e:
            dispatcher.utter_message(
                "Sorry, there are no free seats left in this event."
            )
            return [SlotSet("lon", ""), SlotSet("lat", "")]


class ActionSuggestRoute(Action):
    def name(self):
        return "action_suggest_route"

    def run(self, dispatcher, tracker, domain):
        print(self.name(), tracker)
        origin = tracker.get_slot("origin")
        lon = tracker.get_slot("lon")
        lat = tracker.get_slot("lat")

        try:
            r = requests.get(
                "https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={},{}&key={}&mode=transit".format(
                    origin, lat, lon, os.environ["GOOGLE_KEY"]
                )
            )
            response = json.loads(r.text)

            text_response = ""
            routes = response["routes"][0]["legs"][0]["steps"]
            for i in routes:
                text_response += i["html_instructions"] + ". "

            dispatcher.utter_message(
                "No problem.  Here are the directions for getting to the venue using a public transport: {}".format(
                    text_response
                )
            )

        except (EOFError, IndexError) as e:
            dispatcher.utter_message(
                "Unfortunately, the event don't have a venue announced yet so I can't give you the directions."
            )


class ActionSlotReset(Action):
    def name(self):
        return "action_slot_reset"

    def run(self, dispatcher, tracker, domain):
        print(self.name(), tracker)
        return [AllSlotsReset()]

