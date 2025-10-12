print("def key word to declare a fucntion/method in python")
print("a function declared within a class is generally called a method, we can create functions that acomplishes something and \n "
      " we can re use it when needed , we will talk more about method when we discuss about oop and create our own class , for now \n"
      "we will use some build in method that are provided to us by python for diffrerent classes and we woill see some of the things bellow \n"
)
print("we will see bellow concepts : \n 1.declare a function \n 2.tuples unpacking \n 3.args & kwargs \n 4.lamda expression(map and filter) \n 5.scope")

print("\n \n====== declaring function and using it===========")
def perform_operation(num1 , num2 , operation):
    result = None
    if operation == "+" :
        result = num1-num2
    elif operation== "-":
        result = num1 -num2
    elif operation == "/":
        result=num1/num2
    else:
        return None
    return result
print(perform_operation(2,3,"/"))


print("\n \n====== tuples  unpacking (fucntions returning multiple items basicaly think kinda list inside list and we have un packing)==========")
def top_2_stock():
    return [('google', 200),('microsoft', 300)]
result = top_2_stock()
for name, price in result:
    print(f"stock name is {name} , price is {price}")


print("\n \n====== args and kwargs===========")
def a_function(item1 , item2 , default_1=0 , default2=0):
    pass

def args(*args):
    for item in args:
        print(item,sep=",", end=" ")

def kwargs(**kwargs) :
    for key,val in kwargs.items():
        print(f"key is {key} and val is {val}" , sep="," , end=" , ")

print("we can either pass that default value if we want to else it will use that from the function \n")
a_function(2,3,default2=23)
print("we can pass many args all will be collected as tuples")
args(1,2,3,)
print('\nsame as *args but this one is for dictionaries')
kwargs(e1="jj", e2="chris",e3="urmikha" )


print("\n \n====== lamda functions also known and anonynous function that we use once in general , can use only a singl statement ===========")
print("A Python lambda function is explicitly designed to be a single expression whose result is immediately returned. "
      "It is limited to what can be written on a single line as an expression.")
#suppose we have a function that returns square of a number , how does that look like in a simple function is
def cal_square(num):
    return num**2
#to represent the same using lamda
lamda_fun = lambda num:  num**2
print(lamda_fun(5))
#suppose we have a list of items and we want square each item in the list , we can use map function in that case
my_list = [1,2,3,4]
square_result_list = list(map(lambda num:  num**2 , my_list)) # casting the result to a list, we can do it like this
print(f"square result is :{square_result_list}")
#similar to map we have filter function which inted work with a lamda fucntion that returns True or False and we can take action on bahlf of each item based on the condition
filtered_res = list(filter(lambda n:  n!=2 , my_list))
print(f"filtered result is :{filtered_res}")





