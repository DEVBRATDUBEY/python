class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

    @classmethod  # decorator
    def adding_things(cls, num1, num2):  # CLS MEANS CLASS
        return num1 + num2

    @ classmethod  # decorator
    def adding_things1(cls, num1, num2):  # CLS MEANS CLASS
        return cls('Teddy',num1 + num2)


player1 = PlayerCharacter('Cindy', 20)
print(player1.adding_things(2, 3))
print(PlayerCharacter.adding_things(2, 3))

player3 = PlayerCharacter.adding_things(2, 3)

print(player3.age)
