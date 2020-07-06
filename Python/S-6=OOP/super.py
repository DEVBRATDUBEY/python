# many form
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):  # here we dont need init because we dont have any variable
        print('logged in')


class Wizard(User):  # passing User class implement inheritance
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of'
              f'{self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: left- '
              f'{self.num_arrows}')


def player_attack(char):
    char.attack()


wizard3 = Wizard('Merlin', 60)
player_attack(wizard3)
print(wizard3.attack())  # here attack() implemented polymorphism
