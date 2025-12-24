
#? arthmatic operation

def arithmetic_decorator(func):
    def wrapper(a, b):
        print(f"Performing operation on: {a} and {b}")
        result = func(a, b)
        print(f"Result: {result}\n")
        return result
    return wrapper

@arithmetic_decorator
def add(a, b):
    return a + b

@arithmetic_decorator
def subtract(a, b):
    return a - b

@arithmetic_decorator
def multiply(a, b):
    return a * b

@arithmetic_decorator
def divide(a, b):
    return a / b if b != 0 else "Division by zero not allowed"


add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 0)
