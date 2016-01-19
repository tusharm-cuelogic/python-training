class Parent(object):
	
	def implicit(self):
		print "PARENT implicit()"

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


# Exercise 44a
# Implicit Inheritance
# The implicit actions that happen when define a function in the parent, but not in the child.
# Child class inherit all of its behavior from Parent class.
