num = int(input('Enter the number of row:'))
for row in range(1,num+1,1):
    temp = 1

    for col in range(1,num+1,1):
        if col%2!=0:
            print(row,end=" ")
        else:
            print(temp,end=" ")
            temp +=1
    print()

""" row = 1 temp = 1
                    col = 1    print
                                1 1 1 2 1
                    col = 2    temp =2
                    col = 3
                    col = 4   
                    col = 5
    row = 2 temp = 1
                    col = 1    print
                               2 1 2 2 2 
                    col = 2    
                    col = 3
                    col = 4
                    col = 5
    row = 3 temp = 1
                    col = 1    print
                                3 1 3 2 3
                    col = 2    
                    col = 3
                    col = 4
                    col = 5
    row = 4 temp = 1
                    col = 1    print
                                4 1 4 2 4
                    col = 2    
                    col = 3
                    col = 4
                    col = 5
    row = 5 temp = 1
                    col = 1    print
                                5 1 5 2 5
                    col = 2    
                    col = 3
                    col = 4
                    col = 5
"""
        
