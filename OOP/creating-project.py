# OOP
from colorama import Fore, Back, Style

class PlayerCharacter:
    
    # Class Object Attribute => self.attribute
    # NOT change across objects built with same Class
    membership = True
    
    # __init__ = class Constructor
    # similar to constructor(attr1, attr2) { super(attr1) } in javascript
    # __init__ is called whenever we instantiate a Class
    # self refers to this Class itself as PlayerCharacter
    # self. = this. in javascript
    def __init__(self, name='anonymous', age=0):  
        # name='anonymous', age=0 => default values
        
        # Instantiating only if age > 18
        if (age > 18):
            self.name = name
            self.age = age
        elif (age == 0):
            print(Fore.RED + f'Failed to instantiate this Class with {self}:\nname: {name}\nage: {age}')
            print(Fore.RED + f'Please check whether you\'ve provided age')
        
            
        # If this.membership = True
        if (self.membership):
            self.name = name # attributes / properties
            self.age = age # attributes / properties
        
    # Instantiating Class with self (this)
    def run(self, hello):
        print(f'{hello} {self.name} is running :D')
        return 'done'
    
    def shout(self):
        print(Fore.YELLOW + f'My name is: {self.name}')
        
    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')
    
    # Decorator
    # to write a function
    # using @classmethod => you'll have access to cls (Class)
    # @classmethod is commonly used when we wanna track & change
    # Class.Attributes => self.name, self.age etc.
    @classmethod
    def adding_things(cls, num1, num2):
        try:
            # Instantiate an Object using cls(name, age)
            # player1.adding_things(): <__main__.PlayerCharacter object at 0x0000019E072F5E50>
            return cls('Teddy', num1 + num2)
        
        except TypeError as e:
            print(Fore.RED + f'TypeError:\n{e}')
    
    # Decorator
    # to write a function
    # using @staticmethod => you'll NOT have access to cls (Class)
    # @staticmethod is commonly used when we do NOT care
    # about Class States => self.name, self.age etc.
    # using @staticmethod when NOT gonna change self.attributes
    @staticmethod
    def adding_things2(num1, num2):
        try:
            # when using @staticmethod
            # cannot be used to access cls (Class)
            return num1 + num2
        except TypeError as e:
            print(Fore.RED + f'TypeError:\n{e}')
        

# Instantiating player1 using class PlayerCharacter
# with default values
player1 = PlayerCharacter('Player1', 20)
#help(player1)
print(Fore.YELLOW + f'player1:\n{player1}')
print(Fore.YELLOW + f'player1.name: {player1.name}') 
print(Fore.YELLOW + f'player1.age: {player1.age}')
print(f'\n')
print(f'player1.speak()')
player1.speak()
print(f'\n')
print(Fore.YELLOW + f'player1.run(): {player1.run("OMG!")}')

player1.name = '!!!'
player1.speak = 'BOOOO'


'''
If everyone keeps doing things like this
The world is gonna end
Cuz everyone's hard work will get totally wiped out...
'''
print(player1.speak) # BOOO




'''
print(f'\n')
player2 = {'name': 'Player2', 'age': 25 }
print(f'player2["name"]: {player2["name"]}')
print(f'player2["age"]: {player2["age"]}')
print(f'\n')
player2 = PlayerCharacter('Player2', 24)
player2.attack = 50

print(Fore.YELLOW + f'player1.membership: {player1.membership}')
print(Fore.YELLOW + f'player2.membership: {player2.membership}')
print(f'\n')
print(Fore.YELLOW + f'player1.shout(): {player1.shout()}')
print(Fore.YELLOW + f'player2.shout(): {player2.shout()}')
print(f'player2:\n{player2}')
print(f'player2.name: {player2.name}')
print(f'player2.age: {player2.age}')
print(f'player2.attack: {player2.attack}')
'''



'''
print(f'\n')
player3 = PlayerCharacter()
player3.attack = 100
'''

print(f'\n')
# When using @classmethod decorator to instantiate a Class
# we must instantiate the Class (cls) 
# @classmethod
# def func(cls, arg1, arg2):

# Otherwise
# TypeError: adding_things() takes 2 positional arguments
# but 3 were given
print(Fore.YELLOW + f'player1.adding_things(): {player1.adding_things(2,3)}')

print(f'\n')
# Instantiating player4 using a function from Class.Attribute
# player4 = PlayerCharacter.adding_things(num1,num2) => Class.Attribute(arg1,arg2)
# rather than just calling the Class => player4 = PlayerCharacter()
player4 = PlayerCharacter.adding_things(2,3)
print(f'player4.age: {player4.age}')