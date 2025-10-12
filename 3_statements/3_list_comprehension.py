from random import randint , shuffle


print(f"privide a  num between {randint(1,10)}")
myList = [1.5,2,234,4554,9,5654,23432,67,3453,6,345,74,65,64,6]
shuffle(myList)
print(myList)

print("===this is list comprehension===== to provide readability of code")
anotherList = [num  for num in range(1,10) if num%2==0]
print(anotherList)
