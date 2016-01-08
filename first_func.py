from random import randint

# rolls d6 
def die():
	print(randint(1,6))

# rolls custom die 
def custom_die(low, high):
	output = randint(low, high)
	if output == high: 
		print("{} Critical hit".format(output))
	elif output == low: 
		print("{} Critical miss".format(output))
	else: 
		print(output)	

def main():
	print("Welcome to the die roller! Enter [Q] to quit. ")

	entree = ""

	while entree != "q": 
		# Ask user how many dice to rool 
		entree = input("How many dice? ")
		if entree == 'q':
			exit()
		total_rolls = int(entree)

		entree = input("How many sides does the die have? ")
		if entree == 'q':
			exit()
		total_sides = int(entree)

		# Roll that many die 
		for item in range(total_rolls):
			custom_die(1, total_sides)			 

		# Deciding whether or not to run the program again 	
		# continue_question = input("Would you like to roll again? [Y/N] ").lower()
		# if continue_question == "y":
		# 	continue
		# elif continue_question == "n":
		# 	break
		# else: 
		# 	print("Please type a valid Y or N after next roll")
		# 	continue

main()


