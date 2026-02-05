n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

t = tuple(lst)

print("Tuple:", t)

val = int(input("Enter element to check: "))

print("Count:", t.count(val))

if val in t:
    print("Index:", t.index(val))
else:
    print("Element not found in tuple")
