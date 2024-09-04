# Traditionally
def double(x):
    return x * 2

sequence = [1, 3, 5, 7, 9]

# i. Using list comprehension
# This usage of a list comprehension is straightforward
# making it easy to see that each element 'x' from sequence is passed to the double function
doubled = [double(x) for x in sequence]

# ii. Using Lambda function
# Useful for quick, non reuseable single line of code
# NOT so readable for beginners
doubled = [(lambda x: x * 2)(x) for x in sequence]

# iii. Using a 'map' for functions application
# This is a more Functional Programming approach
doubled = map(double, sequence)