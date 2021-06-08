num = int(input('Enter the row'))
temp = 2
for row in range(1,num+1,1):
    for col in range (1,num+1,1):
        if(temp<=9):
            print(" "+str(temp),end=" ")
        else:
            print(temp,end=" ")
        temp +=2
    print()
