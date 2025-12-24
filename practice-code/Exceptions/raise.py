
# Example 1
def set_age(age):
    if age<0:
        raise ValueError("Age cannot be negtaive")

# Example 2    
name = ""

if name == "":
    raise Exception("Name cannot be empty")

# Example 3
age = "Twenty"

if not isinstance(age, int):
    raise ValueError("Age shold not contains string")