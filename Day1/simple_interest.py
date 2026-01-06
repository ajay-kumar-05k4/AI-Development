# Program to calculate simple interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
interest = (principal * rate * time) / 100
print("Simple Interest:", interest)
