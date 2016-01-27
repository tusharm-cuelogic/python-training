foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print filter(lambda x: x % 3 == 0, foo)

print map(lambda x: x * 2 + 10, foo)

print reduce(lambda x, y: x + y, foo)

# use the standard functions filter(), map() and reduce() to do various things with that list. All of the three functions expect two arguments: A function and a list.