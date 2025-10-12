from datetime import datetime
from dateutil.relativedelta import relativedelta

print("here we will discuss about class key word and attributes in class \n\n")
print("class keyword")
class Person:
    #class attribute , same for every instance
    species = 'mamal'
    def __init__(self, name, birth_date, age=0):
        self.name = name
        self.birth_date = birth_date
        # Note: You don't need to store age here, as it's calculated dynamically

    def getAge(self):
        # 1. Define the format of the birth_date string
        date_format = "%d/%m/%Y"
        # 2. Parse the birth_date string into a datetime object
        try:
            birth_date_dt = datetime.strptime(self.birth_date, date_format)
        except ValueError:
            # Handle cases where the string doesn't match the expected format
            return "Error: Invalid date format. Expected 'dd/MM/yyyy'."
        # 3. Get the current date
        today = datetime.now()
        # 4. Calculate the difference using relativedelta
        # relativedelta calculates the difference in years, months, and days
        age_difference = relativedelta(today, birth_date_dt)
        # 5. Return the age in years
        return age_difference.years


# --- Example Usage ---
# Note: You may need to install the dateutil library if you don't have it: pip install python-dateutil
person1 = Person("Alice", "09/04/1999")
print(f"{person1.name}'s birth date: {person1.birth_date}")
print(f"{person1.name}'s calculated age: {person1.getAge()} years")

person2 = Person("Bob", "01/01/2000")
print(f"{person2.name}'s calculated age: {person2.getAge()} years")
print(f"class attribute {person2.species} , we can also get it directly like {Person.species}")



