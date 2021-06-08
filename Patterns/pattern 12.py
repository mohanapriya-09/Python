num = int(input('Enter the row number'))
for row in range (1,num+1):
    i = row
    for col in range (1,num+1):
        print(i,end=" ")
        i += num
    print()
    
