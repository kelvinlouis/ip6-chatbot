## Generated Story -2306698450094699806
* greet{"name": "Silvia Parankeymalil"}
    - slot{"name": "Silvia Parankeymalil"}
    - utter_greet_with_name+ask_for_service
* ask_for_options
    - utter_options+ask_for_nr_of_people
* provide_nr_of_people{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - utter_confirm+options
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_equipment
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* ask_for_room_price{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price
* ask_for_room_atmosphere
    - utter_room_alpha_atmosphere
* ask_for_room_seating
    - utter_room_alpha_seating
* ask_for_room{"room": "third"}
    - slot{"room": "third"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating
* ask_for_room_price{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_price
* ask_for_room_equipment{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_equipment
* provide_budget{"budget": "1500", "room": "it"}
    - slot{"budget": "1500"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_confirm+budget_limitation
* reserve_room{"room": "the"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_confirm+ask_for_booking_date
* provide_booking_date{"date": "21st of August 2019"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking+ask_for_service
* farewell
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story -1847740183244512759
* greet{"name": "Kelvin"}
    - slot{"name": "Kelvin"}
    - utter_greet_with_name+ask_for_service
* ask_for_options
    - utter_options+ask_for_nr_of_people
* provide_budget{"nr_of_people": "150", "room": "this"}
    - slot{"nr_of_people": "150"}
    - slot{"room": "this"}
    - utter_confirm+options
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_seating{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_seating
* ask_for_room_seating
    - utter_room_alpha_seating
* ask_for_room{"room": "other"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_seating
    - utter_room_gamma_seating
* ask_for_room_price{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price
* provide_booking_date{"room": "it", "date": "21st of August"}
    - slot{"date": "21st of August"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
* thanks
    - utter_appreciation+ask_for_service
* farewell
    - utter_goodbye
* farewell
    - utter_thanks

