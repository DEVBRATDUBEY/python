# OOP
class PlayerCharacter:
    membership = True  # class object attribute || this attribute is static in nature

    def __init__(self, name, age):  # this is called init or
        self.name = name  # constructor or dunder method
        self.age = age  # this are attributes || this attribute is dynamic in nature

    # self is default parameter
    def run(self):
        # if self.membership:# or write this in  below way
            if PlayerCharacter.membership:
                print('run')
                return 'done'
    def shout(self):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Cindy', 12)  # because of line 3 i pass cindy
player2 = PlayerCharacter('Tom', 21)  # because of line 3 i pass cindy
player1.attack = 50

# help(player1) #it show object
# help(list) # it show list doc in detail
print(player1.membership)
print(player1.shout())
