print eval("2+3")

a = 2
print eval("a * a")

env = {'x' : 42}
print eval('x+1', env)

# eval is like exec but it takes an expression and returns its value.