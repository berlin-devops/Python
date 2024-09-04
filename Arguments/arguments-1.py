def multiply(*args):
    print(f'args:\n{args}')
    total = 1
    for arg in args:
        total *= arg

    return total

# 1 * 1 = 1; 1 * 3 = 3; 3 * 5 = 15
print(multiply(1, 3, 5)) 

#multiply('hi', 'hello', 'test')
# ('hi', 'hello', 'test)