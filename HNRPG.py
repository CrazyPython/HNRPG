#! python
""" This is the very first Alpha Build of Halo Night RPG, this program should never see the day of light, but if it does and you want a real description email me at notna888@gmail.com thanks.
"""
from player import *
characterselected = "false"
#When player data is updated, we use Anton = Player(Anton_data) for anton
while characterselected == "false":
	print "Welcome, please select your character"
	print "1 Anton the Linux User"
	print "2 Daniel the Drunk"
	print "3 Harry the Indian"
	print "4 Jack the Ginger"
	print "5 Jayden the Wise"
	print "6 Shaun the Fucking Pony Faggot"
	print "7 Warwick the Filthy Casual"
	try:
		CharacterIndex = int(raw_input("Please enter the integer: "))
	except ValueError:
		print"Sigh, not an integer"
		continue #next loop
	if CharacterIndex == 1:
		print "May Tux be with you."
		characterselected = "true"
		break
	elif CharacterIndex == 2:
		print "Witty Acceptance Message Here"
		characterselected = "true"
		break
	elif CharacterIndex == 3:
		print "There'll be curry when you get back"
		characterselected = "true"
		break
	elif CharacterIndex == 4:
		print "Now go get a soul"
		characterselected = "true"
		break
	elif CharacterIndex == 5:
		print "Mayeth your adventure be exquisite"
		characterselected = "true"
		break
	elif CharacterIndex == 6:
		print "You may even find Luna"
		characterselected = "true"
		break
	elif CharacterIndex == 7:
		print "Don't tap out!"
		characterselected = "true"
		break
	else: print "sigh, try again"

print "\n \n It was a plain and simple Saturday night in the man cave with a few good gamer mates, when Anton found a small free multiplayer indie cross platform action rpg puzzel fps with an live rts element to assist other players against a perfectly weighted dynamic 1st/3rd person adventure game."
