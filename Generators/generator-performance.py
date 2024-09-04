# Iterable
# generators

def generator_function(num):
    for i in range(num):
        yield i

'''
g = generator_function(100)
next(g) # hidden 0
next(g) # hidden 1
print(next(g)) # 2 
print(next(g)) # 3
'''

# Decorator
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1}seconds')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    # A Generator has much better performance
    # compared to a list(range(int))
    for i in range(1000000000):
        i * 5

@performance
def long_time2():
    print('2')
    # A List has much lower performance compared to
    # a Generator
    for i in list(range(1000000000)):
        i * 5

long_time()
long_time2()

