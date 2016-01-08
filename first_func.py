from random import randint

# rolls d6 
def die():
	print(randint(1,6))

# rolls custom die 
def custom_die(low, high):
	print("Your range was {}, {}".format(str(low), str(high)))
	print(randint(low, high))

def main():
	# Ask user how many dice to rool 
	total_rolls = int(input("How many dice? "))
	total_sides = int(input("How many sides does the die have? "))

	# Roll that many die 
	for item in range(total_rolls):
		custom_die(1, total_sides)

main()


