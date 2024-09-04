import re

# Using re.compile() to check for 'this' keyword
pattern = re.compile('search')
string = 'search inside this text'

# anyVar = re.search('targetText', var)
a = re.search('this', string)

# We can also use re.compile('keyword') to do search for us
b = pattern.findall(string)
# fullmatch
c = pattern.fullmatch(string)
# .match object
d = pattern.match(string)

# var.group() is useful when performing multiple searches
try: 
    print(f'a.group():\n{a.group()}') # this
except AttributeError as e:
    print(f'a.group():\nAttributeError a.group()\n{e}')
    print(f'\n')
    
# We can also use re.compile('keyword') to do search for us
try:
    print(f'b: {b}') # ['this']
except AttributeError as e:
    print(f'b:\nAttributeError for b\n{e}')
    print(f'\n')

# .fullmatch()
try:
    print(f'c: {c}') # None because do NOT get a fullmatch
except AttributeError as e:
    print(f'c:\nAttributeError for c\n{e}')
    print(f'\n')

# .match()
try:
    print(f'd: {d}')
except AttributeError as e:
    print(f'd:\nAttributeError for d\n{e}')
    print(f'\n')


