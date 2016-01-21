import time

def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        
        return cache[x]
    return g

start_time = time.time()
fib = memoize(fib)
print fib(20)
print("--- %s seconds ---" % (time.time() - start_time))


# Problem 10: Write a function profile, which takes a function as argument and returns a new function, 
# which behaves exactly similar to the given function, except that it prints the time consumed in executing it.
