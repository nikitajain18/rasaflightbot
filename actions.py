# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_sdk import Tracker
from rasa_core_sdk import Action
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core.events import AllSlotsReset
from rasa_core.events import Restarted

# from rasa_sdk.executor import CollectingDispatcher

import pyodbc 


class FlightForm(FormAction):

	def name(self):
		return "flight_form"

	@staticmethod
	def required_slots(tracker) -> List[Text]:
		return ["fromloc.city_name","toloc.city_name","depart_time.period_of_day"]

	# def submit(self, dispatcher, tracker, domain):
	# 	dispatcher.utter_message("flight form successfully filled")
	# 	return []

	def submit(self, dispatcher, tracker, domain):
		conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=BCDEWSDT004;'
                      'Database=chatbot;'
                      'UID=sa;'
                      'PWD=Welcome@123;')

		origin = tracker.get_slot('fromloc.city_name')
		destination = tracker.get_slot('toloc.city_name')

		cursor = conn.cursor()
		msg = '''select FLIGHT_NUMBER, AIRLINE, PRICE from FlightData where ORIGIN_CITY=? and DESTINATION_CITY=?'''
		cursor.execute(msg,(origin, destination))
		count = str(cursor.rowcount)
		intCount = int(count)
		dispatcher.utter_message("Flight Number" + "     " + "Airline" + "     " + "Price")
		if intCount == 0:
			dispatcher.utter_message("There are no flights scheduled between those cities")
		# if cursor.rowcount < 1:
		# 	dispatcher.utter_message("There are no flights scheduled between those cities")
		for row in cursor:
			dispatcher.utter_message(str(row.FLIGHT_NUMBER) + " " + row.AIRLINE + " " + str(row.PRICE))

		return []
	
	def slot_mappings(self):
		return {
		"toloc.city_name": self.from_entity(entity="city_name", intent="inform"),
		"fromloc.city_name": self.from_entity(entity="city_name", intent="inform")
		}


class AircraftForm(FormAction):

	def name(self):
		return "aircraft_form"

	@staticmethod
	def required_slots(tracker) -> List[Text]:
		return ["fromloc.city_name","toloc.city_name", ]

	def submit(self, dispatcher, tracker, domain):
		conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=BCDEWSDT004;'
                      'Database=chatbot;'
                      'UID=sa;'
                      'PWD=Welcome@123;')

		origin = tracker.get_slot('fromloc.city_name')
		destination = tracker.get_slot('toloc.city_name')

		cursor = conn.cursor()
		msg = '''select AIRLINE_CODE,FLIGHT_NUMBER,AIRLINE from FlightData where ORIGIN_CITY=? AND DESTINATION_CITY=?'''
		cursor.execute(msg,(origin, destination))
		count = str(cursor.rowcount)
		intCount = int(count)
		dispatcher.utter_message("Airline Code" + "     " + "Flight Number" + "     " + "Airline")
		if intCount == 0:
			dispatcher.utter_message("There are no flights scheduled between those cities")
		# if cursor.rowcount < 1:
		# 	dispatcher.utter_message("There are no flights scheduled between those cities")
		for row in cursor:
			dispatcher.utter_message(str(row.AIRLINE_CODE) + " " + str(row.FLIGHT_NUMBER) + " " + str(row.AIRLINE))

		return []

	def slot_mappings(self):
		return {
		"toloc.city_name": self.from_entity(entity="city_name", intent="inform"),
		"fromloc.city_name": self.from_entity(entity="city_name", intent="inform")
		}


class AirfareForm(FormAction):

	def name(self):
		return "airfare_form"

	@staticmethod
	def required_slots(tracker) -> List[Text]:
		return ["fromloc.city_name","toloc.city_name", ]

	def submit(self, dispatcher, tracker, domain):
		conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=BCDEWSDT004;'
                      'Database=chatbot;'
                      'UID=sa;'
                      'PWD=Welcome@123;')

		origin = tracker.get_slot('fromloc.city_name')
		destination = tracker.get_slot('toloc.city_name')

		cursor = conn.cursor()
		msg = '''select AIRLINE, PRICE from FlightData where ORIGIN_CITY=? and DESTINATION_CITY=?'''
		cursor.execute(msg,(origin, destination))
		count = str(cursor.rowcount)
		intCount = int(count)
		dispatcher.utter_message("Airline" + "     " + "Price")
		if intCount == 0:
			dispatcher.utter_message("There are no flights scheduled between those cities")
		# if cursor.rowcount < 1:
		# 	dispatcher.utter_message("There are no flights scheduled between those cities")
		for row in cursor:
			dispatcher.utter_message(row.AIRLINE + " " + str(row.PRICE))

		return []

	def slot_mappings(self):
		return {
		"toloc.city_name": self.from_entity(entity="city_name", intent="inform"),
		"fromloc.city_name": self.from_entity(entity="city_name", intent="inform")
		}


# class ActionAirfare(Action):

# 	def name(self):
# 		return "action_airfare"

# 	def run(self, dispatcher, tracker, domain):
# 		dispatcher.utter_message("Intent: atif_airfare")
# 		return []

# class ActionFlight(Action):

# 	def name(self):
# 		return "action_flight"

# 	def run(self, dispatcher, tracker, domain):
# 		dispatcher.utter_message("Intent: atif_flight")
# 		return []

class ActionFlightTime(Action):

	def name(self):
		return "action_flight_time"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("Intent: atif_flight_time")
		return []

# class ActionCancel(Action):

# 	def name(self):
# 		return "action_cancel"

# 	def run(self, dispatcher, tracker, domain):
# 		dispatcher.utter_message("Cancelled")
# 		return [self.deactivate()]

class ActionRestarted(Action): 	
	def name(self): 		
		return 'action_restarted' 	
	def run(self, dispatcher, tracker, domain): 
		return[Restarted()]

class ActionSlotReset(Action): 	
	def name(self): 		
		return 'action_slot_reset' 	
	def run(self, dispatcher, tracker, domain): 		
		return[AllSlotsReset()]