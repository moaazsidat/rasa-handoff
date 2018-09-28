## greet
* greet
    - utter_greet
	

## goodbye
* goodbye
    - utter_goodbye
	

## meetup
* meetup
    - action_meetup


## ask_human
* ask_human
    - action_talk_to_human


## thanks+goodbye
* thanks+goodbye
    - utter_goodbye


## find_meetup_01
* greet
    - utter_greet
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* affirm
    - action_join_meetup
* affirm
	- action_join_event
* ask_transport{"origin":"Rasa Technologies GmbH"}
	- action_suggest_route
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset

## talk_to_human_01
* greet
    - utter_greet
* ask_human
	- action_talk_to_human
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset

## talk_to_human_02
* greet
    - utter_greet
* ask_human
	- action_talk_to_human

## find_meetup_02
* greet
    - utter_greet
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* affirm
    - action_join_meetup
* affirm
	- action_join_event
* ask_transport{"origin":"Alexanderplatz"}
	- action_suggest_route
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset


## find_meetup_03
* greet
	- utter_greet
* meetup{"location":"London", "type":"tech"}
	- action_meetup
* affirm
    - action_join_meetup
* affirm
	- action_join_event
* ask_transport{"origin":"Marylebone"}
	- action_suggest_route
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset


## find_meetup_04
* greet
	- utter_greet
* meetup{"location":"London", "type":"tech"}
	- action_meetup
* affirm
    - action_join_meetup
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset

	
## find_meetup_06
* greet
    - utter_greet
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* affirm
    - action_join_meetup
* affirm+ask_transport{"origin":"Alexanderplatz"}
	- action_join_event
	- action_suggest_route
* thanks+goodbye
	- utter_thanks
	- utter_goodbye
	- action_slot_reset


## find_meetup_07
* greet
    - utter_greet
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* affirm
    - action_join_meetup
* affirm+ask_transport{"origin":"Rasa Technologies GmbH"}
	- action_join_event
	- action_suggest_route
* thanks+goodbye
	- utter_goodbye
	- action_slot_reset


## talk_to_human_03
* greet
    - utter_greet
* ask_human
	- action_talk_to_human
* thanks+goodbye
	- utter_thanks
	- utter_goodbye
	- action_slot_reset
	
 
## story_09
* greet
	- utter_greet
* meetup{"location":"London", "type":"fitness"}
	- action_meetup
* affirm
	- action_join_meetup
* affirm+ask_transport{"origin":"Baker Street"}
	- action_join_event
	- action_suggest_route 
* thanks+goodbye
	- utter_thanks
	- utter_goodbye
	- action_slot_reset
 
 
## story_10
* greet
	- utter_greet
* meetup{"location":"London", "type":"fitness"}
	- action_meetup
* affirm
	- action_join_meetup
* affirm+ask_transport{"origin":"Baker Street"}
	- action_join_event
	- action_suggest_route 
* thanks+goodbye
	- utter_goodbye
	- action_slot_reset
	

## find_meetup_11
* greet
    - utter_greet
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* deny
	- utter_goodbye
	- action_slot_reset
		
## find_meetup_12
* greet
    - utter_greet
* meetup{"location":"Berlin", "type":"sports"}
    - action_meetup
* affirm
	- action_join_meetup
* goodbye
	- utter_goodbye
	- action_slot_reset

## talk_to_human_04
* greet
    - utter_greet
* ask_human
	- action_talk_to_human
* goodbye
	- utter_goodbye
	- action_slot_reset
	

## find_meetup_13
* greet
	- utter_greet
* meetup{"location":"London", "type":"tech"}
	- action_meetup
* affirm
    - action_join_meetup
* affirm
	- action_join_event
* thanks
	- utter_thanks
	- utter_goodbye
	- action_slot_reset