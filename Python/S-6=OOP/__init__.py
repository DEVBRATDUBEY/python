class PlayerCharacter:
    membership = True  # class object attribute || this attribute is static in nature

    def __init__(self, name='anonymous', age=0):  # this is called init or
        if(age > 18):
            self.name = name  # constructor or dunder method
            self.age = age  # this are attributes || this attribute is dynamic in nature

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Cindy', 20)  
print(player1.shout())