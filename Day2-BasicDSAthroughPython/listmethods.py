lst = [10, 20, 30, 40]

print("Original List:", lst)

lst.append(50)
print("After append:", lst)

lst.extend([60, 70])
print("After extend:", lst)

lst.insert(2, 25)
print("After insert:", lst)

lst.remove(20)
print("After remove:", lst)

lst.pop()
print("After pop:", lst)

print("Index of 30:", lst.index(30))
print("Count of 30:", lst.count(30))

lst.sort()
print("After sort:", lst)

lst.reverse()
print("After reverse:", lst)

copy_lst = lst.copy()
print("Copied list:", copy_lst)

lst.clear()
print("After clear:", lst)
