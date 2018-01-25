import json

class Properties:
	def __init__(self):
		self.game_name = ""
		self.start_event = ""
		self.combat = 0
		self.item = 0
		self.environment = 0
		self.chance = 0
		return

	def Load_Values(self, property_files):
		with open(property_files) as f:
			values = json.load(f)

		# save boolean values into the class
		self.game_name = values["game_name"]
		self.start_event = values["start_event"]
		self.combat = values["combat"]
		self.item = values["item"]
		self.environment = values["environment"]
		self.chance = values["chance"]

