''' Generators:
Generate a sequence of values over time
For example range(100) = a generator
a Generator can pause & resume functions
a range creates value 1 by 1
'''
#range1 = range(100)
#print(f'range1:\n{range1}')
#print(f'\n')

''' Convert a range => list
list of range(100) creates all 0 to 99 all at once
inside memory
'''
#list1 = list(range(100))
#print(f'list1:\n{list1}')

def make_list(number):
    # Prepare to store value into []
    result = []

    ''' in the past, this creates value 1 by 1 in memory
    for eachInteger in number:'''
    '''this generates all values in memory at a time
    much better performance'''
    for eachInteger in range(number):
        result.append(eachInteger * 2)
    return result

my_list1 = make_list(100)
print(f'my_list1:\n{my_list1}')