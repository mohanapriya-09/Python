number = input()
for i in range(1, len(number), 2):
    if int(number[i]) % 2 == 0:
        print("False")
        break
else:
    print("True")
