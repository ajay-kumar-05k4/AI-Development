s1 = set()

n = int(input("Enter number of elements for Set1: "))
for i in range(n):
    x = int(input())
    s1.add(x)

print("Set1:", s1)

s1.add(int(input("Enter element to add: ")))
print("After add:", s1)

s1.remove(int(input("Enter element to remove: ")))
print("After remove:", s1)

s2 = set()
m = int(input("Enter number of elements for Set2: "))
for i in range(m):
    x = int(input())
    s2.add(x)

print("Set2:", s2)

print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))

print("Iterating Set1:")
for i in s1:
    print(i)
