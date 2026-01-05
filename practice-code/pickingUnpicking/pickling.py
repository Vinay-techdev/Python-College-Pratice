
#? Picking - serlization
# picking is the process of converting a python object into binary format
# it can be saved to file or transferred over network


#? What can be picked in python?
# 1. Data type 
# 2. custom class an objects
# 3. Functions
# 4. DataFrame in machine learning
# 5. list, tuples, sets and dict

#! What cannot b picked
# 1. Lambda function
# 2. Nested Functions and local functions
# 3. Sockets,
#? syntax - pickle.dump(object, file)

import pickle

# 1

grade_list = ['A', 'B', 'C', 'D', 'E']
file_obj = open("binaryfile.txt", "wb")

pickle.dump(grade_list, file_obj)
print("pickle stores data in abinary format which is not readble format")
file_obj.close()

# 2

student_info = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subject": ["Math", "Science"]
}

with open("studentBinary.txt", "wb") as file:
    pickle.dump(student_info, file)
print("Dictionary converted into binary format")

# 3 Class

class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
        

student1 = student("Alice", 20, "A")

with open("marksBinary.txt", "wb") as m:
    pickle.dump(student1,m)
print("Class object converted into binary format")

