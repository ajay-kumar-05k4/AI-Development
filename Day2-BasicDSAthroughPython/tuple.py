n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

t = tuple(lst)

print("Tuple:", t)
print("Length:", len(t))
#print("Tuple:", t)
print("Maximum:", max(t))
print("Minimum:", min(t))