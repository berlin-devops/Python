'''
# Traditionally
def add(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x + y
    else:
        raise TypeError("Either x | y is NOT a number")
    
result = add(3, 3.1415)
print(f'result:\n{result}')
print(f'\n')
result2 = add(3, "1")
print(f'result2:\n{result2}')
print(f'\n')
'''

# Using Lambda function without using a 'return'
add2 = lambda x, y: x + y
print(f'Result for add2(x, y):\n{add2(2, 4)}')