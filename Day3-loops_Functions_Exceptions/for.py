

print("1. Print numbers from 1 to 5")
for i in range(1, 6):
    print(i)

print("\n2. Iterate through a list")
numbers = [10, 20, 30, 40]
for n in numbers:
    print(n)

print("\n3. Sum of first 5 natural numbers")
total = 0
for i in range(1, 6):
    total += i
print("Sum =", total)

print("\n4. Multiplication table of 5")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

print("\n5. Simple star pattern")
for i in range(1, 6):
    print("*" * i)
