## Generated Story -8897532857795406961.1
* greet
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Nicola"}
    - slot{"name": "Nicola"}
    - utter_ask_for_service_with_name
* reserve_room{"company": "Novartis"}
    - slot{"company": "Novartis"}
    - utter_confirm
    - utter_options
    - utter_ask_to_narrow_options
* ask_for_room_equipment
    - utter_ask_for_nr_of_people
> 8897532857795406961_nr_of_people.1

## Generated Story -8897532857795406961.2.1
> 8897532857795406961_room_price.ac
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
    - utter_room_gamma_price
* ask_for_room_atmosphere{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_atmosphere
> 8897532857795406961.3

## Generated Story -8897532857795406961.2.2
> 8897532857795406961_room_price.abc
* ask_for_room_price{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"room": null}
    - slot{"current_room": "Beta"}
    - utter_room_beta_price
* ask_for_room_price{"room": "other"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_gamma_price
* ask_for_room_atmosphere{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_atmosphere
> 8897532857795406961.3

## Generated Story -8897532857795406961.2.3
> 8897532857795406961_room_price.a
* ask_for_room_price{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"room": null}
    - slot{"current_room": "Gamma"}
    - utter_room_gamma_price
* ask_for_room_price{"room": "other"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
* ask_for_room_atmosphere{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_atmosphere
> 8897532857795406961.3

## Generated Story -8897532857795406961.3
> 8897532857795406961.3
* ask_for_room_seating
    - utter_room_gamma_seating
* reserve_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"room": null}
    - slot{"current_room": "Gamma"}
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_thanks_with_name
    - utter_goodbye
* farewell

## provide_number_of_people 1
> 8897532857795406961_nr_of_people.1
* provide_nr_of_people{"nr_of_people": "90"}
    - slot{"nr_of_people": "90"}
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
> 8897532857795406961_room_price.abc

## provide_number_of_people 2
> 8897532857795406961_nr_of_people.1
* provide_nr_of_people{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit
> 8897532857795406961_room_price.ac

## provide_number_of_people 3
> 8897532857795406961_nr_of_people.1
* provide_nr_of_people{"nr_of_people": "210"}
    - slot{"nr_of_people": "210"}
    - utter_room_alpha_people_limit
> 8897532857795406961_room_price.a

## provide_number_of_people 4
> 8897532857795406961_nr_of_people.1
* provide_nr_of_people{"nr_of_people": "250"}
    - slot{"nr_of_people": "250"}
    - utter_room_alpha_people_limit
> 8897532857795406961_room_price.a

## provide_number_of_people 5
> 8897532857795406961_nr_of_people.1
* provide_nr_of_people{"nr_of_people": "50"}
    - slot{"nr_of_people": "50"}
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
> 8897532857795406961_room_price.abc

## provide_number_of_people 5
> 8897532857795406961_nr_of_people.1
* provide_nr_of_people{"nr_of_people": "195"}
    - slot{"nr_of_people": "195"}
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit
> 8897532857795406961_room_price.ac

## Generated Story -3982048685169040827
* greet
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Nico"}
    - slot{"name": "Nico"}
    - utter_ask_for_service_with_name
* ask_for_room_equipment
    - utter_confirm
    - utter_options
    - utter_ask_to_narrow_options
* ask_for_room_size{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit
> 3982048685169040827.1

## equipment_alpha_alpha
> 3982048685169040827.1
* ask_for_room_equipment{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment
> equipment_alpha

## equipment_beta_beta
> 3982048685169040827.1
* ask_for_room_equipment{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_equipment
> equipment_beta

## equipment_gamma_gamma
> 3982048685169040827.1
* ask_for_room_equipment{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment
> equipment_gamma

## seating_alpha_this
> equipment_alpha
* ask_for_room_seating{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
> 3982048685169040827.3

## price_alpha_this
> equipment_alpha
* ask_for_room_price{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
> 3982048685169040827.3

## seating_beta_this
> equipment_beta
* ask_for_room_seating{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_seating
> 3982048685169040827.3

## seating_gamma_this
> equipment_gamma
* ask_for_room_seating{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_seating
> 3982048685169040827.3

## 3982048685169040827.3
> 3982048685169040827.3
* ask_for_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating
* ask_for_room_price{"room": "it"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_price
* reserve_room{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_confirm
    - utter_ask_for_booking_date
* provide_booking_date{"date": "12.05.2019"}
    - slot{"date": "12.05.2019"}
    - utter_ask_for_booking_confirmation
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_goodbye
## Generated Story 5286531684760156366
* ask_for_options
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Joel Fischer"}
    - slot{"name": "Joel Fischer"}
    - utter_ask_to_narrow_options
* ask_for_room_equipment{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - utter_confirm
    - utter_available_rooms_200_people
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_price{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price
* ask_for_room_seating{"room": "this"}
    - slot{"room": "this"}
    - utter_room_alpha_seating
* ask_for_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating
* ask_for_room_price{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_gamma_price
* provide_booking_date{"room": "this", "date": "23.03.2019"}
    - slot{"date": "23.03.2019"}
    - slot{"room": "this"}
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

