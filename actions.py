from rasa_core.actions import Action


class ActionExample(Action):

    def name(self):
        # you can then use action_example in your stories
        return "action_example"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        return []
