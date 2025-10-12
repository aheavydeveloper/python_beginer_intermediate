print(">>>> here we are going to discover few new concepts similar to assigning functions and passing in as param in java script\n"
      "1)assigning function to variables\n"
      "2)passing in function into another function as a parameter")
print("It is important to know the fuctions are alos objects that can be passed into other objects")
print('let us first see assigning a function to a variable')
def hello():
   return'hello There'
print(f"we can print the function in memory like : {hello}")
#we can assign the function to a variable like bellow , now this greet holds  a copy of the hello function,even thought hello fun is
#delted greet still will work, let us see with example bellow
greet = hello
del hello
print(f"we can call the function with hte the varible like : {greet()}")
print("\n\n")


#we can pass fucntion as prams similarly a function can return anotehr function
print('we can pass function as a param')
def ref_fun():
    print('hi\' i am a ref function ')

def anothre_fun(fun):
    print('hi\' i am a function 1')
    fun()
anothre_fun(ref_fun)

print("\n------another example-------")


# 1. The function we want to pass (it requires two parameters)
def add(a, b):
    return a + b

# 2. The function that receives another function as an argument
def calculator(func_to_run, x, y):
    print(f"Executing operation on {x} and {y}...")
    # The receiver calls the passed function (func_to_run)
    # and supplies the required parameters (x and y).
    result = func_to_run(x, y)
    return result
# --- Usage ---
result = calculator(add, 5, 3)
print(f"The result is: {result}")
# Output: The result is: 8