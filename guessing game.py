import random as rd
num = rd.randint(1,10)
guess = 0

while guess != int and guess != "exit":
    guess = input("Enter your numerical guess: ")
    if guess == "exit":
        break
    
    guess = (int(guess))
    
    if num == guess:
        print( "Your guess was correct")
    elif num > guess:
        print("Your guess was too low")
    elif num < guess:
        print ("Your guess was too high")

