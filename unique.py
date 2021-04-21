a1=[1,2,2,2,3,3,4,5,6,77,77,88,88,99,99,6,5,4,3]


def unique(lst):
	l1 = set(lst)
	l2 = list(l1)

	return l2

print(unique(a1))

def unique1(lst):
    
    lst2 = []
    for i in lst:
        if i not in lst2:
            lst2.append(i)
        else:
            pass
    
    return lst2

print(unique1(a1))