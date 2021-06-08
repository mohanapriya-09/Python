num = int(input('Enter the number of row'))
for row in range(1,num+num+1,2):
    temp = row
    for col in range(1,num+1,1):
        if(temp<=9):
            print(" "+str(temp),end=" ")
        else :
            print(temp,end=" ")
        temp += 2
    print()
    
