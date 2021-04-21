a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def lst_ol(a,b):
	u = []
	for i in a:
		if i in b:
			u.append(i)
	return u

print(lst_ol(a,b))
