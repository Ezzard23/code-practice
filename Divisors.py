a = int(input("Enter Number: "))

def divisor(a):
	b = []
	for i in range(1,a+1):
		if a % i == 0:
			b.append(i)
	return b

print(divisor(a))
