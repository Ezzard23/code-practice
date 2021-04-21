from math import prod
import random as rd
import string

abc = string.ascii_lowercase
strong_or_weak = str(input("Choose Password Strength: A) Strong B) Weak: "))

def generate_password(strong_or_weak):
    if strong_or_weak == "A" or strong_or_weak == "a" or strong_or_weak == "Strong" or strong_or_weak == "strong":
        result_strw = ''.join(rd.choice(abc) for i in range(0,12))
        result_intw = 1
        return result_strw[:6] + str(result_intw) + result_strw[6:]
    elif strong_or_weak == "B" or strong_or_weak == "b" or strong_or_weak == "Weak" or strong_or_weak == "weak":
        result_strw = ''.join(rd.choice(abc) for i in range(0,6))
        result_intw = 0
        return result_strw[:3] + str(result_intw ) + result_strw[3:]

generate_password(strong_or_weak)


