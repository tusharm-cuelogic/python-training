env = {'a' : 42}
exec('x = a+1', env)
print env['x']

##################################

code = 'def add_%d(x): return x + %d'
for i in range(1, 5):
	exec(code % (i, i))

print add_1(3)
print add_3(3)


# We can create functions or classes dynamically using exec
# We can pass a string and execute that piece of code at run time.