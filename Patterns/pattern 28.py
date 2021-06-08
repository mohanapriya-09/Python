num = int(input("Enter the number of rows"))
for i in range(ord('E'),ord('A'),-1):
    for j in range(num):
        print(chr(i),end=" ")
    print()
