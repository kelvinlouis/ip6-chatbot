## Gamma -> Alpha, Beta
* greet
    - utter_greet+ask_for_name
* provide_name{"name": "John Smith"}
    - utter_ask_for_service_with_name
* ask_for_room_price{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "gamma"}
    - utter_room_gamma_price
* ask_for_alternative_room{"room": "others"}
    - action_correct_room
    - utter_room_alpha_price
    - utter_room_beta_price
* ask_for_room_size{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - utter_room_alpha_people_limit
* ask_for_alternative_room{"room": "others"}
    - action_correct_room
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

## Beta -> Alpha, Gamma
* greet{name: "Arjen Bershka"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_price{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "beta"}
    - utter_room_beta_price
* ask_for_room_size{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "beta"}
    - utter_room_beta_people_limit
* ask_for_alternative_room{"room": "others"}
    - action_correct_room
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## Alpha -> Beta, Gamma 
* greet
    - utter_greet+ask_for_name
* provide_name{"name": "Laura"}
    - utter_ask_for_service_with_name
* ask_for_room_size{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - utter_room_alpha_people_limit
* ask_for_alternative_room{"room": "other rooms"}
    - action_correct_room
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_price{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "beta"}
    - utter_room_beta_price
* ask_for_alternative_room{"room": "others"}
    - action_correct_room
    - utter_room_alpha_price
    - utter_room_gamma_price

## First -> Beta, Gamma
* greet{"name": "Laura Steiner", "company": "Inselspital"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_price{"room": "first"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - utter_room_alpha_price
* ask_for_room_price{"room": "second"}
    - action_correct_room
    - slot{"current_room": "beta"}
    - utter_room_beta_price
* ask_for_alternative_room{"room": "others"}
    - action_correct_room
    - utter_room_alpha_price
    - utter_room_gamma_price


## Second -> Alpha, Gamma
* greet{name: "Blerim Dzemili"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_size{"room": "second"}
    - action_correct_room
    - slot{"current_room": "beta"}
    - utter_room_beta_people_limit
* ask_for_alternative_room{"room": "others"}
    - action_correct_room
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## Third -> Alpha, Beta
* greet
    - utter_greet+ask_for_name
* provide_name{"name": "John"}
    - utter_ask_for_service_with_name
* ask_for_room_price{"room": "third"}
    - action_correct_room
    - slot{"current_room": "gamma"}
    - utter_room_gamma_price
* ask_for_alternative_room{"room": "others"}
    - action_correct_room
    - utter_room_alpha_price
    - utter_room_beta_price
* ask_for_room_size{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - utter_room_alpha_people_limit
* ask_for_room_size{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "beta"}
    - utter_room_beta_people_limit
* ask_for_alternative_room{"room": "others"}
    - action_correct_room
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## All
* greet
    - utter_greet+ask_for_name
* provide_name{"name": "Luca"}
    - utter_ask_for_service_with_name
* ask_for_room_price
    - action_correct_room
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_size
    - action_correct_room
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit
* ask_for_room_size{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - utter_room_alpha_people_limit
* ask_for_room_size{"room": "beta"}
    - action_correct_room
    - slot{"current_room": "beta"}
    - utter_room_beta_people_limit
* ask_for_alternative_room{"room": "others"}
    - action_correct_room
    - utter_room_alpha_people_limit
    - utter_room_gamma_people_limit

## Generated Story -1247501406053206060
* greet{"name": "Nicola"}
    - slot{"name": "Nicola"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_price
    - action_correct_room
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_size{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "gamma"}
    - utter_room_gamma_people_limit
* ask_for_alternative_room{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - utter_room_alpha_people_limit

## Generated Story -4014373213632055186
* provide_name{"name": "Kelvin"}
    - slot{"name": "Kelvin"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_size{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - utter_room_alpha_people_limit
* ask_for_room_price{"room": "alpha"}
    - slot{"room": "alpha"}
    - action_correct_room
    - slot{"current_room": "alpha"}
    - utter_room_alpha_price
* ask_for_room_price{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_size{"room": "gamma"}
    - slot{"room": "gamma"}
    - action_correct_room
    - slot{"current_room": "gamma"}
    - utter_room_gamma_people_limit
* ask_for_room_size{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit

## Generated Story 1215541522732552574
* greet{"name": "Kelvin"}
    - slot{"name": "Kelvin"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_price{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_correct_room
    - utter_room_alpha_price
* ask_for_alternative_room{"room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - utter_room_beta_price
* ask_for_room_size{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_correct_room
    - utter_room_gamma_people_limit
* ask_for_alternative_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
* ask_for_room_price{"room": "Beta"}
    - slot{"room": "Beta"}
    - action_correct_room
    - utter_room_beta_price
* ask_for_alternative_room{"room": "others"}
    - slot{"room": "others"}
    - action_correct_room
    - utter_room_alpha_price
    - utter_room_gamma_price

## Generated Story 6331088323140750359
* greet{"name": "Nicola Cocquio"}
    - slot{"name": "Nicola Cocquio"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_price
    - action_correct_room
    - utter_room_alpha_price
    - utter_room_beta_price
    - utter_room_gamma_price
* ask_for_room_size
    - action_correct_room
    - utter_room_alpha_people_limit
    - utter_room_beta_people_limit
    - utter_room_gamma_people_limit

