## start_greet_without_name_and_ask_for_service_with_name
* greet
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Hans"}
    - slot{"name": "Hans"}
    - utter_ask_for_service_with_name

## start_greet_with_name
* greet+provide_name{"name": "Hans"}
    - slot{"name": "Hans"}
    - utter_greet_with_name
    - utter_ask_for_service

## start_greet_and_ask_for_service_with_name
* greet+provide_name{"name": "Hans"}
    - slot{"name": "Hans"}
    - utter_greet
    - utter_ask_for_service_with_name

## start_greet_with_name_and_150_noofpeople
* greet+provide_name{"name": "Hans", "nr_of_people": "150"}
    - slot{"name": "Hans"}
    - slot{"nr_of_people": "150"}
    - utter_greet_with_name
    - utter_available_rooms_150_people

## start_greet_with_name_and_200_noofpeople
* greet+provide_name{"name": "Hans", "nr_of_people": "200"}
    - slot{"name": "Hans"}
    - slot{"nr_of_people": "200"}
    - utter_greet_with_name
    - utter_available_rooms_200_people

## start_greet_with_name_and_270_noofpeople
* greet+provide_name{"name": "Hans", "nr_of_people": "270"}
    - slot{"name": "Hans"}
    - slot{"nr_of_people": "270"}
    - utter_greet_with_name
    - utter_available_rooms_270_people

## start_greet_with_name_and_provide_budget 900
* greet+provide_name{"name": "Hans", "budget": "900"}
    - slot{"name": "Hans"}
    - slot{"budget": "900"}
    - utter_greet_with_name
    - utter_budget_limitation_900

## start_greet_with_name_and_provide_budget 1100
* greet+provide_name{"name": "Hans", "budget": "1100"}
    - slot{"name": "Hans"}
    - slot{"budget": "1100"}
    - utter_greet_with_name
    - utter_budget_limitation_1100

## start_greet_with_name_and_provide_budget 1400
* greet+provide_name{"name": "Hans", "budget": "1400"}
    - slot{"name": "Hans"}
    - slot{"budget": "1400"}
    - utter_greet_with_name
    - utter_budget_limitation_1400

## start_greet_without_name_ask_for_room_size 150
* greet+ask_for_room_size{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michael"}
    - slot{"name": "Michael"}
    - utter_thanks_with_name
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## start_greet_without_name_ask_for_room_size 150 twice
* greet+ask_for_room_size{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Magdalena"}
    - slot{"name": "Magdalena"}
    - utter_thanks_with_name
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## start_greet_with_name_ask_for_room_size 150
* greet+ask_for_room_size{"name": "Michael", "nr_of_people": "150"}
    - slot{"name": "Michael"}
    - slot{"nr_of_people": "150"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet_with_name
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## start_greet_without_name_ask_for_room_size 200
* greet+ask_for_room_size{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Lionell"}
    - slot{"name": "Lionell"}
    - utter_thanks_with_name
    - utter_available_rooms_200_people
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## start_greet_with_name_ask_for_room_size 200
* greet+ask_for_room_size{"name": "Lionell", "nr_of_people": "200"}
    - slot{"name": "Lionell"}
    - slot{"nr_of_people": "200"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet_with_name
    - utter_available_rooms_200_people
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## start_greet_without_name_ask_for_room_size 270
* greet+ask_for_room_size{"nr_of_people": "270"}
    - slot{"nr_of_people": "270"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Martina"}
    - slot{"name": "Martina"}
    - utter_thanks_with_name
    - utter_available_rooms_270_people
    - utter_room_alpha_people_limit

## start_greet_with_name_ask_for_room_size 270
* greet+ask_for_room_size{"name": "Martina", "nr_of_people": "270"}
    - slot{"name": "Martina"}
    - slot{"nr_of_people": "270"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet_with_name
    - utter_available_rooms_270_people
    - utter_room_alpha_people_limit

## start_greet_without_name_ask_for_room_size Alpha
* greet+ask_for_room_size{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michel"}
    - slot{"name": "Michel"}
    - utter_thanks_with_name
    - utter_room_alpha_people_limit

## start_greet_without_name_ask_for_room_size Beta
* greet+ask_for_room_size{"room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michel"}
    - slot{"name": "Michel"}
    - utter_thanks_with_name
    - utter_room_beta_people_limit

## start_greet_without_name_ask_for_room_size Gamma
* greet+ask_for_room_size{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michel"}
    - slot{"name": "Michel"}
    - utter_thanks_with_name
    - utter_room_gamma_people_limit

## start_greet_with_name_ask_for_room_size Beta
* greet+ask_for_room_size{"name": "Martina", "room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"name": "Martina"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_greet_with_name
    - utter_room_beta_people_limit

## start_greet_without_name_ask_for_room_price 900
* greet+ask_for_room_price{"budget": "900"}
    - slot{"budget": "900"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michael"}
    - slot{"name": "Michael"}
    - utter_thanks_with_name
    - utter_budget_limitation_900
    - utter_room_beta_price

## start_greet_with_name_ask_for_room_price 900
* greet+ask_for_room_price{"name": "Michael", "budget": "900"}
    - slot{"name": "Michael"}
    - slot{"budget": "900"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_greet_with_name
    - utter_budget_limitation_900
    - utter_room_beta_price

## start_greet_without_name_ask_for_room_price 1100
* greet+ask_for_room_price{"budget": "1100"}
    - slot{"budget": "1100"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Lionell"}
    - slot{"name": "Lionell"}
    - utter_thanks_with_name
    - utter_budget_limitation_1100
    - utter_room_beta_price
    - utter_room_gamma_price

## start_greet_with_name_ask_for_room_price 1100
* greet+ask_for_room_price{"name": "Lionell", "budget": "1100"}
    - slot{"budget": "1100"}
    - slot{"name": "Lionell"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_greet_with_name
    - utter_budget_limitation_1100
    - utter_room_beta_price
    - utter_room_gamma_price

## start_greet_without_name_ask_for_room_price 1400
* greet+ask_for_room_price{"budget": "1400"}
    - slot{"budget": "1400"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Martina"}
    - slot{"name": "Martina"}
    - utter_thanks_with_name
    - utter_budget_limitation_1400
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price

## start_greet_with_name_ask_for_room_price 1400
* greet+ask_for_room_price{"name": "Martina", "budget": "1400"}
    - slot{"budget": "1400"}
    - slot{"name": "Martina"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_greet_with_name
    - utter_budget_limitation_1400
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price

## start_greet_without_name_ask_for_room_price Alpha
* greet+ask_for_room_price{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michel"}
    - slot{"name": "Michel"}
    - utter_thanks_with_name
    - utter_room_alpha_price

## start_greet_without_name_ask_for_room_price Beta
* greet+ask_for_room_price{"room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michel"}
    - slot{"name": "Michel"}
    - utter_thanks_with_name
    - utter_room_beta_price

## start_greet_without_name_ask_for_room_price Gamma
* greet+ask_for_room_price{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michel"}
    - slot{"name": "Michel"}
    - utter_thanks_with_name
    - utter_room_gamma_price

## start_greet_with_name_ask_for_room_price Beta
* greet+ask_for_room_price{"name": "Martina", "room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"name": "Martina"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_greet_with_name
    - utter_room_beta_price

## start_greet_without_name_ask_for_room_equipment
* greet+ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Natascha"}
    - slot{"name": "Natascha"}
    - utter_thanks_with_name
    - utter_generic_equipment_options

## start_greet_with_name_ask_for_room_equipment
* greet+ask_for_room_equipment{"name": "Natascha"}
    - slot{"name": "Natascha"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_greet_with_name
    - utter_generic_equipment_options

## start_greet_without_name_ask_for_room_equipment Alpha
* greet+ask_for_room_equipment{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michel"}
    - slot{"name": "Michel"}
    - utter_thanks_with_name
    - utter_room_alpha_equipment

## start_greet_without_name_ask_for_room_equipment Beta
* greet+ask_for_room_equipment{"room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michel"}
    - slot{"name": "Michel"}
    - utter_thanks_with_name
    - utter_room_beta_equipment

## start_greet_without_name_ask_for_room_equipment Gamma
* greet+ask_for_room_equipment{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Michel"}
    - slot{"name": "Michel"}
    - utter_thanks_with_name
    - utter_room_gamma_equipment

## start_greet_with_name_ask_for_room_equipment Alpha
* greet+ask_for_room_equipment{"name": "Martina", "room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"name": "Martina"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_greet_with_name
    - utter_room_alpha_equipment

## start_greet_without_name_ask_for_options
* greet+ask_for_options
    - utter_greet
    - utter_ask_for_name
* provide_name{"name": "Nathalie"}
    - slot{"name": "Nathalie"}
    - utter_thanks_with_name
    - utter_options
    - utter_ask_to_narrow_options

## start_greet_with_name_ask_for_options
* greet+ask_for_options{"name": "Nathalie"}
    - slot{"name": "Nathalie"}
    - utter_greet_with_name
    - utter_options
    - utter_ask_to_narrow_options

## ask_for_directions_with_start_location
* ask_for_directions{"start_location": "train station"}
    - slot{"start_location": "train station"}
    - utter_directions_with_start_location

## ask_for_directions_without_start_location
* ask_for_directions
    - utter_directions_without_start_location

## reserve_room
    - slot{"current_room": null}
* reserve_room
    - utter_ask_for_room

## provide_booking_date
* provide_booking_date
    - utter_ask_for_booking_date

## provide_booking_date_with_date
* provide_booking_date{"date": "28.11.2018"}
    - slot{"date": "28.11.2018"}
    - utter_ask_book_room
> ask_book_room_with_date

## provide_booking_date_with_time
* provide_booking_date{"time": "12:45"}
    - slot{"time": "12:45"}
    - utter_ask_for_booking_date

## provide_booking_date_with_date_time
* provide_booking_date{"date": "28.11.2018", "time": "12:45"}
    - slot{"date": "28.11.2018"}
    - slot{"time": "12:45"}
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

## reserve_room_alpha_without_date
    - slot{"date": null}
* reserve_room{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_ask_for_booking_date

## reserve_room_beta_without_date
    - slot{"date": null}
* reserve_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_ask_for_booking_date

## reserve_room_gamma_without_date
    - slot{"date": null}
* reserve_room{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_ask_for_booking_date

## reserve_room_this_without_date
    - slot{"date": null}
* reserve_room{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_ask_for_booking_date

## reserve_room_with_room_alpha
    - slot{"date": "28.11.2018"}
* reserve_room{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_confirm_booking

## reserve_room_with_room_beta
    - slot{"date": "28.11.2018"}
* reserve_room{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_confirm_booking

## reserve_room_with_room_gamma
    - slot{"date": "28.11.2018"}
* reserve_room{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_confirm_booking

## reserve_room_with_room_it
    - slot{"date": "28.11.2018"}
* reserve_room{"room": "it"}
    - slot{"room": "it"}
    - action_correct_room
    - slot{"room": null}
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
    - utter_confirm
    - utter_ask_for_room

## ask_for_room_catering_no_room
* ask_for_room_catering
    - utter_catering_options

## ask_for_room_catering_alpha
* ask_for_room_catering{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_catering_options

## ask_for_room_catering_beta
* ask_for_room_catering{"room": "beta"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_catering_options

## ask_for_room_catering_gamma
* ask_for_room_catering{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_catering_options

## ask_for_room_catering_all
* ask_for_room_catering{"room": "all"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_catering_options

## ask_for_room_catering_other
* ask_for_room_catering{"room": "other"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_catering_options

## ask_for_room_catering_this
* ask_for_room_catering{"room": "this"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"room": null}
    - utter_catering_options

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
    - utter_dissatisfaction
    - utter_ask_for_alternative

## affirm_ask_book_room_with_room
> ask_book_room_with_room
* affirm
    - utter_ask_for_booking_date

## provide_room
* provide_room
    - utter_ask_for_room

## equipment_ask_for_room
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
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

## equipment_all_provide_room
> equipment_ask_for_room
* provide_room{"room": "all"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment

## seating_ask_for_room
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
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

## seating_all_provide_room
> seating_ask_for_room
* provide_room{"room": "all"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
    - utter_room_beta_seating
    - utter_room_gamma_seating

## price_ask_for_room
* ask_for_room_price
    - action_set_topic
    - slot{"topic": "price"}
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

## price_all_provide_room
> price_ask_for_room
* provide_room{"room": "all"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price

## size_ask_for_room
* ask_for_room_size
    - action_set_topic
    - slot{"topic": "size"}
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

## size_all_provide_room
> size_ask_for_room
* provide_room{"room": "all"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## highlight_ask_for_room
* ask_for_room_highlight
    - action_set_topic
    - slot{"topic": "highlight"}
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

## highlight_all_provide_room
> highlight_ask_for_room
* provide_room{"room": "all"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_highlight
    - utter_room_beta_highlight
    - utter_room_gamma_highlight

## lighting_ask_for_room
* ask_for_room_lighting
    - action_set_topic
    - slot{"topic": "lighting"}
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

## lighting_all_provide_room
> lighting_ask_for_room
* provide_room{"room": "all"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_lighting
    - utter_room_beta_lighting
    - utter_room_gamma_lighting

## atmosphere_ask_for_room
* ask_for_room_atmosphere
    - action_set_topic
    - slot{"topic": "atmosphere"}
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

## atmosphere_all_provide_room
> atmosphere_ask_for_room
* provide_room{"room": "all"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_atmosphere
    - utter_room_beta_atmosphere
    - utter_room_gamma_atmosphere

## equipment_alpha
* ask_for_room_equipment{"room": "alpha"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment

## seating_alpha
* ask_for_room_seating{"room": "alpha"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_seating

## price_alpha
* ask_for_room_price{"room": "alpha"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price

## size_alpha
* ask_for_room_size{"room": "alpha"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_people_limit

## highlight_alpha
* ask_for_room_highlight{"room": "alpha"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_highlight

## lighting_alpha
* ask_for_room_lighting{"room": "alpha"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_lighting

## atmosphere_alpha
* ask_for_room_atmosphere{"room": "alpha"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_atmosphere

## equipment_beta
* ask_for_room_equipment{"room": "beta"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_equipment

## seating_beta
* ask_for_room_seating{"room": "beta"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_seating

## price_beta
* ask_for_room_price{"room": "beta"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_price

## size_beta
* ask_for_room_size{"room": "beta"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_people_limit

## highlight_beta
* ask_for_room_highlight{"room": "beta"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_highlight

## lighting_beta
* ask_for_room_lighting{"room": "beta"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_lighting

## atmosphere_beta
* ask_for_room_atmosphere{"room": "beta"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_atmosphere

## equipment_gamma
* ask_for_room_equipment{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment

## seating_gamma
* ask_for_room_seating{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating

## price_gamma
* ask_for_room_price{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price

## size_gamma
* ask_for_room_size{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_people_limit

## highlight_gamma
* ask_for_room_highlight{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_highlight

## lighting_gamma
* ask_for_room_lighting{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_lighting

## atmosphere_gamma
* ask_for_room_atmosphere{"room": "gamma"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere

## equipment_alpha_this
    - slot{"current_room": "Alpha"}
* ask_for_room_equipment{"room": "this"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment

## seating_alpha_this
    - slot{"current_room": "Alpha"}
* ask_for_room_seating{"room": "this"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_seating

## price_alpha_this
    - slot{"current_room": "Alpha"}
* ask_for_room_price{"room": "this"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price

## size_alpha_this
    - slot{"current_room": "Alpha"}
* ask_for_room_size{"room": "this"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_people_limit

## highlight_alpha_this
    - slot{"current_room": "Alpha"}
* ask_for_room_highlight{"room": "this"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_highlight

## lighting_alpha_this
    - slot{"current_room": "Alpha"}
* ask_for_room_lighting{"room": "this"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_lighting

## atmosphere_alpha_this
    - slot{"current_room": "Alpha"}
* ask_for_room_atmosphere{"room": "this"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_atmosphere

## equipment_beta_this
    - slot{"current_room": "Beta"}
* ask_for_room_equipment{"room": "this"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_equipment

## seating_beta_this
    - slot{"current_room": "Beta"}
* ask_for_room_seating{"room": "this"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_seating

## price_beta_this
    - slot{"current_room": "Beta"}
* ask_for_room_price{"room": "this"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_price

## size_beta_this
    - slot{"current_room": "Beta"}
* ask_for_room_size{"room": "this"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_people_limit

## highlight_beta_this
    - slot{"current_room": "Beta"}
* ask_for_room_highlight{"room": "this"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_highlight

## lighting_beta_this
    - slot{"current_room": "Beta"}
* ask_for_room_lighting{"room": "this"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_lighting

## atmosphere_beta_this
    - slot{"current_room": "Beta"}
* ask_for_room_atmosphere{"room": "this"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_atmosphere

## equipment_gamma_this
    - slot{"current_room": "Gamma"}
* ask_for_room_equipment{"room": "this"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment

## seating_gamma_this
    - slot{"current_room": "Gamma"}
* ask_for_room_seating{"room": "this"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating

## price_gamma_this
    - slot{"current_room": "Gamma"}
* ask_for_room_price{"room": "this"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price

## size_gamma_this
    - slot{"current_room": "Gamma"}
* ask_for_room_size{"room": "this"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_people_limit

## highlight_gamma_this
    - slot{"current_room": "Gamma"}
* ask_for_room_highlight{"room": "this"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_highlight

## lighting_gamma_this
    - slot{"current_room": "Gamma"}
* ask_for_room_lighting{"room": "this"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_lighting

## atmosphere_gamma_this
    - slot{"current_room": "Gamma"}
* ask_for_room_atmosphere{"room": "this"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "this"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere

## equipment_alpha_from_context
    - slot{"current_room": "Alpha"}
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_alpha_equipment

## seating_alpha_from_context
    - slot{"current_room": "Alpha"}
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_alpha_seating

## price_alpha_from_context
    - slot{"current_room": "Alpha"}
* ask_for_room_price
    - action_set_topic
    - slot{"topic": "price"}
    - utter_room_alpha_price

## size_alpha_from_context
    - slot{"current_room": "Alpha"}
* ask_for_room_size
    - action_set_topic
    - slot{"topic": "size"}
    - utter_room_alpha_people_limit

## highlight_alpha_from_context
    - slot{"current_room": "Alpha"}
* ask_for_room_highlight
    - action_set_topic
    - slot{"topic": "highlight"}
    - utter_room_alpha_highlight

## lighting_alpha_from_context
    - slot{"current_room": "Alpha"}
* ask_for_room_lighting
    - action_set_topic
    - slot{"topic": "lighting"}
    - utter_room_alpha_lighting

## atmosphere_alpha_from_context
    - slot{"current_room": "Alpha"}
* ask_for_room_atmosphere
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - utter_room_alpha_atmosphere

## equipment_beta_from_context
    - slot{"current_room": "Beta"}
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_beta_equipment

## seating_beta_from_context
    - slot{"current_room": "Beta"}
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_beta_seating

## price_beta_from_context
    - slot{"current_room": "Beta"}
* ask_for_room_price
    - action_set_topic
    - slot{"topic": "price"}
    - utter_room_beta_price

## size_beta_from_context
    - slot{"current_room": "Beta"}
* ask_for_room_size
    - action_set_topic
    - slot{"topic": "size"}
    - utter_room_beta_people_limit

## highlight_beta_from_context
    - slot{"current_room": "Beta"}
* ask_for_room_highlight
    - action_set_topic
    - slot{"topic": "highlight"}
    - utter_room_beta_highlight

## lighting_beta_from_context
    - slot{"current_room": "Beta"}
* ask_for_room_lighting
    - action_set_topic
    - slot{"topic": "lighting"}
    - utter_room_beta_lighting

## atmosphere_beta_from_context
    - slot{"current_room": "Beta"}
* ask_for_room_atmosphere
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - utter_room_beta_atmosphere

## equipment_gamma_from_context
    - slot{"current_room": "Gamma"}
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_gamma_equipment

## seating_gamma_from_context
    - slot{"current_room": "Gamma"}
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_gamma_seating

## price_gamma_from_context
    - slot{"current_room": "Gamma"}
* ask_for_room_price
    - action_set_topic
    - slot{"topic": "price"}
    - utter_room_gamma_price

## size_gamma_from_context
    - slot{"current_room": "Gamma"}
* ask_for_room_size
    - action_set_topic
    - slot{"topic": "size"}
    - utter_room_gamma_people_limit

## highlight_gamma_from_context
    - slot{"current_room": "Gamma"}
* ask_for_room_highlight
    - action_set_topic
    - slot{"topic": "highlight"}
    - utter_room_gamma_highlight

## lighting_gamma_from_context
    - slot{"current_room": "Gamma"}
* ask_for_room_lighting
    - action_set_topic
    - slot{"topic": "lighting"}
    - utter_room_gamma_lighting

## atmosphere_gamma_from_context
    - slot{"current_room": "Gamma"}
* ask_for_room_atmosphere
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - utter_room_gamma_atmosphere

## equipment_alpha_other
    - slot{"current_room": "Alpha"}
* ask_for_room_equipment{"room": "other"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_equipment
    - utter_room_gamma_equipment

## seating_alpha_other
    - slot{"current_room": "Alpha"}
* ask_for_room_seating{"room": "other"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_seating
    - utter_room_gamma_seating

## price_alpha_other
    - slot{"current_room": "Alpha"}
* ask_for_room_price{"room": "other"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_price
    - utter_room_gamma_price

## size_alpha_other
    - slot{"current_room": "Alpha"}
* ask_for_room_size{"room": "other"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## highlight_alpha_other
    - slot{"current_room": "Alpha"}
* ask_for_room_highlight{"room": "other"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_beta_highlight
    - utter_room_gamma_highlight

## lighting_alpha_other
    - slot{"current_room": "Alpha"}
* ask_for_room_lighting{"room": "other"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_lighting
    - utter_room_gamma_lighting

## atmosphere_alpha_other
    - slot{"current_room": "Alpha"}
* ask_for_room_atmosphere{"room": "other"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_atmosphere
    - utter_room_gamma_atmosphere

## equipment_beta_other
    - slot{"current_room": "Beta"}
* ask_for_room_equipment{"room": "other"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_equipment
    - utter_room_gamma_equipment

## seating_beta_other
    - slot{"current_room": "Beta"}
* ask_for_room_seating{"room": "other"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
    - utter_room_gamma_seating

## price_beta_other
    - slot{"current_room": "Beta"}
* ask_for_room_price{"room": "other"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_gamma_price

## size_beta_other
    - slot{"current_room": "Beta"}
* ask_for_room_size{"room": "other"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## highlight_beta_other
    - slot{"current_room": "Beta"}
* ask_for_room_highlight{"room": "other"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_highlight
    - utter_room_gamma_highlight

## lighting_beta_other
    - slot{"current_room": "Beta"}
* ask_for_room_lighting{"room": "other"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_lighting
    - utter_room_gamma_lighting

## atmosphere_beta_other
    - slot{"current_room": "Beta"}
* ask_for_room_atmosphere{"room": "other"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_atmosphere
    - utter_room_gamma_atmosphere

## equipment_gamma_other
    - slot{"current_room": "Gamma"}
* ask_for_room_equipment{"room": "other"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_equipment
    - utter_room_beta_equipment

## seating_gamma_other
    - slot{"current_room": "Gamma"}
* ask_for_room_seating{"room": "other"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
    - utter_room_beta_seating

## price_gamma_other
    - slot{"current_room": "Gamma"}
* ask_for_room_price{"room": "other"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_beta_price

## size_gamma_other
    - slot{"current_room": "Gamma"}
* ask_for_room_size{"room": "other"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit

## highlight_gamma_other
    - slot{"current_room": "Gamma"}
* ask_for_room_highlight{"room": "other"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_highlight
    - utter_room_beta_highlight

## lighting_gamma_other
    - slot{"current_room": "Gamma"}
* ask_for_room_lighting{"room": "other"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_lighting
    - utter_room_beta_lighting

## atmosphere_gamma_other
    - slot{"current_room": "Gamma"}
* ask_for_room_atmosphere{"room": "other"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "other"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_atmosphere
    - utter_room_beta_atmosphere

## equipment_all
* ask_for_room_equipment{"room": "all"}
    - action_set_topic
    - slot{"topic": "equipment"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment

## seating_all
* ask_for_room_seating{"room": "all"}
    - action_set_topic
    - slot{"topic": "seating"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
    - utter_room_beta_seating
    - utter_room_gamma_seating

## price_all
* ask_for_room_price{"room": "all"}
    - action_set_topic
    - slot{"topic": "price"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price

## size_all
* ask_for_room_size{"room": "all"}
    - action_set_topic
    - slot{"topic": "size"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## highlight_all
* ask_for_room_highlight{"room": "all"}
    - action_set_topic
    - slot{"topic": "highlight"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_highlight
    - utter_room_beta_highlight
    - utter_room_gamma_highlight

## lighting_all
* ask_for_room_lighting{"room": "all"}
    - action_set_topic
    - slot{"topic": "lighting"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_lighting
    - utter_room_beta_lighting
    - utter_room_gamma_lighting

## atmosphere_all
* ask_for_room_atmosphere{"room": "all"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - slot{"room": "all"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_atmosphere
    - utter_room_beta_atmosphere
    - utter_room_gamma_atmosphere

## equipment_alpha_there_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "equipment"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_equipment

## seating_alpha_there_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "seating"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_seating

## price_alpha_there_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "price"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_price

## size_alpha_there_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "size"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_people_limit

## highlight_alpha_there_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "highlight"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_highlight

## lighting_alpha_there_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "lighting"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_lighting

## atmosphere_alpha_there_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_alpha_atmosphere

## equipment_beta_there_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "equipment"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_equipment

## seating_beta_there_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "seating"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_seating

## price_beta_there_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "price"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_price

## size_beta_there_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "size"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_people_limit

## highlight_beta_there_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "highlight"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_highlight

## lighting_beta_there_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "lighting"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_lighting

## atmosphere_beta_there_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Beta"}
    - slot{"room": null}
    - utter_room_beta_atmosphere

## equipment_gamma_there_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "equipment"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_equipment

## seating_gamma_there_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "seating"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_seating

## price_gamma_there_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "price"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_price

## size_gamma_there_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "size"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_people_limit

## highlight_gamma_there_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "highlight"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_highlight

## lighting_gamma_there_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "lighting"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_lighting

## atmosphere_gamma_there_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
* ask_for_room{"room": "there"}
    - slot{"room": "there"}
    - action_correct_room
    - slot{"current_room": "Gamma"}
    - slot{"room": null}
    - utter_room_gamma_atmosphere

## equipment_alpha_others_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "equipment"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_equipment
    - utter_room_gamma_equipment

## seating_alpha_others_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "seating"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_seating
    - utter_room_gamma_seating

## price_alpha_others_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "price"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_price
    - utter_room_gamma_price

## size_alpha_others_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "size"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## highlight_alpha_others_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "highlight"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"current_room": "Alpha"}
    - slot{"room": null}
    - utter_room_beta_highlight
    - utter_room_gamma_highlight

## lighting_alpha_others_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "lighting"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_lighting
    - utter_room_gamma_lighting

## atmosphere_alpha_others_ask_for_room
    - slot{"current_room": "Alpha"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_beta_atmosphere
    - utter_room_gamma_atmosphere

## equipment_beta_others_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "equipment"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_equipment
    - utter_room_gamma_equipment

## seating_beta_others_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "seating"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
    - utter_room_gamma_seating

## price_beta_others_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "price"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_gamma_price

## size_beta_others_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "size"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## highlight_beta_others_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "highlight"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_highlight
    - utter_room_gamma_highlight

## lighting_beta_others_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "lighting"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_lighting
    - utter_room_gamma_lighting

## atmosphere_beta_others_ask_for_room
    - slot{"current_room": "Beta"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_atmosphere
    - utter_room_gamma_atmosphere

## equipment_gamma_others_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "equipment"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_equipment
    - utter_room_beta_equipment

## seating_gamma_others_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "seating"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_seating
    - utter_room_beta_seating

## price_gamma_others_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "price"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_price
    - utter_room_beta_price

## size_gamma_others_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "size"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit

## highlight_gamma_others_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "highlight"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_highlight
    - utter_room_beta_highlight

## lighting_gamma_others_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "lighting"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_lighting
    - utter_room_beta_lighting

## atmosphere_gamma_others_ask_for_room
    - slot{"current_room": "Gamma"}
    - action_set_topic
    - slot{"topic": "atmosphere"}
* ask_for_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - slot{"room": null}
    - utter_room_alpha_atmosphere
    - utter_room_beta_atmosphere

## equipment_none
    - slot{"current_room": null}
* ask_for_room_equipment
    - action_set_topic
    - slot{"topic": "equipment"}
    - utter_room_alpha_equipment
    - utter_room_beta_equipment
    - utter_room_gamma_equipment

## seating_none
    - slot{"current_room": null}
* ask_for_room_seating
    - action_set_topic
    - slot{"topic": "seating"}
    - utter_room_alpha_seating
    - utter_room_beta_seating
    - utter_room_gamma_seating

## price_none
    - slot{"current_room": null}
* ask_for_room_price
    - action_set_topic
    - slot{"topic": "price"}
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price

## size_none
    - slot{"current_room": null}
* ask_for_room_size
    - action_set_topic
    - slot{"topic": "size"}
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## highlight_none
    - slot{"current_room": null}
* ask_for_room_highlight
    - action_set_topic
    - slot{"topic": "highlight"}
    - utter_room_alpha_highlight
    - utter_room_beta_highlight
    - utter_room_gamma_highlight

## lighting_none
    - slot{"current_room": null}
* ask_for_room_lighting
    - action_set_topic
    - slot{"topic": "lighting"}
    - utter_room_alpha_lighting
    - utter_room_beta_lighting
    - utter_room_gamma_lighting

## atmosphere_none
    - slot{"current_room": null}
* ask_for_room_atmosphere
    - action_set_topic
    - slot{"topic": "atmosphere"}
    - utter_room_alpha_atmosphere
    - utter_room_beta_atmosphere
    - utter_room_gamma_atmosphere

## ask_for_room_size 150
* ask_for_room_size{"nr_of_people": "150"}
    - slot{"nr_of_people": "150"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_available_rooms_150_people
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## ask_for_room_size 200
* ask_for_room_size{"nr_of_people": "200"}
    - slot{"nr_of_people": "200"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_available_rooms_200_people
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## ask_for_room_size 270
* ask_for_room_size{"nr_of_people": "270"}
    - slot{"nr_of_people": "270"}
    - action_set_topic
    - slot{"topic": "size"}
    - utter_available_rooms_270_people
    - utter_room_alpha_people_limit

## ask_for_room_price 900
* ask_for_room_price{"budget": "900"}
    - slot{"budget": "900"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_budget_limitation_900
    - utter_room_beta_price

## ask_for_room_price 1100
* ask_for_room_price{"budget": "1100"}
    - slot{"budget": "1100"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_budget_limitation_1100
    - utter_room_beta_price
    - utter_room_gamma_price

## ask_for_room_price 1400
* ask_for_room_price{"budget": "1400"}
    - slot{"budget": "1400"}
    - action_set_topic
    - slot{"topic": "price"}
    - utter_budget_limitation_1400
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price

## provide_budget 900
* provide_budget{"budget": "900"}
    - slot{"budget": "900"}
    - utter_budget_limitation_900

## provide_budget 1100
* provide_budget{"budget": "1100"}
    - slot{"budget": "1100"}
    - utter_budget_limitation_1100

## provide_budget 1400
* provide_budget{"budget": "1400"}
    - slot{"budget": "1400"}
    - utter_budget_limitation_1400

## farewell
* farewell
    - utter_goodbye