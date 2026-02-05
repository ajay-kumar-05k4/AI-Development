d = {}

n = int(input("Enter number of key-value pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("\nDictionary:", d)

u_key = input("\nEnter key to update/add: ")
u_value = input("Enter new value: ")
d[u_key] = u_value
print("After update:", d)

del_key = input("\nEnter key to delete: ")
if del_key in d:
    d.pop(del_key)
    print("After deletion:", d)
else:
    print("Key not found")

print("\nIterating dictionary:")
for k, v in d.items():
    print(k, ":", v)

search = input("\nEnter key to search: ")
if search in d:
    print("Key exists with value:", d[search])
else:
    print("Key not found")
