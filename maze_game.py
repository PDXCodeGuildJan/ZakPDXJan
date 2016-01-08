path = []
# function that uses empty list above to record steps taken in maze
# and returns a indexed list of the steps taken when maze is finished
def path_taken(room):
	path.append(room)
	if room == "finish":
		for index, item in enumerate(path):
			print("Step :{}, {}".format(index+1, item))

def room0():
	path_taken("room 0")
	print("\nYou're currently in room 0 you can go [N]orth or [E]ast.")
	choice = input("Please type N or E to pick a direction to travel in: ").upper()
	if choice == "N": 
		return room2
	elif choice == "E":
		return room1
	elif choice == "Q":
		exit()	
	else: 
		print("-"*60)
		print("Invalid direction")
		return room0

def room1():
	path_taken("room 1")
	print("\nYou're now in room 1 and have hit a dead end!")
	choice = input("Pick a direction you can only go [W]est:  ").upper()
	if choice == "W":
		return room0
	elif choice == "Q":
		exit()
	else:
		print("-"*60) 
		print("Stop hitting your head against the wall! pick W!")
		return room1

def room2():
	path_taken("room 2")
	print("\nYou're now in room 2 you can go [N]orth or [S]outh.")
	choice = input("Pick a direction you can go N or S: ").upper()
	if choice == "N":
		return room3
	elif choice == "S":
		return room0
	elif choice == "Q":
		exit()
	else: 
		print("-"*60)
		print("Please pick a valid direction!")
		return room2

def room3():
	path_taken("room 3")
	print("\nYou're now in room 3 you can go [S]outh or [E]ast.")
	choice = input("Pick a direction you can go S or E: ").upper()
	if choice == "S":
		return room2
	elif choice == "E":
		return finish
	elif choice == "Q":
		exit()
	else: 
		print("-"*60)
		print("Please pick a valid direction")
		return room3

def finish():
	path_taken("Finish")
	print("You've finished the maze!")

def main():
	print("-" * 60)
	print("\nWelcome to the maze. You may use N, S, E, W to move around.")
	print("If you want to quit at anytime press Q")
	current_room = room0

	while current_room != finish:
		new_room = current_room()
		current_room = new_room

	print("-"*60)	
	print("\nYou've finished the maze!\n")
	print("Below is the path you took.")
	path_taken("finish")	



main()