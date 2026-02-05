n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

print("List:", lst)
print("Sum:", sum(lst))
