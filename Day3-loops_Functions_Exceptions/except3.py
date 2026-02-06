try:
    num = int(input("Enter number: "))
    result = 10 / num
    print("Result =", result)

except ZeroDivisionError:
    print("Division by zero not allowed")

except ValueError:
    print("Enter valid integer")

finally:
    print("Execution completed")
