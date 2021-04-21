name,age = input("Enter your name: "),int(input("Enter you age: "))

def old_age(name,age):
	nage = (100 - age) + 2020
    
    return f"Hello, {name} you will turn 100 in the year {nage}"

print(old_age(name, age))
