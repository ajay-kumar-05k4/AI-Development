def positional(a, b):
    print("Positional:", a + b)

def keyword(a, b):
    print("Keyword:", a * b)

def default(a, b=10):
    print("Default:", a + b)

def variable(*nums):
    print("Variable:", sum(nums))

positional(5, 3)
keyword(b=4, a=6)
default(7)
default(7, 5)
variable(1, 2, 3, 4, 5)
