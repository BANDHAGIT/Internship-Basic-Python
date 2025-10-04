# Basic Function
print("=== Basic Function ===")
def say_hello():
    print("Hello, World!")

say_hello()

# Function with Parameters
print("\n=== Function with Parameters ===")
def greet(name):
    print("Hello,", name)

greet("Haidar")
greet("Python")

# Function with Return Value
print("\n=== Function with Return Value ===")
def add(a, b):
    return a + b

result = add(5, 3)
print("Result:", result)