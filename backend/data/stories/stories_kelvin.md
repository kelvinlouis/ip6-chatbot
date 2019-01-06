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
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* ask_for_room_price{"room": "alpha"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price
* ask_for_room_atmosphere
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - utter_room_alpha_atmosphere
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_alpha_seating
* ask_for_room{"room": "third"}
    - slot{"room": "third"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating
* ask_for_room_price{"room": "this"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_price
* ask_for_room_equipment{"room": "this"}
    - action_set_topic
    - slot{"topic": "equipment"}
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
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_seating
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_alpha_seating
* ask_for_room{"room": "other"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_seating
    - utter_room_gamma_seating
* ask_for_room_price{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "price"}
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
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_confirm
    - utter_options
    - utter_ask_to_narrow_options
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
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
    - action_set_topic
    - slot{"topic": "price"}
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_equipment{"room": "last"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "last"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_gamma_seating
* ask_for_room_lighting
    - action_set_topic
    - slot{"topic": "lighting"}
    - utter_room_gamma_lighting
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_lighting
    - utter_room_beta_lighting
* ask_for_room_price{"room": "beta"}
    - action_set_topic
    - slot{"topic": "price"}
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

## Generated Story -4138610628731786766
* greet+provide_name{"name": "Leo Huppenbauer"}
    - slot{"name": "Leo Huppenbauer"}
    - utter_greet_with_name
    - utter_ask_for_service
* ask_for_room_size{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_available_rooms_200_people
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_price{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price
* ask_for_room{"room": "other"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_beta_price
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_gamma_equipment
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
* ask_for_room_seating{"room": "the"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_seating
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
    - utter_room_beta_seating
* ask_for_room_atmosphere{"room": "Gamma"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere
* ask_for_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_atmosphere
* provide_preference{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_ask_book_room
* provide_booking_date{"room": "it", "date": "21st of April 2019"}
    - slot{"date": "21st of April 2019"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
* thanks
    - utter_appreciation
    - utter_ask_for_additional_service
* ask_for_directions
    - utter_directions_without_start_location
* thanks
    - utter_appreciation
    - utter_ask_for_additional_service
* deny
    - utter_goodbye
* farewell
    - utter_thanks

## Generated Story -4138610628731786766 - 2
* greet+provide_name{"name": "Moritz Berger"}
    - slot{"name": "Moritz Berger"}
    - utter_greet_with_name
    - utter_ask_for_service
* ask_for_room_size{"nr_of_people": "250"}
    - slot{"nr_of_people": "250"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_available_rooms_270_people
    - utter_room_alpha_people_limit
* ask_for_room_price{"room": "alpha"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_alpha_equipment
* ask_for_room_seating{"room": "the"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_seating
    - utter_room_gamma_seating
* ask_for_room_atmosphere{"room": "Gamma"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere
* ask_for_room_price{"room": "Gamma"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price
* ask_for_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_atmosphere
* provide_preference{"room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_ask_book_room
* provide_booking_date{"room": "it", "date": "next month"}
    - slot{"date": "next month"}
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

## Generated Story 6808398299947786488
* greet
    - utter_greet
    - utter_ask_for_name
* greet+provide_name{"name": "Christoph Zeller"}
    - slot{"name": "Christoph Zeller"}
    - utter_ask_for_service_with_name
* provide_budget{"budget": "1500"}
    - slot{"budget": "1500"}
    - utter_budget_limitation_1400
* ask_for_options
    - utter_options
    - utter_ask_for_nr_of_people
* provide_nr_of_people{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - utter_confirm
    - utter_available_rooms_200_people
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_price{"room": "it"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_ask_for_room
* provide_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price
* ask_for_room{"room": "other"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_beta_price
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_gamma_seating
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_gamma_equipment
* ask_for_room_size{"room": "it"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_people_limit
* ask_for_room_lighting
    - action_set_topic
    - slot{"topic": "lighting"}
    - utter_ask_for_room
* ask_for_room{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_lighting
* ask_for_room_highlight{"room": "the"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_highlight
* ask_for_room{"room": "other"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_highlight
    - utter_room_beta_highlight
* provide_preference{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_ask_book_room
* affirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "next month"}
    - slot{"date": "next month"}
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
## Generated Story -5549234874568375575
* greet+provide_name{"name": "Chris"}
    - slot{"name": "Chris"}
    - utter_greet_with_name
    - utter_ask_for_service
* provide_budget{"budget": "1500.-"}
    - slot{"budget": "1500.-"}
    - utter_budget_limitation_1400
* ask_for_options
    - utter_options
    - utter_ask_for_nr_of_people
* provide_nr_of_people{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - utter_confirm
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_price{"room": "second"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "second"}
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
* ask_for_room_seating{"room": "the"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_seating
* ask_for_room{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating
* ask_for_room_atmosphere{"room": "the"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_atmosphere
* ask_for_room{"room": "first"}
    - slot{"room": "first"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_atmosphere
* ask_for_room_seating{"room": "there"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
* disagree
    - utter_dissatisfaction
    - utter_ask_for_alternative
* provide_preference{"room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_confirm_preference_positive
    - utter_ask_book_room
* affirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "16th of October in 2019"}
    - slot{"date": "16th of October in 2019"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
* thanks
    - utter_appreciation
    - utter_ask_for_additional_service
* ask_for_directions
    - utter_directions_without_start_location
* farewell
    - utter_goodbye

## Generated Story -6002812056623375490
* ask_for_room_size{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_alpha_people_limit
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_alpha_seating
    - utter_room_beta_seating
    - utter_room_gamma_seating
* affirm
    - utter_satisfied
    - utter_ask_for_additional_service
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* ask_for_room_equipment{"equipment": "video"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* ask_for_room_equipment{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment
* affirm
    - utter_ask_for_booking_date
* deny
    - utter_ask_for_additional_service
* ask_for_room_atmosphere{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere
* ask_for_room_equipment{"room": "it", "equipment": "stage"}
    - slot{"room": "it"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - utter_room_gamma_equipment
* ask_for_room_equipment{"room": "beta", "equipment": "stage"}
    - slot{"room": "beta"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - utter_room_beta_equipment
* thanks
    - utter_ask_for_additional_service
* reserve_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_ask_for_booking_date
* reserve_room{"date": "12th of january"}
    - slot{"date": "12th of january"}
    - utter_ask_book_room
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story -567897446373106099
* greet
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "sherin"}
    - slot{"name": "sherin"}
    - utter_ask_for_service_with_name
* ask_for_options
    - utter_options
* ask_for_room_size{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_confirm
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_equipment{"room": "other", "equipment": "stage"}
    - slot{"room": "other"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment
* ask_for_room_price
    - action_set_topic
    - slot{"topic": "price"}
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_lighting{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_lighting
* ask_for_room_equipment{"equipment": "audio system"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_gamma_equipment
* ask_for_room_seating{"room": "beta"}
    - slot{"room": "beta"}
    - action_set_topic
    - slot{"topic": "seating"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_seating
* ask_for_room_equipment{"equipment": "stage", "room": "beta"}
    - slot{"room": "beta"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_equipment
* ask_for_room_atmosphere{"room": "the"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_atmosphere
* ask_for_room_price{"room": "beta"}
    - slot{"room": "beta"}
    - action_set_topic
    - slot{"topic": "price"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_price
* provide_booking_date{"room": "beta", "date": "12th of december"}
    - slot{"date": "12th of december"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_thanks
    - utter_goodbye
* farewell
    - utter_thanks

## Generated Story -6758454970928526451
* greet+ask_for_room_size{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Adis Seferovic"}
    - slot{"name": "Adis Seferovic"}
    - utter_thanks_with_name
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* provide_preference{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_satisfied
    - utter_ask_for_additional_service
* ask_for_room_price
    - action_set_topic
    - slot{"topic": "price"}
    - utter_room_beta_price
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_beta_equipment
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_beta_seating
* affirm
    - utter_satisfied
    - utter_ask_for_additional_service
* ask_for_room_atmosphere{"room": "the"}
    - slot{"room": "the"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_atmosphere
* disagree
    - utter_dissatisfaction
    - utter_ask_for_alternative
* ask_for_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere
* ask_for_room_highlight{"room": "it"}
    - slot{"room": "it"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_highlight
* ask_for_room_price{"room": "it"}
    - slot{"room": "it"}
    - action_set_topic
    - slot{"topic": "price"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_price
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_gamma_equipment
* affirm
    - utter_satisfied
    - utter_ask_for_additional_service
* reserve_room{"room": "the"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_ask_book_room
* affirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "21st of June 2019"}
    - slot{"date": "21st of June 2019"}
    - utter_ask_for_booking_confirmation
* deny
    - utter_dissatisfaction
    - utter_ask_for_alternative
* provide_booking_date{"date": "22nd of June 2019"}
    - slot{"date": "22nd of June 2019"}
    - utter_ask_book_room
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* ask_for_directions
    - utter_directions_without_start_location
* farewell
    - utter_goodbye

## Generated Story 1173773893864298968
* greet
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Melvin Tats"}
    - slot{"name": "Melvin Tats"}
    - utter_ask_for_service_with_name
* ask_for_room_size{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_confirm
    - utter_available_rooms_200_people
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_price{"room": "last"}
    - slot{"room": "last"}
    - action_set_topic
    - slot{"topic": "price"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price
* affirm
    - utter_satisfied
    - utter_ask_for_additional_service
* ask_for_room_atmosphere{"room": "the"}
    - slot{"room": "the"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_atmosphere
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_gamma_seating
* ask_for_room{"room": "each"}
    - slot{"room": "each"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
    - utter_room_beta_seating
    - utter_room_gamma_seating
* ask_for_room_highlight{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_highlight
* affirm
    - utter_satisfied
    - utter_ask_for_additional_service
* provide_booking_date{"room": "the", "date": "21 December in 2019"}
    - slot{"date": "21 December in 2019"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
* ask_for_directions{"start_location": "airport"}
    - utter_directions_with_start_location
* thanks
    - utter_appreciation
    - utter_ask_for_additional_service
* deny
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story 2267034108717563910
* greet+ask_for_room_size{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Philipp Bachmann"}
    - slot{"name": "Philipp Bachmann"}
    - utter_thanks_with_name
    - utter_available_rooms_200_people
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_equipment{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment
* ask_for_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment
* ask_for_room_price
    - action_set_topic
    - slot{"topic": "price"}
    - utter_room_gamma_price
* ask_for_room{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price
* ask_for_room_atmosphere
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - utter_room_alpha_atmosphere
* ask_for_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere
* affirm
    - utter_satisfied
    - utter_ask_for_additional_service
* reserve_room{"room": "the"}
    - slot{"room": "the"}
    - action_default_fallback
    - rewind
* reserve_room{"room": "the"}
    - slot{"room": "the"}
    - action_correct_room
    - slot{"room": null}
    - utter_confirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "20th of January"}
    - slot{"date": "20th of January"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_goodbye
* farewell
    - utter_thanks

## Generated Story 5681509169342593390
* greet+ask_for_room_price{"budget": "2000 CHF"}
    - slot{"budget": "2000 CHF"}
    - action_set_topic
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Nicolas Cage"}
    - slot{"name": "Nicolas Cage"}
    - utter_thanks_with_name
    - utter_budget_limitation_1400
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price
* affirm
    - utter_satisfied
    - utter_ask_for_additional_service
* reserve_room
    - utter_ask_for_room
* provide_room{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_ask_for_booking_date
* provide_booking_date{"date": "20. December"}
    - slot{"date": "20. December"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_goodbye
* thanks
    - utter_thanks

