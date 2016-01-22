def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def trace(f):
    f.indent = 0
    def g(x):
        print '|  ' * f.indent + '|--', f.__name__, x
        f.indent += 1
        value = f(x)
        print '|  ' * f.indent + '|--', 'return', repr(value)
        f.indent -= 1
        return value
    return g

def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g

fib = trace(fib)
fib = memoize(fib)
print fib(4)

# Decorators - 6.2.2. Example: Memoize
# get rid of the redundant computation by caching the result function when it is called for the first time 
# and reuse it when it is needed next time.