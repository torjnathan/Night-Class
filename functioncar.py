def car(want_a_car, color, doors, cost):
	if want_a_car.lower() == "yes":
		print "Great!"
		print "You want a %s car. We can do that!" % color
		print "you want %s doors. I guess that's alright." % doors
		if int(cost) < 5000:
			print "You are way too cheap! Bye"
			print "Sold!"
		else:
			print "okay fine"

want_a_car = raw_input("Do you want a new car?: ")
color = raw_input("What color do you want?: ")
doors = raw_input("How many doors do you want?: ")
cost = raw_input("How much are you willing to pay?: ")
