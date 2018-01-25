

# Combat Mode: will be standalone from the story meaning it will "pause"
#	the story and focus on the combat until it's over.
#
#
#
#
class Combat:

	def __init__(self):
		# TODO: initialize with environment effects?
		# 			random turn
		# 			rule breakers
		return

	def Battle(self, player, monster):
		print "Initiating Combat Mode. Engaging " + monster.name + ".\n"

		# TODO: make it interesting and random number generator turn 1-2
		turn = 0

		# make a copy of the health to maintain monster obj
		self.monster_health = monster.HP 

		while(1):
			if monster_health <= 0:
				print "Victory: " + player.name + " has defeated the " + monster.name + ".\n"
				break

			if player.HP <= 0:
				exit("Defeat: " + player.name + " has been slain by the " + monster.name) + ".\n"

			# print current state details
			print "Stats:"
			print player.name + " HP: " + str(player.HP)
			print monster.name + " HP: " + str(monster_health) + "\n"

			if turn%2 == 0:
				# player's turn
				player.Print_Options()
				while(1):
					player_input = raw_input("\nSelect Attack: ")
					idx = Verify_Int(player_input)
					if idx >= 0:
						dmg = player.Get_Dmg(idx)
						if dmg != None:
							monster_health -= dmg
							# interface the game
							print player.name + " used " + player.attack_name[idx] + "."
							print monster.name + " has " + str(monster_health) + " HP remaining.\n"
							break
			else:
				# monster's turn
				# TODO: incorporate use of different attacks
				idx = 0
				dmg = monster.AP[idx]
				player.HP -= dmg
				print monster.name + " used " + monster.attack_name[idx] + "."
				print player.name + " has " + str(player.HP) + " HP remaining.\n"

			turn += 1

		return



