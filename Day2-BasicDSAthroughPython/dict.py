d = {
    "name": "Ajay",
    "age": 21,
    "course": "CSE"
}

print("Dictionary:", d)

print("\nIterating using keys:")
for k in d.keys():
    print(k)

print("\nIterating using values:")
for v in d.values():
    print(v)

print("\nIterating using key and value:")
for k, v in d.items():
    print(k, ":", v)
