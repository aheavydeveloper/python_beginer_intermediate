#generators doesnt create a whole thing in memory upfront.
#proviously we have created functions witn def keyword and we used return keyword to return result from the fucntion.
#generator function allow us to write a function that can send back a value and then later resume to pick up where it left off.
#This type of function is a generator in python allowing us to generate a sequence of values over time.time,
# Insted of generating everything and hold it in memory it allows to generate a sequence of values over time.
#The main difference of syntax will be the use of YIELD keyword.
#so when a generator function is  compiled they become an object that supports some sort of iteration protocol,
# That means they are actually called in your code , they do not return a value and then exit.Insted generator function will automaticaly
#suspend and resume their execution state around the last point of value generation.
#The advantage here is that insted of having to compute an entire series of values upfront and hold it in memeory ,
# the generator computes one value and waits until the next value is called for.
#For example the range() fucntion doesn't produce an list in memory for all teh values from start to stop,
# insted it just keeps track of the last number and the step size to provide a flow of numbers.
#now if the user did need a list then we can simply cat the generator fucntion to a list like -->>> list(range(0,10))

print('now let us see how to create our own generators')
def create_cube(input_list):
    for x in range(len(input_list)):
        yield input_list[x]**3 #this yields a generator

my_list = [1,2,3,4,5]
ans = create_cube(my_list) #ans  is pointing to a generator obj
print(ans)
print(next(ans))
print(next(ans))
#internally what happens in this for loop is next is called on the generator
for x in ans:
    print(x)