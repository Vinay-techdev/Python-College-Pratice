
# Example 1
class ageError(Exception):
    "Raised When person is less than 18"
    pass

try:
    age = int(input("Enter your age "))
    if age<18:
        raise ageError
except ageError:
    print("Person is not eligible to vote")
else:
    print("Person is eligible to vote")

name = input("Enter the name")
g = input("Enter the gender")

# Example 2
name = input("Enter the name")
gender = input("Enter the gender")

try:
    if gender not in ['Male',"male","Female","female","other","Other"]:
        raise Exception("Not a proper Gender ")
    else:
        age = int(input("Enter the age  "))
        if age < 18:
            raise Exception("age should be greater than 18 ")
        else:
            print(f"the name is {name} . gender  {gender}, age {age}")
except Exception as e:
    print(f"Exception Handled: {e}")