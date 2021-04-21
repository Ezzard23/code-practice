
birthdays = {"Chris Ezzard": "02/23/1996", "Justin Henderson": "12/09/1996", "Jacoby Allen": "10/29/1996", "Ropafadzo Moyo": "04/10/1998"}
print("Welcome to the Birthday dictionary. We know the birthdays of:\n Chris Ezzard\n Jacoby Allen \n Justin Henderson \n Ropafadzo Moyo\n")


name = str(input("Who's birthday would you like to look up?"))


def get_birthday(name):
	if name in birthdays:
		return f"{name} birthday is {birthdays[name]}"
    
print(get_birthday(name))