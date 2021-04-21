# control flow
from random import shuffle



a = 45
if a > 23:
	print("Yes")
else:
	print("No")


loc = 'store'

if loc == 'Auto Shop':
    print("cars are cool")
elif loc == 'Bank':
    print("Money is cool")
elif loc == 'Store':
    print("Welcome to the store")
else:
    print("I'm cool")
    
#For Loop
my_list = [1,2,3,4,5,6]

for n in my_list:
    if n % 2 == 0:
        print(f'This is an even number : {n}')
    else:
        print(f'This is an odd number: {n}')

list_sum = 0
for n in my_list:
    list_sum = list_sum + n

print(list_sum)

list2 = [(1,3),(2,5),(3,5),(9,8)]

for (a,b) in list2:
    print(a)
    print(b)
    
# while loops

x = 0 

while x < 5: 
    print(34 * x)
    
    x +=1
else:
    print("not under 5")
    

for a in enumerate(list2):
    print (a)
    
    
name = "Chris"

if "i" in name:
    print("i is in the name")
    
shuffle(list2)

print(list2)
    