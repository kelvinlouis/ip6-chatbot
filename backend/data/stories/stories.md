## 1 (Nicola)
* greet
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "John Smith"}
    - utter_ask_for_service_with_name
* ask_for_room_equipment
    - utter_confirm
    - utter_options
    - utter_ask_to_narrow_options
* ask_for_room_size{"nr_of_people": "100"}
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_seating{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating
* ask_for_room{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_seating
* ask_for_room{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_seating
* ask_for_room_price{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price
    - utter_ask_for_confirmation
* affirm
    - utter_confirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "23-03-2019"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_goodbye
* farewell

## inspired by chat 1-6 (Nicola)
* ask_for_options
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Luca Hauser"}
    - utter_greet_with_name
    - utter_ask_for_service
* ask_for_room_size{"nr_of_people": "150"}
    - utter_confirm
    - utter_available_rooms_150_people
* ask_for_room_equipment
    - utter_generic_equipment_options
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* ask_for_room_seating
    - utter_room_alpha_seating
    - utter_room_beta_seating
    - utter_room_gamma_seating
* ask_for_room_atmosphere
    - utter_room_alpha_atmosphere
    - utter_room_beta_atmosphere
    - utter_room_gamma_atmosphere
* provide_budget{"budget": "1500"}
    - utter_enough_budget
* provide_preference{"room": "third"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_confirm_preference_positive
    - utter_room_gamma_price
* reserve_room
    - utter_confirm_booking
* thanks
    - utter_appreciation
    - utter_ask_for_additional_service
* farewell OR deny
    - utter_goodbye

## inspired by chat 9-10 (Kelvin)
* ask_for_options
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Jennifer Meier"}
    - utter_ask_for_nr_of_people
* provide_nr_of_people{"nr_of_people": "150"}
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_equipment
    - utter_ask_for_room
* provide_room{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment
* ask_for_room_price{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price
* provide_budget{"budget": "1500"}
    - utter_confirm
    - utter_budget_limitation_1400
* ask_for_room{"room": "others"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_size{"room": "others"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_atmosphere
    - utter_room_alpha_atmosphere
* ask_for_room{"room": "others"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_beta_atmosphere
    - utter_room_gamma_atmosphere
* ask_for_room{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_ask_what_info
* ask_for_room_equipment
    - utter_room_gamma_equipment
* provide_preference
    - utter_ask_book_room
* affirm
    - utter_confirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "12.01.2019"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
* thanks
    - utter_appreciation
    - utter_ask_for_additional_service
* farewell OR deny
    - utter_goodbye

## inspired by chat 11-12 (Kelvin)
* ask_for_options
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Mark"}
    - utter_ask_for_nr_of_people
* ask_for_room_size{"nr_of_people": "150"}
    - utter_confirm
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_equipment
    - utter_generic_equipment_options
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* provide_budget{"budget": "1500"}
    - utter_confirm
    - utter_budget_limitation_1400
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_highlight
    - utter_room_alpha_highlight
    - utter_room_beta_highlight
    - utter_room_gamma_highlight
* ask_for_room_atmosphere{"room": "second"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_atmosphere
* ask_for_room_seating
    - utter_room_alpha_seating
    - utter_room_beta_seating
    - utter_room_gamma_seating
* reserve_room
    - utter_ask_book_room
* provide_booking_date{"date": "12.02.2018", "time": "09:00"}
    - utter_ask_for_booking_confirmation
* deny OR provide_booking_date{"date": "13.02.2018"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_thanks
    - utter_goodbye
* thanks OR farewell
    - utter_thanks

## inspired by chat 13-14 (Kelvin)
* greet+provide_name{"name": "Arjen Bershka"}
    - utter_greet_with_name
    - utter_ask_for_service
* ask_for_options
    - utter_options
    - utter_ask_for_nr_of_people
* ask_for_room_size{"nr_of_people": "150"}
    - utter_confirm
    - utter_options
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_equipment
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* ask_for_room_seating
    - utter_room_alpha_seating
    - utter_room_beta_seating
    - utter_room_gamma_seating
* provide_budget{"budget": "1500"}
    - utter_confirm
    - utter_budget_limitation_1400
* ask_for_room_highlight{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_highlight
* ask_for_room{"room": "other"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_alpha_highlight
    - utter_room_gamma_highlight
* ask_for_room_price{"room": "third"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price
* provide_preference{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_ask_book_room
* ask_for_room_price{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_ask_for_confirmation
* affirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "12th of September"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny OR farewell
    - utter_goodbye
* thanks
    - utter_thanks

## inspired by chat 3-2 (Kelvin)
* greet+provide_name{"name": "Laura Steiner", "company": "Inselspital"}
    - utter_greet_with_name
    - utter_ask_for_service
* ask_for_room_size{"nr_of_people": "150"}
    - utter_available_rooms_150_people
    - utter_ask_what_info
* ask_for_room_equipment
    - utter_generic_equipment_options
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* ask_for_room_seating
    - utter_room_alpha_seating
    - utter_room_beta_seating
    - utter_room_gamma_seating
* ask_for_room_lighting{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_lighting
* ask_for_room_price{"room": "it"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price
* reserve_room{"room": "first"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_confirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "05.08.2019"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny OR farewell
    - utter_goodbye
* thanks
    - utter_thanks

## Inspired by chat 5-4 (Johanna)
* ask_for_options
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Mergime"}
    - utter_ask_for_nr_of_people
* ask_for_room_size{"nr_of_people": "150"}
    - utter_thanks_with_name
    - utter_confirm
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_equipment
    - utter_generic_equipment_options
    - utter_ask_for_room
* provide_room{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_equipment
* ask_for_room_seating{"room": "it"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_seating
* ask_for_room_price{"room": "the"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_price
* affirm
    - utter_appreciation
    - utter_ask_for_additional_service
* ask_for_room{"room": "other"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_gamma_price
* ask_for_room_atmosphere{"room": "first"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_atmosphere
* ask_for_room_seating{"room": "it"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_seating
* ask_for_room{"room": "others"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_beta_atmosphere
    - utter_room_gamma_atmosphere
* disagree
    - utter_confirm_preference_negative
* provide_preference{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_confirm_preference_positive
    - utter_ask_for_booking_confirmation
* affirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "1.1.2020"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
* thanks
    - utter_thanks
