
class person:
    name = "Unknown"
    age = 00

    def __init__(self, name, age = 21):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hi {self.name}, you are {self.age} years old right?")

obj = person("Vinay", 21)

# creating multiple instance of class
obj1 = person("Virat", 35)
obj2 = person("ABD", 37)

obj.greet()
obj1.greet()
obj2.greet()

#modifying an attribute values
obj.age = 22
obj.greet()
