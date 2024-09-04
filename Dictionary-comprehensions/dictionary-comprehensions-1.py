# Let's say we've got a list of users
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "password2"),
    (3, "username", "1234")
]

username_mapping = {user[1]: user for user in users}
#print(f'username_mapping:\n{username_mapping}')

# Dictionary comprehensions
# Just using 'username' as a key will give entire tuple
# Create a dictionary mapping usernames to user tuples
print(f'username_mapping["Rolf"]:\n{username_mapping["Rolf"]}')

'''
If we do NOT use a Dictionary Mapping

for user in users:
    if user[1] == "Bob":
        print(f'user:\n{user}')
'''

username_input = input('Enter your username:\n')
password_input = input('Enter your password:\n')

_, username, password = username_mapping[username_input]

if password_input == password:
    print(f'Your credentials are correct!\n')
else:
    print(f'Your credentials are incorrect!\n')
