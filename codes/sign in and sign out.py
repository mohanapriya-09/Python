user = {"test@gmail.com": ["123", 9988776655], "demo@gmail.com": ["234", 1122334455]}
while True:
    print("1.New USer \n2. Existing User \n3.Exit")
    option = int(input('Enter your choice'))
    if option == 1:
        email = str(input("Enter the email id"))
        password = str(input("Enter the password"))
        mobile = int(input("Enter the mobile number:"))
        if email in user.keys():
            print("Existing email Id")
        else:
            user[email] = [password,mobile]
    elif option == 2:
        email = str(input("Enter the email id"))
        password = str(input("Enter the password"))
        if email in user.keys() and password == user[email][0]:
            print("Signed in")
        else:
            print("Enter the valid email id")
    elif option == 3:
        break
    else:
        print("Enter a valid input")
