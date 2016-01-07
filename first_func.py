from random import randint

def die():
	die_roll = randint(1,6)
	print(die_roll)
	
def custom_die(low, high):
	die_roll = randint(low, high)
	print("Your range was {}, {}".format(str(low), str(high)))
	print(die_roll)


custom_die(1,10)
custom_die(10,100)