try:
    x = int(input("Enter number: "))
    print(10/x)

except Exception as e:
    print("Error:", e)

else:
    print("No error occurred")

finally:
    print("Program finished")
