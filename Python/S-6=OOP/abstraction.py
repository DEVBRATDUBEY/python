# abstraction and abstraction means hiding of information or abstracting

# away information and giving access to only what's necessary.

class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and'
              f' I am {self.age} years old')


player1 = PlayerCharacter('Dev', 100)
player1.speak()  # here encapsulation implemented
# in encapsulation we care about function or method
# and don't necessarily want to know about how function or
# method works.
player1.speak = 'value changed'
print(player1.speak)
print(player1.speak())  # it gives error and says object is not callable
