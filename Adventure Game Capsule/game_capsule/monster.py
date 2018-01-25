



# Monsters: This class will act in the same manner as events.
# Class Attributes:
#	[Variable Name] = [Type] | [Description]
#	name = string | Name of monster
#	HP = float | hitpoints
#	attack_name = list (string) | names of individual attacks
#	AP = list [float] | attack power of each corresponding attack
#
class Monster:

	def __init__(self, name, health, attacks):
		self.name = name
		self.HP = health # health points
		self.attack_name = []
		self.AP = [] # attack power

		for attack in attacks:
			self.attack_name.append(attack)
			self.AP.append(attacks[attack])

		return
