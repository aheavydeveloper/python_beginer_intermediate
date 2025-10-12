
class Animal:
    species = 'mamal'
    #in most of the object oriented programing this self or  the obj is passed as an hiddend param, but in python we have to explicilty put it
    def __init__(self):
        print('animal created')
    def whoAmI(self):
        print('i am an animal')
    def eat(self):
        (print('animal eating'))

class Dog(Animal):

    def __init__(self, breed):
        print('dogo created')
        super().__init__()
        self.breed = breed

    def eat(self):
        (print(f"{self.breed} is  eating"))
        pass#it's like returning void

dog1 = Dog('lab')
print(f"i can access the class attribute via obj or class :{dog1.species}")
print(f"it is also an class attribute , we can acces it via class also : {Dog.species} or via Animal also {Animal.species}" )
dog1.eat()
dog1.whoAmI()
