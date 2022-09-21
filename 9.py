from itertools import filterfalse
data = list(filterfalse(lambda i: i >= 0, [1, -2, 3, 0, -4, 5, 1]))
print(data)
