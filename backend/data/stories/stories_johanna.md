## Generated Story -2356003198837254943
* greet
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Hans"}
    - slot{"name": "Hans"}
    - utter_ask_for_service_with_name
* ask_for_options
    - utter_confirm
    - utter_options
    - utter_ask_to_narrow_options
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_ask_for_nr_of_people
* provide_nr_of_people{"nr_of_people": "180"}
    - slot{"nr_of_people": "180"}
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_atmosphere{"room": "first"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "first"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment
* ask_for_room_seating{"room": "this"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
* ask_for_room{"room": "other"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_seating
    - utter_room_gamma_seating
* ask_for_room_price{"room": "beta"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_price
* ask_for_room_price{"room": "others"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_gamma_price
* reserve_room{"room": "the"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_confirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "12.03.2019"}
    - slot{"date": "12.03.2019"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_thanks
    - utter_goodbye
* farewell
    - utter_thanks

## Generated Story -1049300769894828425
* greet
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Yin"}
    - slot{"name": "Yin"}
    - utter_ask_for_service_with_name
* ask_for_options
    - utter_confirm
    - utter_options
* ask_for_room_size{"nr_of_people": "150"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"nr_of_people": "150"}
    - utter_confirm
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_price
    - action_set_topic
    - slot{"topic": "price"}
    - utter_ask_for_room
* provide_room{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price
* ask_for_room{"room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_price
* provide_room{"room": "last"}
    - slot{"room": "last"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price
* ask_for_room_atmosphere
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - utter_ask_for_room
* provide_room{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere
* ask_for_room_atmosphere{"room": "Beta"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_atmosphere
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_beta_seating
    - utter_room_beta_seating
* provide_preference
    - utter_ask_book_room
* provide_booking_date{"date": "15th of April 2020"}
    - slot{"date": "15th of April 2020"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
* thanks
    - utter_goodbye
* farewell
    - utter_thanks

## Generated Story -4072066764741267877
* greet
    - utter_greet
    - utter_ask_for_service
* provide_nr_of_people{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_options
    - utter_ask_what_info
* ask_for_room_equipment{"room": "the"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "the"}
    - utter_ask_for_room
* provide_room{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment
* ask_for_room{"room": "second"}
    - slot{"room": "second"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_equipment
* provide_room{"room": "last"}
    - slot{"room": "last"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment
* ask_for_room_price
    - action_set_topic
    - slot{"topic": "price"}
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_atmosphere
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - utter_room_alpha_atmosphere
    - utter_room_beta_atmosphere
    - utter_room_gamma_atmosphere
* ask_for_room_highlight
    - action_set_topic
    - slot{"topic": "highlight"}
    - utter_room_beta_highlight
    - utter_room_gamma_highlight
    - utter_room_alpha_highlight
* ask_for_room_seating{"room": "Beta"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_seating
* reserve_room{"room": "it"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_confirm
    - utter_ask_for_booking_date
* provide_booking_date
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_thanks
    - utter_goodbye
* farewell

## Generated Story -4473528322610655305
* greet+ask_for_options
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Donita"}
    - slot{"name": "Donita"}
    - utter_greet_with_name
    - utter_ask_for_service
* ask_for_options
    - utter_options
    - utter_ask_for_nr_of_people
* provide_nr_of_people{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_atmosphere{"room": "Alpha"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_atmosphere
* ask_for_room_lighting
    - action_set_topic
    - slot{"topic": "lighting"}
    - action_correct_room
    - utter_room_alpha_lighting
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - action_correct_room
    - utter_room_alpha_equipment
* ask_for_room_price{"room": "it"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
* ask_for_room_price{"room": "others"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - action_correct_room
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* ask_for_room_atmosphere
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - utter_room_gamma_atmosphere
    - utter_room_beta_atmosphere
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - action_correct_room
    - utter_room_gamma_seating
    - utter_room_beta_seating
* reserve_room{"room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_confirm
    - utter_ask_for_booking_date
* ask_for_room_equipment{"room": "it"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_equipment
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_beta_seating
* reserve_room{"room": "it"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_confirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "24 July 2019"}
    - slot{"date": "24 July 2019"}
    - utter_ask_for_booking_confirmation
* thanks
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_thanks
    - utter_goodbye

