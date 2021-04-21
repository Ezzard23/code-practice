p1 = input("Enter Rock, Paper, or Scissors: ")
p2 = input("Enter Rock, Paper, or Scissors: ")


def rsp(p1,p2,gp = 0):
    p1_win = 0
    p2_win = 0


    
    while p1_win < 4 or p2_win < 4:
		


		if p1 == "Rock" and p2 == "Scissors":
			p1_win +=1
		elif p1 == "Scissors" and p2 == "Paper":
			p1_win += 1 
		elif p1 == "Paper" and p2 == "Rock":
			p1_win += 1
		elif p2 == "Rock" and p1 == "Scissors":
			p1_win +=1
		elif p2 == "Scissors" and p1 == "Paper":
			p1_win += 1 
		elif p2 == "Paper" and p1 == "Rock":
			p1_win += 1

		else:
			print("Draw")

	return p1_win, p2_win

print(rsp(p1,p2))


if __name__ == '__main__':
	main()