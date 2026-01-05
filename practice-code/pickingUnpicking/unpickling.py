
#? Unpickling - deserliztion
# unpicking is the process of converting binary format into python object
# Syntax pickle.load(file)

# 1
import pickle
file_obj = open("binaryfile.txt", "rb")
loaded_data = pickle.load(file_obj)

print("Grade loaded data -> ", loaded_data)
file_obj.close()

# 2
with open("studentBinary.txt", "rb") as file:
    data = pickle.load(file)
print("students loaded data -> ", data)

# 3

class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
        

student1 = student("Alice", 20, "A")
with open("marksBinary.txt", "rb") as m:
    mData = pickle.load(m)

print("Marks loaded data -> ", mData)