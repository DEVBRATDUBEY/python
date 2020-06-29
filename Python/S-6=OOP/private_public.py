class PlayerCharacter:
    membership = True

    # 'dunder' is also likely show that hay this is private
    def __init__(self, name, age):
        if age > 18:
            self._name = name  # _ underscore is just convention that says
            self._age = age  # it is a private variable it doesn't force or show error
            # when we override variable

    def shout(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name} and'
              f' I am {self._age} years old')


player1 = PlayerCharacter('Dev', 100)
player1.speak()

# player1.speak = 'value changed'
print(player1.speak)
print(player1.speak())  # it gives error and says object is not callable
