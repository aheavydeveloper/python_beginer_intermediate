print("python provides some operators or generators, we can use them to make the code more readable")

print("\n\n ======== range operator======")
for i in range(1,10):
    print(i)
my_list = ["names" , "last names" , "titles" , "good names" , "nick name" , "first name" , "middle name"]
for i in range(0 , len(my_list)):
    print(my_list[i])


print("\n \n  some  times we want both index and value of the list while iterating what python provide is an enumurator  like bellow")
employees = ["janmejeya" , '23' ,'32']
print(enumerate(employees))
for index,item in enumerate(employees):
    print(f"index   is {index} and item is {item}")


print("\n \n================== we can check if something is present using the in ======================")
emp_list = ['gudu' , 'urmikhs' , 'sayar sahab' , "christina" , 'anshika']
print('gudu' in emp_list)
print('gudu' not in emp_list)
dictionary = {
    'fruit': 'mango',
    'veges':'carot'
}
print(f"checking if fruit is in dictionary : {'fruit' in dictionary}")
