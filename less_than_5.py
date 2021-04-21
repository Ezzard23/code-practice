a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_than_five(lst):
  b = []
  for i in lst:
  		if i < 20:
  			b.append(i)
  return b
             
print(less_than_five(a))