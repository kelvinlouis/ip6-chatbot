from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionCorrectRoom(Action):
   def name(self):
      # type: () -> Text
      return "action_correct_room"

   def run(self, dispatcher, tracker, domain):
      current_room = tracker.get_slot('current_room')
      room = tracker.get_slot('room')

      if room == 'Alpha' or room == 'first':
        return [SlotSet('current_room', 'Alpha')]
      elif room == 'Beta' or room == 'second':
        return [SlotSet('current_room', 'Beta')]
      elif room == 'Gamma' or room == 'third' or room == 'last':
        return [SlotSet('current_room', 'Gamma')]
      
      return []