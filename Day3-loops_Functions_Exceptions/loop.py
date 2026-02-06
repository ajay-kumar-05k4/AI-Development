

print("1. BREAK Example")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("\n2. CONTINUE Example")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\n3. NESTED LOOP Example (Pattern)")
for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
    print()
