num = int(input('Enter the number of row'))
for row in range(1,num+1,1):
    temp = row

    for col in range(1,num+1,1):
        print(temp,end = " ")
        temp +=1
    print()
    
