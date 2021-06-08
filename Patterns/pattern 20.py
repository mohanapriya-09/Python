num = int(input('Enter the number of rows'))
for row in range(1,num+1,1):
    for col in range(1,num+1,1):
        temp = (row*col)%2
        print(temp,end=" ")
    print()
    
