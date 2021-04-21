def swap_case(word):
    swap_case = []
    for i in word:
        if i == i.upper():
            swap_case.append(i.lower())
        elif i == i.lower():
            swap_case.append(i.upper())
        else:
            swap_case.append(i)
    return "".join(swap_case)


if __name__ == '__main__':
	s = input()
	print(swap_case(s))
