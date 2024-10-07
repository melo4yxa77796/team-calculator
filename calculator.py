def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

  def get_user_input():
    operation = input("Enter operation (+, -, *, /): ")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return operation, x, y 