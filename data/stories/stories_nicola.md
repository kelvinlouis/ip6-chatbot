## Generated Story -8897532857795406961
* greet
    - utter_greet+ask_for_name
* provide_name{"name": "Nicola"}
    - slot{"name": "Nicola"}
    - utter_ask_for_service_with_name
* reserve_room{"company": "Novartis"}
    - slot{"company": "Novartis"}
    - utter_confirm+options
    - utter_ask_for_service
* ask_for_room_equipment
    - utter_ask_for_nr_of_people_with_name
* provide_nr_of_people{"nr_of_people": "195"}
    - slot{"nr_of_people": "195"}
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_price{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"room": null}
    - slot{"current_room": "Alpha"}
    - utter_room_alpha_price
* ask_for_room_price{"room": "other"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_atmosphere{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_atmosphere
* ask_for_room_seating
    - utter_room_gamma_seating
* reserve_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"room": null}
    - slot{"current_room": "Gamma"}
    - utter_confirm_booking+ask_for_service
* deny
    - utter_thanks_with_name
    - utter_goodbye
* farewell

