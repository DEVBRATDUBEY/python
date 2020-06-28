# OOP
class PlayerCharacter:
    def __init__(self, name): # this is called init or
        self.name = name #constructor or dunder method

    def run(self):
        print('run')


player1 = PlayerCharacter('Cindy')# because of line 3 i pass cindy


print(player1)
print(player1.name)
