# OOP
class PlayerCharacter:
    def __init__(self, name, age):  # this is called init or
        self.name = name# constructor or dunder method
        self.age = age

# self is default parameter
    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Cindy', 12)  # because of line 3 i pass cindy
player2 = PlayerCharacter('Tom', 21)  # because of line 3 i pass cindy
player1.attack = 50


print(player1.attack)
print(player1.run())
print(player1)
print(player1.name)
print(player2.age)

