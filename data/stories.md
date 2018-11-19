## Gamma -> Alpha, Beta
* greet
    - utter_greet+ask_for_name
* provide_name{"name": "John Smith"}
    - utter_ask_for_service_with_name
* ask_for_room_price{"room": "Gamma"}
    - action_get_room_price
    - slot{"current_room": "Gamma"}
* ask_for_alternative_room{"room": "others"}
    - action_get_room_price
* ask_for_room_size{"room": "Alpha"}
    - action_get_room_size
    - slot{"current_room": "Alpha"}
* ask_for_alternative_room{"room": "others"}
    - action_get_room_size

## Beta -> Alpha, Gamma
* greet{name: "Arjen Bershka"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_price{"room": "Beta"}
    - action_get_room_price
    - slot{"current_room": "Beta"}
* ask_for_room_size{"room": "Beta"}
    - action_get_room_size
    - slot{"current_room": "Beta"}
* ask_for_alternative_room{"room": "others"}
    - action_get_room_size

## Alpha -> Beta, Gamma 
* greet
    - utter_greet+ask_for_name
* provide_name{"name": "Laura"}
    - utter_ask_for_service_with_name
* ask_for_room_size{"room": "Alpha"}
    - action_get_room_size
    - slot{"current_room": "Alpha"}
* ask_for_alternative_room{"room": "others"}
    - action_get_room_size
* ask_for_room_price{"room": "Beta"}
    - action_get_room_price
    - slot{"current_room": "Beta"}
* ask_for_alternative_room{"room": "others"}
    - action_get_room_price

## First -> Beta, Gamma
* greet{"name": "Laura Steiner", "company": "Inselspital"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_price{"room": "first"}
    - action_get_room_price
    - slot{"current_room": "Alpha"}
* ask_for_room_price{"room": "second"}
    - action_get_room_price
    - slot{"current_room": "Beta"}
* ask_for_alternative_room{"room": "others"}
    - action_get_room_price


## Second -> Alpha, Gamma
* greet{name: "Blerim Dzemili"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_size{"room": "second"}
    - action_get_room_size
    - slot{"current_room": "Beta"}
* ask_for_alternative_room{"room": "others"}
    - action_get_room_size

## Third -> Alpha, Beta
* greet
    - utter_greet+ask_for_name
* provide_name{"name": "John"}
    - utter_ask_for_service_with_name
* ask_for_room_price{"room": "third"}
    - action_get_room_price
    - slot{"current_room": "Gamma"}
* ask_for_alternative_room{"room": "others"}
    - action_get_room_price
* ask_for_room_size{"room": "Alpha"}
    - action_get_room_size
    - slot{"current_room": "Alpha"}
* ask_for_room_size{"room": "Beta"}
    - action_get_room_size
    - slot{"current_room": "Beta"}
* ask_for_alternative_room{"room": "others"}
    - action_get_room_size

## Generated Story -1247501406053206060
* greet{"name": "Nicola"}
    - slot{"name": "Nicola"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_price
    - action_get_room_price
* ask_for_room_size{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_get_room_size
    - slot{"current_room": "Gamma"}
* ask_for_alternative_room{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_get_room_size
    - slot{"current_room": "Alpha"}

## Generated Story -4014373213632055186
* provide_name{"name": "Kelvin"}
    - slot{"name": "Kelvin"}
    - utter_greet_with_name+ask_for_service
* ask_for_room_size{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_get_room_size
    - slot{"current_room": "Alpha"}
* ask_for_room_price{"room": "Alpha"}
    - slot{"room": "Alpha"}
    - action_get_room_price
    - slot{"current_room": "Alpha"}
* ask_for_room_price{"room": "others"}
    - slot{"room": "others"}
    - action_get_room_price
* ask_for_room_size{"room": "Gamma"}
    - slot{"room": "Gamma"}
    - action_get_room_size
    - slot{"current_room": "Gamma"}
* ask_for_room_size{"room": "others"}
    - slot{"room": "others"}
    - action_get_room_size