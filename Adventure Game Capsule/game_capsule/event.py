# Class Attributes:
#	[Variable Name] = [Type] | [Description]
#	event_name = string | Name of event
#	event_situation = string | Description of event
#	transitions = list (string) | Names of transition events
#	transitions_text = list (string) | Description of action that leads to transition event
#
class Event:
	def __init__(self, name, situation, options):
		self.event_name = name
		self.event_situation = situation
		self.transitions = [] # name of next event
		self.transitions_text = [] # description of next event

		# Retrieve event names
		for event in options:
			self.transitions.append(event)
			self.transitions_text.append(options[event])

		return

	# Provide player options
	def Print_Options(self):
		for idx in range(len(self.transitions_text)):
			print str(idx) + " : " + self.transitions_text[idx]
		return

	# Get the next event selected
	# Input: 	player_input - string | raw input from user
	#
	# Return: 	Empty String - string | invalid input
	#				Event Name - string | valid transition index
	def Get_Next_Event(self, idx):
		ret_val = ""

		if idx >= len(self.transitions) or idx < 0:
			print "Input out of range: " + str(idx)
		else:
			ret_val = self.transitions[idx]

		return ret_val

