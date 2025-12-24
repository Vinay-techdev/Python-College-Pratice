
#? add two numbers
# # My method
# class sum:
#     def add(slef, a, b):
#         return a+b
    
#     def display(slef, res):
#         print("The sum of two numbers: ", res)
    
# obj = sum()
# res = obj.add(10, 20)
# obj.display(res)

# # slide method
# class sum:
#     def add(slef, a, b):
#         slef.res =  a+b
    
#     def display(slef):
#         print("The sum of two numbers: ", slef.res)
    
# obj = sum()
# obj.add(10, 20)
# obj.display()

# Arthmatic operation

class sum:
    def s(slef, a, b):
        slef.res1 = a+b

    def sub(slef, a, b):
        slef.res2 = a -b

    def mul(slef, a, b):
        slef.res3 = a *b

    def div(slef, a, b):
        slef.res4 = a/b

    def mod(slef, a, b):
        slef.res5 = a%b
    
    def display(slef):
        print("The sum of two numbers: ", slef.res1)
        print("The sub of two numbers: ", slef.res2)
        print("The mul of two numbers: ", slef.res3)
        print("The div of two numbers: ", slef.res4)
        print("The mod of two numbers: ", slef.res5)

obj = sum()
obj.s(10, 20)
obj.sub(20, 10)
obj.mul(10, 20)
obj.div(10, 20)
obj.mod(10, 20)
obj.display()
