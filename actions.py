from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionGetRoomPrice(Action):
   def name(self):
      # type: () -> Text
      return "action_get_room_price"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

      current_room = tracker.get_slot('current_room')
      room = tracker.get_slot('room')

      if room == 'others':
        if current_room.lower() == 'alpha':
          # utter b,c
          dispatcher.utter_template('utter_room_beta_price', tracker)
          dispatcher.utter_template('utter_room_gamma_price', tracker)
        elif current_room.lower() == 'beta':
          # utter a, c
          dispatcher.utter_template('utter_room_alpha_price', tracker)
          dispatcher.utter_template('utter_room_gamma_price', tracker)
        elif current_roomw.lower() == 'gamma':
          # utter a, b
          dispatcher.utter_template('utter_room_alpha_price', tracker)
          dispatcher.utter_template('utter_room_beta_price', tracker)
      elif room == None:
        dispatcher.utter_template('utter_room_alpha_price', tracker)
        dispatcher.utter_template('utter_room_beta_price', tracker)
        dispatcher.utter_template('utter_room_gamma_price', tracker)
      else:
        if room.lower() == 'alpha':
          dispatcher.utter_template('utter_room_alpha_price', tracker)
          return [SlotSet('current_room', 'Alpha')]
        elif room.lower() == 'beta':
          dispatcher.utter_template('utter_room_beta_price', tracker)
          return [SlotSet('current_room', 'Beta')]          
        elif room.lower() == 'gamma':
          dispatcher.utter_template('utter_room_gamma_price', tracker)
          return [SlotSet('current_room', 'Gamma')]

      return []

class ActionGetRoomSize(Action):
   def name(self):
      # type: () -> Text
      return "action_get_room_size"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

      current_room = tracker.get_slot('current_room')
      room = tracker.get_slot('room')

      if room == 'others':
        if current_room.lower() == 'alpha':
          # utter b,c
          dispatcher.utter_template('utter_room_beta_size', tracker)
          dispatcher.utter_template('utter_room_gamma_size', tracker)
        elif current_room.lower() == 'beta':
          # utter a, c
          dispatcher.utter_template('utter_room_alpha_size', tracker)
          dispatcher.utter_template('utter_room_gamma_size', tracker)
        elif current_roomw.lower() == 'gamma':
          # utter a, b
          dispatcher.utter_template('utter_room_alpha_size', tracker)
          dispatcher.utter_template('utter_room_beta_size', tracker)
      elif room == None:
        dispatcher.utter_template('utter_room_alpha_size', tracker)
        dispatcher.utter_template('utter_room_beta_size', tracker)
        dispatcher.utter_template('utter_room_gamma_size', tracker)
      else:
        if room.lower() == 'alpha':
          dispatcher.utter_template('utter_room_alpha_size', tracker)
          return [SlotSet('current_room', 'Alpha')]
        elif room.lower() == 'beta':
          dispatcher.utter_template('utter_room_beta_size', tracker)
          return [SlotSet('current_room', 'Beta')]          
        elif room.lower() == 'gamma':
          dispatcher.utter_template('utter_room_gamma_size', tracker)
          return [SlotSet('current_room', 'Gamma')]

      return []