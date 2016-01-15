ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Songs", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	print "More stuff list: ", more_stuff
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go stuff: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print "Stuff after pop: ", stuff
print ' '.join(stuff)
print '#'.join(stuff[3:5])
print "Range: ", range(3, 5)


# Exercise 38
# Understood how to do operations on list.
# Got new inbuilt function like join(to convert list into string with given string)
