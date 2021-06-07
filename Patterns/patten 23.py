num = int(input('Enter the number of rows'))
for row in range(1,num+1):
    for col in range(1,num+1):
        temp = (row)%2
        print(temp,end=" ")
    print()
