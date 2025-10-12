print("if else statement , keywords are - if , elif , else")
name = 'gudu                                                                                                                           '
if name=='gudu':
    print('hello gudu')
elif name=='mama':
    print('oh hello mama')
else:
    print('i do not know who are yeah')


print("\n \n ------for loop---------- ")
ranod_string = "bla bla bla"
for c in ranod_string:
    print(c)

print("tuples unpacking \n \n")
myList = [(1,2) , (4,7) , (7,9)]
for a,b in myList:
    print(a)
    print(b)

print("====iterating  over a dictionary======")
d = {'k1' : 1 , 'k2': 2 , "k3" : 3}
for item in d:
    print(item)

print("====iteerating over a dictioonary key value pair===")
d = {'k1' : 1 , 'k2': 2 , "k3" : 3}
for key,value in d.items():
    print(f"key is {key} value is {value} ")

print("\n \n ----while loop======")
i = 10
while i>0:
    if i%2 ==0:
        print(f"even number {i}")
    else:
       print(f"odd number {i}")
    i-=1
    continue

