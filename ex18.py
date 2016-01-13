# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# takes no argumets
def print_none():
	print "I got nothin'."

print_two("Tushar", "Mate")
print_two_again("Pranav", "Naxane")
print_one("Cuelogic")
print_none()


# Understands following points in exercise 18
# How to write function defination.
# How to pass arguments to function.
# How to call function.
