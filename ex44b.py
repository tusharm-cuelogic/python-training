class Parent(object):

	def override(self):
		print "Parent override()"

class Child(Parent):

	def override(self):
		print "Child override()"

dad = Parent()
son = Child()

dad.override()
son.override()

# Exercise 44b
# Override Explicitly
# Use when we want the child to behave differently.
# override the function in the child class, effectively replacing the functionality of the parent class with same function name.
