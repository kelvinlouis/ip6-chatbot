## start_greet_without_name
* greet
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Hans"}
    - utter_greet_with_name
    - utter_ask_for_service

## start_greet_with_name
* greet+provide_name{"name": "Hans"}
    - utter_greet_with_name
    - utter_ask_for_service

## affirm
* affirm

## ask_for_directions_with_start_location
* ask_for_directions{"start_location": "train station"}
    - utter_directions_with_start_location

## ask_for_directions_without_start_location
* ask_for_directions
    - utter_directions_without_start_location

## ask_for_options
* ask_for_options

## deny
* deny

## disagree
* disagree

## farewell
* farewell

## provide_booking_date
* provide_booking_date
    - utter_ask_for_booking_date

## provide_booking_date_with_date
* provide_booking_date{"date": "28.11.2018"}
    - utter_ask_for_booking_confirmation

## provide_booking_date_with_time
* provide_booking_date{"time": "12:45"}
    - utter_ask_for_booking_date

## provide_booking_date_with_date_time
* provide_booking_date{"date": "28.11.2018", "time": "12:45"}
    - utter_ask_for_booking_confirmation

## provide_name
* provide_name
    - utter_ask_for_name

## provide_name_with_name
* provide_name{"name": "Hans"}

## provide_name_with_name_company
* provide_name{"name": "Hans", "company": "SBB"}

## provide_name_with_company
* provide_name{"company": "SBB"}

## provide_preference
* provide_preference
    - utter_ask_for_room

## provide_preference_with_room
* provide_preference{"room": "Alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}

## provide_room
* provide_room
    - utter_ask_for_room

## provide_room_with_room
* provide_room{"room": "Alpha"}

## reserve_room
* reserve_room
    - utter_ask_for_room

## reserve_room_with_room
* reserve_room{"room": "Alpha"}
    - utter_confirm_booking

## thanks
* thanks

## equipment_gamma
* ask_for_room_equipment{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment

## seating_gamma
* ask_for_room_seating{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating

## price_gamma
* ask_for_room_price{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price

## size_gamma
* ask_for_room_size{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_people_limit

## highlight_gamma
* ask_for_room_highlight{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_highlight

## lighting_gamma
* ask_for_room_lighting{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_lighting

## atmosphere_gamma
* ask_for_room_atmosphere{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere

## equipment_beta
* ask_for_room_equipment{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_equipment

## seating_beta
* ask_for_room_seating{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_seating

## price_beta
* ask_for_room_price{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_price

## size_beta
* ask_for_room_size{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_people_limit

## highlight_beta
* ask_for_room_highlight{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_highlight

## lighting_beta
* ask_for_room_lighting{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_lighting

## atmosphere_beta
* ask_for_room_atmosphere{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_atmosphere

## equipment_alpha
* ask_for_room_equipment{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment

## seating_alpha
* ask_for_room_seating{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_seating

## price_alpha
* ask_for_room_price{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price

## size_alpha
* ask_for_room_size{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_people_limit

## highlight_alpha
* ask_for_room_highlight{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_highlight

## lighting_alpha
* ask_for_room_lighting{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_lighting

## atmosphere_alpha
* ask_for_room_atmosphere{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_atmosphere

## provide_nr_of_people 90
* provide_nr_of_people{"nr_of_people": "90"}
    - slot{"nr_of_people": "90"}
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## provide_nr_of_people 200
* provide_nr_of_people{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## provide_nr_of_people 210
* provide_nr_of_people{"nr_of_people": "210"}
    - slot{"nr_of_people": "210"}
    - utter_room_alpha_people_limit

## provide_nr_of_people 250
* provide_nr_of_people{"nr_of_people": "250"}
    - slot{"nr_of_people": "250"}
    - utter_room_alpha_people_limit

## provide_nr_of_people 50
* provide_nr_of_people{"nr_of_people": "50"}
    - slot{"nr_of_people": "50"}
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## provide_nr_of_people 195
* provide_nr_of_people{"nr_of_people": "195"}
    - slot{"nr_of_people": "195"}
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## provide_budget 800
* provide_budget{"budget": "800"}
    - slot{"budget": "800"}
    - utter_budget_limitation_900

## provide_budget 900
* provide_budget{"budget": "900"}
    - slot{"budget": "900"}
    - utter_budget_limitation_900

## provide_budget 1000
* provide_budget{"budget": "1000"}
    - slot{"budget": "1000"}
    - utter_budget_limitation_900

## provide_budget 1100
* provide_budget{"budget": "1100"}
    - slot{"budget": "1100"}
    - utter_budget_limitation_1100

## provide_budget 1200
* provide_budget{"budget": "1200"}
    - slot{"budget": "1200"}
    - utter_budget_limitation_1100

## provide_budget 1300
* provide_budget{"budget": "1300"}
    - slot{"budget": "1300"}
    - utter_budget_limitation_1100

## provide_budget 1400
* provide_budget{"budget": "1400"}
    - slot{"budget": "1400"}
    - utter_budget_limitation_1400

## provide_budget 1500
* provide_budget{"budget": "1500"}
    - slot{"budget": "1500"}
    - utter_budget_limitation_1400

## provide_budget 1600
* provide_budget{"budget": "1600"}
    - slot{"budget": "1600"}
    - utter_budget_limitation_1400