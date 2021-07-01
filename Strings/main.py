import compare
import palindrom
import  concardination
import  range
def user_input():
    a = input("Enter the String")
    return a
print("1.Palindrom\n2.String Compare\n3.String Concardination\n4.Slicing")
operation = int(input("Enter the operation you want to perform"))
if operation == 1:
    palindrom.palindrom()
elif operation == 2:
    compare.compare()
elif operation == 3:
    concardination.concardination()
elif operation == 4:
    print(range.slicing())



