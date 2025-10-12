class NotEligibleError(BaseException):
    def __init__(self, note):
        super().__init__(note)
        self.msg=note

class Person:
    def __init__(self , gender , age=0 ):
        self.age=age
        self.gender = gender
    def vote(self):
            if int(self.age) >18:
                print("vote counted")
            else:
                raise NotEligibleError('not eligible')

person = Person('male' , 12)
try:
 person.vote()
except NotEligibleError as e:
    print(e)