# Factorial of given number
name = str(input("Enter your name:"))
while True:
    if name.isalpha():
        break
    else:
        print("Enter the valid name:")
        name = str(input("Enter your name"))