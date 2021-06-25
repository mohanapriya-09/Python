name = input("Enter the doctor's name:")
mobile = input("Mobile:")
specification = input("Specification:")
timing = input("Timing:")
cost = input("Cost:")

file = open("doctor's info.txt")
data = file.readlines()
file.close()


if mobile not in str(data):
    file = open("doctor's info.txt","a")
    file.write(name+" "+mobile+" "+specification+" "+timing+" "+cost+"\n")
    file.close()
else:
    print("This mobile number already exist")



