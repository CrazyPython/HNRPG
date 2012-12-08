#! python

PlayerHealth=100
PrinnyHealth=30
runaway = "false"

print "A wild Prinny is licking your face"

while PlayerHealth>0 and PrinnyHealth>0 and runaway == "false":
	print " "
	Action = str(raw_input("Press P to pat, R to run, H to push it away: "))

	if Action == "P":
		print "Prinny licks your face more."
		PlayerHealth = PlayerHealth - 10
		print "Your Health is: " + str(PlayerHealth)
		print "Prinnys Health is: " + str(PrinnyHealth)
	elif Action == "R":
		print "Wimp..."
		runaway = "true"
	elif Action == "H":
		print "You hurt Prinnys feelings"
		PrinnyHealth=PrinnyHealth - 5
		print "Prinnys Health is now: " + str(PrinnyHealth)
		print "Yours is: " + str(PlayerHealth)
	else: print "lets try that again"


