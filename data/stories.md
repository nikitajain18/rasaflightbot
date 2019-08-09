## greet path
* greet
  - utter_greet
  - utter_how_help


## cancel path
* cancel
  - utter_cancelled
  - action_deactivate_form
  - action_restart
  - utter_how_help

## aircraft path
* atis_aircraft
  - aircraft_form
  - form{"name":"aircraft_form"}
  - form{"name": null}
  - utter_did_that_help

## aircraft path 2
* atis_aircraft
  - aircraft_form
  - form{"name":"aircraft_form"}
  - form{"name": null}
  - utter_did_that_help
* deny
  - utter_deny
  - action_restart
  - utter_how_help

## flight path deny 
* atis_flight{"fromloc.city_name": "new delhi", "toloc.city_name": "chicago"}
  - slot{"fromloc.city_name": "new delhi"}
  - slot{"toloc.city_name": "chicago"}
  - flight_form
  - form{"name": "flight_form"}
  - slot{"fromloc.city_name": "new delhi"}
  - slot{"toloc.city_name": "chicago"}
  - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
  - slot{"depart_time.period_of_day": "morning"}
  - form: flight_form
  - slot{"depart_time.period_of_day": "morning"}
  - form{"name": null}
  - slot{"requested_slot": null}
  - utter_did_that_help
* deny
  - utter_deny
  - action_restart
  - utter_how_help

## affirm path
* affirm
  - utter_happy

## goodbye path
* goodbye
  - utter_goodbye
  - action_restart

## atis_flight+atis_aircraft path
* atis_flight+atis_aircraft
- flight_form
- form{"name": "flight_form"}
- form{"name": null}
- aircraft_form
- form{"name": "aircraft_form"}
- form{"name": null}
- utter_did_that_help
* affirm
- utter_happy
- action_restart
- utter_how_else_may_help

## above with deny
* atis_flight+atis_aircraft
  - flight_form
  - form{"name": "flight_form"}
  - form{"name": null}
  - aircraft_form
  - form{"name": "aircraft_form"}
  - form{"name": null}
  - utter_did_that_help
* deny
  - utter_deny
  - action_restart
  - utter_how_help

## flight path
* atis_flight
  - flight_form
  - form{"name": "flight_form"}
  - form{"name": null}
  - utter_did_that_help
* affirm
  - utter_happy
  - action_restart

## flight time path
* atis_flight_time
  - action_flight_time
  - utter_did_that_help
 

## full flight path
* atis_flight
  - flight_form
  - form{"name": "flight_form"}
  - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "new york"}
  - slot{"fromloc.city_name": "new york"}
  - flight_form
  - slot{"fromloc.city_name": "new york"}
  - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "chicago"}
  - slot{"toloc.city_name": "chicago"}
  - flight_form
  - slot{"toloc.city_name": "chicago"}
  - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
  - slot{"depart_time.period_of_day": "morning"}
  - flight_form
  - slot{"depart_time.period_of_day": "morning"}
  - form{"name": null}
  - slot{"requested_slot": null}
  - utter_did_that_help
* affirm
    - utter_happy
    - action_restart

## full flight path 2
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
    - form: undo
    - form: flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "new york"}
    - form: flight_form
    - slot{"fromloc.city_name": "new york"}
    - slot{"requested_slot": "toloc.city_name"}
* form: atis_flight{"city_name": "chicago"}
    - form: rewind
* form: inform{"city_name": "chicago"}
    - form: flight_form
    - slot{"toloc.city_name": "chicago"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "morning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* affirm
    - utter_happy
    - action_restart


## full flight path 3
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "new york"}
    - form: flight_form
    - slot{"fromloc.city_name": "new york"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "chicago"}
    - form: flight_form
    - slot{"toloc.city_name": "chicago"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "morning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* affirm
    - utter_happy
    - action_restart


## full flight path 4
* atis_flight
    - flight_form
    - undo
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "new york"}
    - form: flight_form
    - slot{"fromloc.city_name": "new york"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "chicago"}
    - form: flight_form
    - slot{"toloc.city_name": "chicago"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "morning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* affirm
    - utter_happy
    - action_restart


## full flight path 5
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "mumbai"}
    - form: flight_form
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform
    - form: rewind
* form: inform{"city_name": "delhi"}
    - form: flight_form
    - slot{"toloc.city_name": "delhi"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "evening"}
    - slot{"depart_time.period_of_day": "evening"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "evening"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* affirm
    - utter_happy
    - action_restart

## full flight path deny if helped
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "mumbai"}
    - form: flight_form
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform
    - form: rewind
* form: inform{"city_name": "delhi"}
    - form: flight_form
    - slot{"toloc.city_name": "delhi"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "evening"}
    - slot{"depart_time.period_of_day": "evening"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "evening"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* deny
    - utter_deny
    - action_restart

## flight path when 2/3 entities are provided
* atis_flight{"fromloc.city_name": "mumbai", "toloc.city_name": "delhi"}
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"toloc.city_name": "delhi"}
    - flight_form
    - form{"name": "flight_form"}
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"toloc.city_name": "delhi"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "morning"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* affirm
    - utter_happy
    - action_restart

## full flight path denied if helped 2
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform
    - form: rewind
* form: inform{"city_name": "mumbai"}
    - form: flight_form
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "pune"}
    - form: flight_form
    - slot{"toloc.city_name": "pune"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "night"}
    - slot{"depart_time.period_of_day": "night"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "night"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* deny
    - utter_deny
    - action_restart


## full flight path deny if helped 3
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform
    - form: rewind
* form: inform{"city_name": "bombay"}
    - form: flight_form
    - slot{"fromloc.city_name": "bombay"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform
    - form: rewind
* form: inform{"city_name": "new delhi"}
    - form: flight_form
    - slot{"toloc.city_name": "new delhi"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "morning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* deny
    - utter_deny
    - action_restart


## full flight path deny if helped 4
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "mumbai"}
    - form: flight_form
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "pune"}
    - form: flight_form
    - slot{"toloc.city_name": "pune"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "morning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* deny
    - utter_deny
    - action_restart

## cancel
* cancel
  - utter_cancelled
  - action_restart
  - utter_how_help

## flight path with cancel after 1st question
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "mumbai"}
    - form: flight_form
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"requested_slot": "toloc.city_name"}
* cancel
  - action_deactivate_form
  - form{"name": null}
  - utter_cancelled
  - action_restart
  - utter_how_help

## flight path with cancel after 2nd question
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "mumbai"}
    - form: flight_form
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "pune"}
    - form: flight_form
    - slot{"toloc.city_name": "pune"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* cancel
  - action_deactivate_form
  - form{"name": null}
  - utter_cancelled
 - action_restart
 - utter_how_help

## cancel path
* atis_flight
  - flight_form
  - form{"name":"flight_form"}
* cancel
  - action_deactivate_form
  - form{"name": null}
  - utter_cancelled
 - action_restart
 - utter_how_help



## aircraft form
* atis_aircraft
    - aircraft_form
    - form{"name": "aircraft_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "new york"}
    - form: aircraft_form
    - slot{"fromloc.city_name": "new york"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "chicago"}
    - form: aircraft_form
    - slot{"toloc.city_name": "chicago"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* affirm
    - utter_happy
    - action_restart

## affirm
* affirm
    - utter_happy
    - action_restart

## flight path 6
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "mumbai"}
    - form: flight_form
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "new delhi"}
    - form: flight_form
    - slot{"toloc.city_name": "new delhi"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "morning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* deny
  - utter_deny
  - action_restart
  - utter_how_help

## Generated Story -6705403471482867503
* atis_aircraft
    - aircraft_form
    - form{"name": "aircraft_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "pune"}
    - form: aircraft_form
    - slot{"fromloc.city_name": "pune"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "mumbai"}
    - form: aircraft_form
    - slot{"toloc.city_name": "mumbai"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* deny
    - utter_deny
    - action_restart
    - utter_how_help

## aircraft path
* atis_aircraft
  - aircraft_form
  - form{"name":"aircraft_form"}
  - slot{"requested_slot":"fromloc.city_name"}
* form: inform{"city_name":"pune"}
  - form: aircraft_form
  - slot{"fromloc.city_name":"pune"}
  - slot{"requested_slot":"toloc.city_name"}
* cancel
  - utter_cancelled
  - action_deactivate_form
  - form{"name": null}
  - action_restart
  - utter_how_help


## flight and aircraft intent
* atis_airfare
  - airfare_form
  - form{"name":"airfare_form"}
  - slot{"requested_slot":"fromloc.city_name"}
* form: inform{"city_name": "new york"}
  - form: airfare_form
  - slot{"fromloc.city_name": "new york"}
  - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "chicago"}
  - form: airfare_form
  - slot{"toloc.city_name": "chicago"}
  - form{"name": null}
  - slot{"requested_slot": null}
  - utter_how_else_may_help
* atis_flight
  - flight_form
  - form{"name": "flight_form"}
  - form{"name": null}
  - utter_did_that_help
* affirm
  - utter_happy
  - action_restart

## flight and airfare intent 2
* atis_airfare
  - airfare_form
  - form{"name":"airfare_form"}
  - slot{"requested_slot":"fromloc.city_name"}
* form: inform{"city_name": "new york"}
  - form: airfare_form
  - slot{"fromloc.city_name": "new york"}
  - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "chicago"}
  - form: airfare_form
  - slot{"toloc.city_name": "chicago"}
  - form{"name": null}
  - slot{"requested_slot": null}
  - utter_how_else_may_help
* atis_flight
  - flight_form
  - form{"name": "flight_form"}
  - form{"name": null}
  - utter_did_that_help
* deny
  - utter_deny
  - action_restart
  - utter_how_help

## airfare intent 2
* atis_airfare
  - airfare_form
  - form{"name":"airfare_form"}
  - slot{"requested_slot":"fromloc.city_name"}
* form: inform{"city_name": "new york"}
  - form: airfare_form
  - slot{"fromloc.city_name": "new york"}
  - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "chicago"}
  - form: airfare_form
  - slot{"toloc.city_name": "chicago"}
  - form{"name": null}
  - slot{"requested_slot": null}
  - utter_how_else_may_help
* deny
  - utter_happy
  - action_restart

## Generated Story -201348274389789465
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* form: inform{"city_name": "new york"}
    - form: flight_form
    - slot{"fromloc.city_name": "new york"}
    - slot{"requested_slot": "toloc.city_name"}
* atis_aircraft
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - aircraft_form
    - form{"name": "aircraft_form"}
    - slot{"requested_slot":"fromloc.city_name"}
* form: inform{"city_name":"mumbai"}
    - form: aircraft_form
    - slot{"fromloc.city_name": "new york"}
    - slot{"requested_slot": "toloc.city_name"}
* form: inform{"city_name": "chicago"}
    - form: aircraft_form
    - slot{"toloc.city_name": "chicago"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* affirm
    - utter_happy

## Generated Story -841458621813349484
* atis_airfare{"fromloc.city_name": "new delhi", "toloc.city_name": "chicago"}
    - slot{"fromloc.city_name": "new delhi"}
    - slot{"toloc.city_name": "chicago"}
    - airfare_form
    - form{"name": "airfare_form"}
    - slot{"fromloc.city_name": "new delhi"}
    - slot{"toloc.city_name": "chicago"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_how_else_may_help
* atis_flight{"cost_relative": "cheapest"}
    - flight_form
    - form{"name": "flight_form"}
    - slot{"fromloc.city_name": "new delhi"}
    - slot{"toloc.city_name": "chicago"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "morning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* affirm
    - utter_happy
    - action_restart

## Generated Story 5389827213637307035
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "fromloc.city_name"}
* cancel
    - utter_cancelled
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart


## Generated Story 7352010103293613952
* atis_airfare{"fromloc.city_name": "mumbai", "toloc.city_name": "new delhi"}
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"toloc.city_name": "new delhi"}
    - airfare_form
    - form{"name": "airfare_form"}
    - slot{"fromloc.city_name": "mumbai"}
    - slot{"toloc.city_name": "new delhi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_how_else_may_help
* atis_flight
    - flight_form
    - form{"name": "flight_form"}
    - slot{"requested_slot": "depart_time.period_of_day"}
* form: inform{"depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - form: flight_form
    - slot{"depart_time.period_of_day": "morning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* deny
    - utter_deny
    - action_restart
    - utter_how_help

## deny
* deny
  - utter_deny
  - action_restart
  - utter_how_help

## Generated Story 3452066023238760438
* atis_flight{"fromloc.city_name": "Los Angeles", "toloc.city_name": "miami", "depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - slot{"fromloc.city_name": "Los Angeles"}
    - slot{"toloc.city_name": "miami"}
    - flight_form
    - form{"name": "flight_form"}
    - slot{"fromloc.city_name": "Los Angeles"}
    - slot{"toloc.city_name": "miami"}
    - slot{"depart_time.period_of_day": "morning"}
    - slot{"depart_time.period_of_day": "morning"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_did_that_help
* deny
    - utter_deny
    - action_restart

## two intents
