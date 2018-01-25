from story import Story

# temporary import
# from player import Player
# from monster import Monster

from sys import argv
from sys import exit

def Verify_Int(player_input):
	ret_val = -1

	try:
		# try to convert to int
		ret_val = int(player_input)
	except:
		print "Bad Input: " + player_input

	return ret_val


# Execution of the game
def Play(Adventure):
	print "Playing: " + Adventure.game_name

	curr_event_name = Adventure.start_event
	curr_event = Adventure.event_selector[curr_event_name]

	# encounter = Combat()
	# minion = Monster("Umang", 40, {"stare": 2})
	# you = Player("Jerry", 30, {"swipe": 4, "kick": 5, "name call": 2})

	while(1):
		print "Event: " + curr_event.event_name + "\n"
		
		# temporary test, will need to make a hard copy
		# m = minion
		# encounter.Battle(you, m)
		# end temporary test

		print curr_event.event_situation + "\n"
		
		if len(curr_event.transitions) == 0:
			break

		curr_event.Print_Options()

		# Loop til valid input
		while(1):
			player_input = raw_input("\nEnter Option: ")
			idx = Verify_Int(player_input)
			if idx >= 0:
				curr_event_name = curr_event.Get_Next_Event(idx)
				if len(curr_event_name) > 0: # valid room
					break

		curr_event = Adventure.event_selector[curr_event_name]

	return


def main():
	if len(argv) != 3:
		exit("Not enough arguments.")

	story_file = argv[1]
	property_file = argv[2]

	game = Story(property_file)
	game.Load_Story(story_file)
	Play(game)

	return

if __name__ == '__main__':
	main()
