lists = []
row = int(input('Enter the number of rows'))
col = int(input('Enter the number of columns'))

for i in range (row):
    lists.append([])
    for j in range (col):
        lists[i].append(int(input()))
for i in range(len(lists)):
    for j in range(len(lists[i])):
        if(i==0 or i+j==len(lists)-1 or i==len(lists)-1):
            print(lists[i][j],end=" ")
        else:
            print(end =" ")
    print()

'''
row = 5
col = 5
i = 0       append      j = 0    append
              [[]]        1        [[1,2,3,4,5]]
                          2
                          3
                          4
                          5


i = 1       append           j = 0    append
            [[1,2,3,4,5],[]]     1        [[1,2,3,4,5]]
                              2
                              3
                              4
                              5
i = 2       append           j = 0    append
            [[1,2,3,4,5],     1        [[1,2,3,4,5]]
             [1,2,3,4,5],[]]  2
                              3
                              4
                              5
i = 3       append           j = 0    append
            [[1,2,3,4,5]      1        [[1,2,3,4,5]]
            [1,2,3,4,5],      2
            [1,2,3,4,5]       3
            [1,2,3,4,5],[]]   4
                              5
i = 4       append           j = 0    append
            [[1,2,3,4,5],      1        [[1,2,3,4,5]]
            [1,2,3,4,5],       2
            [1,2,3,4,5],       3
            [1,2,3,4,5],       4
                 []            5



i = 0       j       print
            1        1 2 3 4 5 
            2
            3
            4
            5

i = 1       j       print
            1        1 2 3 4 5 
            2              4
            3            
            4          
            5       
i = 2       j       print
            1        1 2 3 4 5 
            2
            3
            4
            5
i = 3       j       print
            1        1 2 3 4 5 
            2              4
            3            3
            4
            5
i = 4       j       print
            1        1 2 3 4 5 
            2             4  
            3           3
            4         2
            5        1 2 3 4 5 

'''    
