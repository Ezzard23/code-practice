import random as rd 

randnum = rd.randint(1000,9999)

num = list(map(int,str(randnum))) #splitting integer into list to iterate


def cows_bulls(x,y):
    cows = 0
    bulls = 0
    while cows < 4:
        for i,j in zip(num, guess): #use zip to compare 2 list 
    # List comprehension version [i for i, j in zip(a, b) if i == j]
    		if i == j:
       			cows += 1
    		else:
        		bulls +=1

    return cows,bulls






if __name__ = "__main__":
	user_num = input("Give me a number: ")
	print(cows_bulls(num))