num = int(input("Enter the number of rows"))
for i in range(num):
    for j in range(ord('A'),ord('E'),1):
        print(chr(j),end=" ")
    print()
