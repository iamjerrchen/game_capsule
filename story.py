from sys import exit
from properties import Properties
from event import Event
import json

# Class Attributes:
#	[Variable Name] = [Type] | [Description]
#	start_event = string | Name of the first event
#	story_content = dictionary (varies) | Imported content from a json file
#	event_selector = dictionary | (key) event name, (value) Event object
#	game_name = string | Name of story/adventure/game
#
class Story:

	def __init__(self, property_file):
		self.filename = None
		self.properties = Properties()
		self.properties.Load_Values(property_file)
		return

	# Ensures each event's transitions are valid (existence) events
	def Verify_Transitions(self):
		bad_transitions = 0

		# Verify existence of start event
		if self.start_event not in self.event_selector:
			bad_transitions += 1
			print "Missing start event: " + self.start_event

		# Verify existence of all transitions as events
		for event_name in self.event_selector:
			for transition_names in (self.event_selector[event_name]).transitions:
				if transition_names not in self.event_selector:
					bad_transitions += 1
					print "Event '" + event_name + "' contains nonexistent event transition: '" + transition_names + "'"

		if bad_transitions > 0:
			exit("Add as valid event or fix transition.")

		return

	# Create the representation of the story
	def Load_Story(self, filename):
		self.filename = filename

		# Read from formatted File
		if filename.endswith(".json"):
			self.Interpret_Json(filename)
		else:
			file_type = filename.split('.')
			exit("." + file_type[len(file_type)-1] + " is not a support file type.\nPlease use .json file types.")

		# initialize variables
		self.event_selector = {}
		self.game_name = self.story_content["game_name"]
		self.start_event = self.story_content["start_event"]

		# Populate the event selector
		json_events = self.story_content["events"]
		for name in json_events:
			# Duplicate event names will overwrite older events
			self.event_selector[str(name)] = Event(str(name), json_events[name]["situation"], json_events[name]["options"])

		self.Verify_Transitions()
		return

	# Json Format
	def Interpret_Json(self, filename):
		with open(filename) as f:
			self.story_content = json.load(f)
		return

	# Save content into json format
	def Save_Game(self):
		if filename == None:
			return
		# TODO
		else:
			pass
		return


