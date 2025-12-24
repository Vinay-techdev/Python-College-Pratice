
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(s):
        print(f"Employee name : {s.name}\n Salary: {s.salary}")

class manager(employee):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept

    def show_manager_info(s):
        print(f"Manager department: {s.dept}")

class director(manager):
    def __init__(self, name, salary, dept, region):
        super().__init__(name, salary, dept)
        self.region = region

    def show_director_info(self):
        print(f"Director info: {self.region}") 

obj = director("ABC", 50000, "dev", "India")
obj.show_details
obj.show_manager_info
obj.show_director_info 
