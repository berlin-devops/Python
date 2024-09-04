'''
A list = Iterable
A Dunder Method __iter__
Just like 'while' loop | 'for' loop
__iter__ goes over some iterable => do something on it => move on to the next iterable

Generators = a kind of iterables
Yet, not every iterable can become Generators

For example,
range() = a generator
list() = an Iterable, but NOT a Generator
'''

'''
def make_list(number):
    # Prepare to store value into []
    result = []

    # in the past, this creates value 1 by 1 in memory
    for eachInteger in number:
    # this generates all values in memory at a time
    # much better performance
    for eachInteger in range(number):
        result.append(eachInteger * 2)
    return result

my_list1 = make_list(100)
print(f'my_list1:\n{my_list1}')
'''

def generator_function(num):
    for i in range(num):
        # yield pauses the function & come back to it later
        yield i * 2

# now, we 'for' loop to come back to generator_function
#for item in generator_function(100):
#    print(f'{item}')
g = generator_function(100)
next(g) # 0
next(g) # 2
print(next(g)) # 4
print(next(g)) # 6

g2 = generator_function(1)
next(g2)
next(g2)
print(f'g2 1st next(g2) => 2nd next(g2):\nprinting 3rd next(g2): {print(next(g2))}')
# StopIteration because the iteration was over already
