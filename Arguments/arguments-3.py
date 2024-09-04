def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def apply(*args, operator):
    if operator == "*":
        ''' * Asterisk unpacks all entered values
        and unpack these values as passed-in params
        into functions'''
        return multiply(*args)
    elif operator == "+":
        return sum(*args)
    else:
        return "No Valid operator specified to apply() "

print(f'apply(1, 3, 5, 7, operator="+") :')
print(apply(1, 3, 5, 7, operator="+")) #16
print(f'\n')
print(f'apply(1, 3, 5, 7, operator="*") :')
print(apply(1, 3, 5, 7, operator="*")) #105