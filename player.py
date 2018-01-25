



class Player:

	# Increase health or regen or attack power per progression
	# levels?
	# experience?
	def __init__(self, name, health, attacks):
		self.name = name
		self.HP = health # health points
		self.attack_name = []
		self.AP = [] # attack power
		# self.items = []
		self.regen = 0
		self.armour = 0

		for attack in attacks:
			self.attack_name.append(attack)
			self.AP.append(attacks[attack])

		return

	def Print_Options(self):
		for idx in range(len(self.attack_name)):
			print str(idx) + " : " + self.attack_name[idx] + " (dmg: " + str(self.AP[idx]) + ")."
		return

	def Get_Dmg(self, idx):
		ret_val = None

		if idx >= len(self.AP) or idx < 0:
			print "Input out of range: " + str(idx)
		else:
			ret_val = self.AP[idx]

		return ret_val
