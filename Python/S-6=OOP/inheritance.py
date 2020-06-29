class User:
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


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Merlin', 100)
print(wizard1)
wizard1.attack()
print(wizard1.sign_in())
archer1.attack()

# instance inbuilt tool to check instance of class
wizard3 = Wizard('Merlin', 60)
print(isinstance(wizard3, Wizard))  # return True
# because wizard3 is instance of Wizard
print(isinstance(wizard3, User))
# every object inherit python object
