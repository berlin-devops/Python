number = 7

user_input = input('Please enter \'y\' if you\'d like to play: ')

def guess_number(user_number):
    if user_number == number:
        print(f'\n')
        print(f'You entered {user_number}\nwhich has matched answer "{number}"\n')
    elif number - user_number in (1, -1):
        print(f'You\'re off by one...')
    elif abs(number - user_number) == 1:
        print(f'You\'re off by one...')
    else:
        print(f'\n')
        print(f'You entered "{user_number}"\nwhich does NOT match\nPlease try again\n')

# Previously, we use
# if user_input.lower == "y":
if user_input in ("y", "Y"):
    user_number = int(input('Guess our number:\n'))
    guess_number(user_number)
elif user_input.lower() != "y":
    print(f'You did NOT agree to play\n')

