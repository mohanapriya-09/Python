num = int(input('Enter the number of rows'))
a = ord('A')
for i in range(num):
    n = a
    for j in range(num):
        print(chr(n),end = " ")
        n +=1
    a+=1
    print()
