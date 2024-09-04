import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = input('Enter some text here:\n')

a = pattern.search(string)
print(f'Pattern matching entered text against our pattern:\n{pattern}\n')

# At least 8 char long
# Contain any sort letters, numbers $%#@
# has to end with a number