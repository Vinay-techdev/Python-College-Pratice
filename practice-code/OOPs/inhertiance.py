

class A:
    def show(self):
        print("Method in A")
        super().show()

class B :
    def show(self):
        print("Method in B")

class C(A,B):
    def show(self):
        print("Method in C")
        super().show()

obj = C()
obj.show()