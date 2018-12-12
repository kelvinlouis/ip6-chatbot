## Generated Story -2306698450094699806
* greet+provide_name{"name": "Silvia Manikuthil"}
    - slot{"name": "Silvia Manikuthil"}
    - utter_greet_with_name
    - utter_ask_for_service
* ask_for_options
    - utter_options
    - utter_ask_for_nr_of_people
* provide_nr_of_people{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - utter_confirm
    - utter_options
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
    - utter_confirm
    - utter_budget_limitation_1400
* reserve_room{"room": "the"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_confirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "21st of August 2019"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* farewell
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story -1847740183244512759
* greet+provide_name{"name": "Kelvin"}
    - slot{"name": "Kelvin"}
    - utter_greet_with_name
    - utter_ask_for_service
* ask_for_options
    - utter_options
    - utter_ask_for_nr_of_people
* provide_budget{"nr_of_people": "150", "room": "this"}
    - slot{"nr_of_people": "150"}
    - slot{"room": "this"}
    - utter_confirm
    - utter_options
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
    - utter_appreciation
    - utter_ask_for_additional_service
* farewell
    - utter_goodbye
* farewell
    - utter_thanks

## Generated Story 3406083726647241337
* greet
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Anna Oddermatt"}
    - slot{"name": "Anna Oddermatt"}
    - utter_ask_for_service_with_name
* ask_for_room_equipment
    - utter_confirm
    - utter_options
    - utter_ask_to_narrow_options
* ask_for_room_equipment
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* provide_nr_of_people{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_price
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_equipment{"room": "last"}
    - slot{"room": "last"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment
* ask_for_room_seating
    - utter_room_gamma_seating
* ask_for_room_lighting
    - utter_room_gamma_lighting
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_lighting
    - utter_room_beta_lighting
* ask_for_room_price{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_price
* reserve_room{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_confirm
    - utter_ask_for_booking_date
* provide_booking_date{"room": "it", "date": "28th of September 2019"}
    - slot{"date": "28th of September 2019"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
* thanks
    - utter_appreciation
    - utter_ask_for_additional_service
* deny
    - utter_goodbye
* farewell
    - utter_thanks

