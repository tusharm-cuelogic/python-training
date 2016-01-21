def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def trace(f):
    def g(x):
        print f.__name__, x
        value = f(x)
        print 'return', repr(value)
        return value
    return g

fib = trace(fib)
print fib(3)

#def trace(f):
#    f.indent = 0
#    def g(x):
#        print '|  ' * f.indent + '|--', f.__name__, x
#        f.indent += 1
#        value = f(x)
#        print '|  ' * f.indent + '|--', 'return', repr(value)
#        f.indent -= 1
#        return value
#    return g

#fib = trace(fib)
#print fib(4)

# Decorators - 6.2.1. Example: Tracing Function Calls
# functions are first-class objects
# functions are first-class objects. They can be passed as arguments to other functions and a new functions can be returned from a function call.