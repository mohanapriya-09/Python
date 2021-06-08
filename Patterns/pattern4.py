num = int(input('Enter the row'))
for row in range(num,0,-1):
    for col in range (1,num+1,1):
        print(row,end=" ")
    print()
"""
row = 5 col = 1   print
        col = 2    5 5 5 5 5
        col = 3
        col = 4
        col = 5
row = 4 col = 1   print
        col = 2    4 4 4 4 4 
        col = 3
        col = 4
        col = 5
row = 3 col = 1   print
        col = 2    3 3 3 3 3 
        col = 3
        col = 4
        col = 5
row = 2 col = 1   print
        col = 2    2 2 2 2 2 
        col = 3
        col = 4
        col = 5

row = 1 col = 1   print
        col = 2    1 1 1 1 1 
        col = 3
        col = 4
        col = 5
"""
