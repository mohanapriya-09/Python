import main
def slicing():
    string = main.user_input()
    start = int(input("Enter the starting range:"))
    end = int(input("Enter the ending range:"))
    return string[start:end]

