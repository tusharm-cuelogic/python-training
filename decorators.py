def outer(some_func):

	def inner():
		print "before some_func"
		ret = some_func()
		print ret + 1
	return inner

def foo():
	return 1

decorated = outer(foo)
decorated()

# Decorator is a callable that takes a function as an argument and returns a replacement function.
