try:
    with open("number.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
