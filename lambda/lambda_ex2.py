def make_incrementor (n):
	return lambda x: x + n

f = make_incrementor(3)
g = make_incrementor(4)

print f(33), g(45)

print make_incrementor(25)(20)
