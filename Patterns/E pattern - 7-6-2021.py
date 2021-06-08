lists = []
row = int(input('Enter the number of rows'))
col = int(input('Enter the number of columns'))

for i in range (row):
    lists.append([])
    for j in range (col):
        lists[i].append(int(input()))
for i in range(len(lists)):
    for j in range(len(lists[i])):
        if(i==0 or j==0 or i==len(lists)//2 or i==len(lists)-1):
            print(lists[i][j],end="")
        else:
            print(" ")
    print()
    
    
