# create a mapping of state to abbrevation
states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New Yourk'
cities['OR'] = 'Portland'

# print out some cities
print '_' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '_' * 10
print "Michigan's abbrevation is: ", states['Michigan']
print "Florida's abbrevation is: ", states['Florida']

# do it by using the state then cities dict
print '_' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbrevation
print '_' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '_' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '_' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city



# Exercise 39
# dicts: Its a list of key : value pairs.
# dicts is a combination of numbers and strings.
# items() returns a list of dict's (key, value) in pairs
# In this exercise we've learned how to create dict & how to access the keys & values
# how to access the key value pair using for-loop.
