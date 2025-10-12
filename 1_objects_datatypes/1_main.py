#data types # int # float # str # list # dict # tuple # set # bool

integer =  20
floating_point = 33/65
print(f"floating point number is {floating_point}")

#python provides some fuctions like len to count the length of a string , tuples , list etc..There are other functions also like open to opoen a text file
#string is immutable in python , we can not chage it once created
string = "this is a string "
print(f"getting charecter at a  positions {string[0]}")
print(f"we can get the length of the string by len function, the length of the above string is : {len(string)}")
print(f"we can split the string using split method of string class, and by default it will split by white spaces :  {string.split()}")
print(f"some other string functions are upper :  {string.upper()} , lower {string.lower()}")
print(f"now let us see how do we get a substring of a string the way we do it is : {(string[0:7:2])}")
print(f"reversing the above string using the technique : {string[::-1]} \n\n")


print("-------------------------now let us look at list ----------------------------------")
random_list = [1, "number" , "5.0890" , True]
print(f"access elemets by index :  {random_list[0]}")
print(f"length of the list is :  {len(random_list)}")
print(f"we can split and apply same technique we did in string to get a sub list  of the list like : {random_list[1:3:]}")
sublist= random_list[1:3]
print(sublist)
print(f"appending an element to the list with append method :{random_list.append("family")} , after appenign list looks like : {random_list}")
print(f"pop out element from the end of  list using pop method : {random_list.pop()} , after poping the last element list lis {random_list}")
print(f"pop out element from the any position  of  list using pop method and passing index number : {random_list.pop(1)} , after poping 1st index list is {random_list} \n\n")


print("---geting started with tuples-----")
a_tuple = (1,"another" , "4.89347" , 7,3284738 , False)
print(f"a tuple is immutabel , other than that similar to the list \n \n")



print("----string with dictionaries-=------")
print("-----dictionary stores key value pair , similar to hasmap the sequence is not guaranteed and multiple keys are not allowed")
dictionary = dict(name="janmejaya", age=23, address = dict(pin="560102" , landmark = "near siridi sai temple"))
print(dictionary)

print("this is simple way of assigning the dictionary in python way")
employee = {
    'name' : "janmejaya",
    'age':23,
    'age':29,
    'salary':123000.54,
    'address':{
        "permanent":{
            'pin':560102
        },
        "current":{
            'pin':"756102"
        }
    }
}
print(f"dictionary is a key value pair , get the value by passing key like : {employee['age']}")
print(f"to get the list of keys of the employee in the form of a list : {employee.keys()}")
print(f"to get the list of values of the employee in the form of a list : {employee.values()}")
print(f"to get the list of key  values pair in form of a list of tuples  : {employee.items()} \n \n \n")


print("----string with sets-=------")
random_set = set()
random_set.add(1)
random_set.add(2)
random_set.add(2)
print(f"set only contains unique elements {random_set} ,  pop element from set: {random_set.pop()} , after poping set is {random_set} \n\n")



print("-----starting wiht boolean-----")
print("boolean we write as True and False , T and F is capital")
print(1>2)


