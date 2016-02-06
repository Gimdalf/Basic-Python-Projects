Board = ["0 ","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 "]
print "   %s   |   %s   |   %s   \n ----------------------- \n   %s   |   %s   |   %s   \n ----------------------- \n   %s   |   %s   |   %s    "%(Board[0], Board[1], Board[2], Board[3], Board[4], Board[5], Board[6], Board[7], Board[8])

for x in range (0,9):
	if x in [0,2,4,6,8]:
		player = "X"
		choice = raw_input("X, choose your place:")
		while Board[int(choice)] == "X" or Board[int(choice)] == "Q":
			print "Invalid Location"
			choice = raw_input("X, choose your place:")
		replace = int(choice)
		del Board[replace]
		Board.insert (replace,"X ")
		print "   %s   |   %s   |   %s   \n ----------------------- \n   %s   |   %s   |   %s   \n ----------------------- \n   %s   |   %s   |   %s    "%(Board[0], Board[1], Board[2], Board[3], Board[4], Board[5], Board[6], Board[7], Board[8])
		if str(Board[0]) + str(Board[1]) + str(Board[2]) == "X X X ":
			print "X has won!"
			break
		elif str(Board[3]) + str(Board[4]) + str(Board[5]) == "X X X ":
			print "X has won!"
			break
		elif str(Board[6]) + str(Board[7]) + str(Board[8]) == "X X X ":
			print "X has won!"
			break
		elif str(Board[0]) + str(Board[3]) + str(Board[6])  == "X X X ":
			print "X has won!"
			break
		elif str(Board[1]) + str(Board[4]) + str(Board[7])  == "X X X ":
			print "X has won!"
			break
		elif str(Board[2]) + str(Board[5]) + str(Board[8]) == "X X X ":
			print "X has won!"
			break
		elif str(Board[0]) + str(Board[4]) + str(Board[8]) == "X X X ": 
			print "X has won!"
			break
		elif str(Board[2]) + str(Board[4]) + str(Board[6]) == "X X X ":
			print "X has won!"
			break
#Q side
	else:
		player = "Q"
		choice = raw_input("Q, choose your place:")
		while Board[int(choice)] == "X" or Board[int(choice)] == "Q":
			print "Invalid Location"
			choice = raw_input("Q, choose your place:")
		replace = int(choice)
		del Board[replace]
		Board.insert (replace,"Q ")
		print "   %s   |   %s   |   %s   \n ----------------------- \n   %s   |   %s   |   %s   \n ----------------------- \n   %s   |   %s   |   %s    "%(Board[0], Board[1], Board[2], Board[3], Board[4], Board[5], Board[6], Board[7], Board[8])
		if str(Board[0]) + str(Board[1]) + str(Board[2]) == "Q Q Q ":
			print "Q has won!"
			break
		elif str(Board[3]) + str(Board[4]) + str(Board[5]) == "Q Q Q ":
			print "Q has won!"
			break
		elif str(Board[6]) + str(Board[7]) + str(Board[8]) == "Q Q Q ":
			print "Q has won!"
			break
		elif str(Board[0]) + str(Board[3]) + str(Board[6])  == "Q Q Q ":
			print "Q has won!"
			break
		elif str(Board[1]) + str(Board[4]) + str(Board[7])  == "Q Q Q ":
			print "Q has won!"
			break
		elif str(Board[2]) + str(Board[5]) + str(Board[8]) == "Q Q Q ":
			print "Q has won!"
			break
		elif str(Board[0]) + str(Board[4]) + str(Board[8]) == "Q Q Q ": 
			print "Q has won!"
			break
		elif str(Board[2]) + str(Board[4]) + str(Board[6]) == "Q Q Q ":
			print "Q has won!"
			break
