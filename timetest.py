import time

def timetest(f):
    def inner(*arg):
        a=time.time()
        f(*arg)
        b=time.time()
        return "Execution time: "+str(b-a)
    return inner

def name(f):
    def inner(*arg): 
        f(*arg)
        return f.func_name + ' ' + str(arg)
    return inner
    
@name
def fib2(n):
    if n<=1:
        return 1
    else:
        return fib2(n-1)+fib2(n-2)

@timetest
def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print fib(10)
print fib2(5)
