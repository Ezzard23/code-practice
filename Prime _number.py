num = int(input())

def prime_n(num):
    for i in range(2,num):
        if num % i != 0:
            return "Prime Number"
        else:
            return "Not Prime Number"

print(prime_n(num))