s = {10, 20, 30}

print("Original:", s)

s.add(40)
print("After add:", s)

s.remove(20)
print("After remove:", s)

s.discard(50)
print("After discard:", s)

s.pop()
print("After pop:", s)

s2 = s.copy()
print("Copy:", s2)

s.clear()
print("After clear:", s)
