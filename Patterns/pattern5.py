num = int(input('Enter the row'))
temp = 1
for row in range(1,num+1,1):
    for col in range (1,num+1,1):
        if(temp<=9):
            print(" "+str(temp),end=" ")
        else:
            print(temp,end=" ")
        temp +=2
    print()
"""
row = 1 col = 1     print
                    1  3  5  7  9
        col = 2
        col = 3
        col = 4
        col = 5
row = 2 col = 1     print
                    11 13 15 17 19
        col = 2
        col = 3
        col = 4
        col = 5

row = 3 col = 1     print
                    21 23 25 27 29 
        col = 2
        col = 3
        col = 4
        col = 5
row = 4 col = 1     print
                    31 33 35 37 39
        col = 2
        col = 3
        col = 4
        col = 5
row = 5 col = 1     print
                   41 43 45 47 49
        col = 2
        col = 3
        col = 4
        col = 5

"""
