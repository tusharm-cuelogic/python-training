class Parent(object):

	def altered(self):
		print "Parent altered()"

class Child(Parent):

	def altered(self):
		print "Child, Before Parent altered()"
		super(Child, self).altered()
		print "Child, After Parent altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()


# Exercise 44c
# Alter Befor or After
# Overriding where to alter the behavior before or after the Parent class's version runs.
# super: python built-in function to get the Parent version to call.
