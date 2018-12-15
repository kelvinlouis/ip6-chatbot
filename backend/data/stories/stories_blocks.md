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

## ask_for_directions_with_start_location
* ask_for_directions{"start_location": "train station"}
    - utter_directions_with_start_location

## ask_for_directions_without_start_location
* ask_for_directions
    - utter_directions_without_start_location

## reserve_room
* reserve_room
    - utter_ask_for_room

## provide_booking_date
* provide_booking_date
    - utter_ask_for_booking_date

## provide_booking_date_with_date
* provide_booking_date{"date": "28.11.2018"}
    - utter_ask_book_room
> ask_book_room_with_date

## provide_booking_date_with_time
* provide_booking_date{"time": "12:45"}
    - utter_ask_for_booking_date

## provide_booking_date_with_date_time
* provide_booking_date{"date": "28.11.2018", "time": "12:45"}
    - utter_ask_book_room
> ask_book_room_with_date

## affirm_booking
> ask_book_room_with_date
* affirm
    - utter_confirm_booking
    - utter_ask_for_additional_service
* deny
    - utter_goodbye

## deny_booking
> ask_book_room_with_date
* deny
    - utter_ask_for_room
> with_booking_date

## reserve_room_with_room_alpha
> with_booking_date
* reserve_room{"room": "alpha"}
    - action_correct_room
    - utter_confirm_booking

## reserve_room_with_room_beta
> with_booking_date
* reserve_room{"room": "beta"}
    - action_correct_room
    - utter_confirm_booking

## reserve_room_with_room_gamma
> with_booking_date
* reserve_room{"room": "Gamma"}
    - action_correct_room
    - utter_confirm_booking

## reserve_room_with_room_first
> with_booking_date
* reserve_room{"room": "first"}
    - action_correct_room
    - utter_confirm_booking

## reserve_room_with_room_second
> with_booking_date
* reserve_room{"room": "second"}
    - action_correct_room
    - utter_confirm_booking

## reserve_room_with_room_third
> with_booking_date
* reserve_room{"room": "third"}
    - action_correct_room
    - utter_confirm_booking

## reserve_room_with_room_last
> with_booking_date
* reserve_room{"room": "last"}
    - action_correct_room
    - utter_confirm_booking

## reserve_room_with_room_it
> with_booking_date
* reserve_room{"room": "it"}
    - utter_confirm_booking

## reserve_room_with_room_this
> with_booking_date
* reserve_room{"room": "this"}
    - action_correct_room
    - utter_confirm_booking

## reserve_room_with_room_the
> with_booking_date
* reserve_room{"room": "the"}
    - action_correct_room
    - utter_confirm_booking

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

## ask_book_room_with_room_alpha
* provide_preference{"room": "Alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_ask_book_room
> ask_book_room_with_room

## ask_book_room_with_room_beta
* provide_preference{"room": "Beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_ask_book_room
> ask_book_room_with_room

## ask_book_room_with_room_gamma
* provide_preference{"room": "Gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_ask_book_room
> ask_book_room_with_room

## deny_ask_book_room_with_room
> ask_book_room_with_room
* deny
    - utter_confirm_preference_negative

## affirm_ask_book_room_with_room
> ask_book_room_with_room
* affirm
    - utter_ask_for_booking_date

## provide_room
* provide_room
    - utter_ask_for_room

## equipment_ask_for_room
* ask_for_room_equipment
    - utter_ask_for_room
> equipment_ask_for_room

## equipment_alpha_provide_room
> equipment_ask_for_room
* provide_room{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment

## equipment_beta_provide_room
> equipment_ask_for_room
* provide_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_equipment

## equipment_gamma_provide_room
> equipment_ask_for_room
* provide_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment

## seating_ask_for_room
* ask_for_room_seating
    - utter_ask_for_room
> seating_ask_for_room

## seating_alpha_provide_room
> seating_ask_for_room
* provide_room{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_seating

## seating_beta_provide_room
> seating_ask_for_room
* provide_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_seating

## seating_gamma_provide_room
> seating_ask_for_room
* provide_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating

## price_ask_for_room
* ask_for_room_price
    - utter_ask_for_room
> price_ask_for_room

## price_alpha_provide_room
> price_ask_for_room
* provide_room{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price

## price_beta_provide_room
> price_ask_for_room
* provide_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_price

## price_gamma_provide_room
> price_ask_for_room
* provide_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price

## size_ask_for_room
* ask_for_room_size
    - utter_ask_for_room
> size_ask_for_room

## size_alpha_provide_room
> size_ask_for_room
* provide_room{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_people_limit

## size_beta_provide_room
> size_ask_for_room
* provide_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_people_limit

## size_gamma_provide_room
> size_ask_for_room
* provide_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_people_limit

## highlight_ask_for_room
* ask_for_room_highlight
    - utter_ask_for_room
> highlight_ask_for_room

## highlight_alpha_provide_room
> highlight_ask_for_room
* provide_room{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_highlight

## highlight_beta_provide_room
> highlight_ask_for_room
* provide_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_highlight

## highlight_gamma_provide_room
> highlight_ask_for_room
* provide_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_highlight

## lighting_ask_for_room
* ask_for_room_lighting
    - utter_ask_for_room
> lighting_ask_for_room

## lighting_alpha_provide_room
> lighting_ask_for_room
* provide_room{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_lighting

## lighting_beta_provide_room
> lighting_ask_for_room
* provide_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_lighting

## lighting_gamma_provide_room
> lighting_ask_for_room
* provide_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_lighting

## atmosphere_ask_for_room
* ask_for_room_atmosphere
    - utter_ask_for_room
> atmosphere_ask_for_room

## atmosphere_alpha_provide_room
> atmosphere_ask_for_room
* provide_room{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_atmosphere

## atmosphere_beta_provide_room
> atmosphere_ask_for_room
* provide_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_atmosphere

## atmosphere_gamma_provide_room
> atmosphere_ask_for_room
* provide_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere

## equipment_alpha
* ask_for_room_equipment{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment

## seating_alpha
* ask_for_room_seating{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - slot{"room": null}
    - utter_room_alpha_seating

## price_alpha
* ask_for_room_price{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - slot{"room": null}
    - utter_room_alpha_price

## size_alpha
* ask_for_room_size{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - slot{"room": null}
    - utter_room_alpha_people_limit

## highlight_alpha
* ask_for_room_highlight{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - slot{"room": null}
    - utter_room_alpha_highlight

## lighting_alpha
* ask_for_room_lighting{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - slot{"room": null}
    - utter_room_alpha_lighting

## atmosphere_alpha
* ask_for_room_atmosphere{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - slot{"room": null}
    - utter_room_alpha_atmosphere

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

## provide_nr_of_people 90
* provide_nr_of_people{"nr_of_people": "90"}
    - slot{"nr_of_people": "90"}
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_alpha_people_limit

## provide_nr_of_people 200
* provide_nr_of_people{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - utter_room_alpha_people_limit
    - utter_room_alpha_people_limit

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
    - utter_room_alpha_people_limit

## provide_nr_of_people 195
* provide_nr_of_people{"nr_of_people": "195"}
    - slot{"nr_of_people": "195"}
    - utter_room_alpha_people_limit
    - utter_room_alpha_people_limit

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

## farewell
* farewell
    - utter_goodbye