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
player1.speak()
