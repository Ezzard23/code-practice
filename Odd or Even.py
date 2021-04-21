num = int(input("Enter Number: "))
check = int(input("Enter Number: "))

def even_odd(num,check):
    if num % check == 0:
        return f"{check} divides evenly into {num}"
    elif num % 4 == 0:
        return "This number is divisible by 4"
    if num % 2 == 0:
        return "This number is even"
    if num % 2 != 0:
        return " This number is odd"

print(even_odd(num,check))