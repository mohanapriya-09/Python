import main
def palindrom():
    string = main.user_input()
    if string == reversed(string):
        print("The string is palindrom")
    else:
        print("The string is not a palindrom")
