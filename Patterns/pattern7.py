num = int(input('Enter the row'))
for row in range(1,num+1,1):
    for col in range(1,num+1,1):
        if col*row <= 9:
            print(" "+str(row*col),end=" ")
        else:
            print(row*col,end=" ")

    print()

"""
row = 1 col = 1    print
                    1 2 3 4 5
        col = 2
        col = 3
        col = 4
        col = 5
row = 2 col = 1    print
                    2 4 6 8 10
        col = 2
        col = 3
        col = 4
        col = 5

row = 3 col = 1    print
                    3  6  9 12 15
        col = 2
        col = 3
        col = 4
        col = 5

row = 4 col = 1    print
                    4  8 12 16 20
        col = 2
        col = 3
        col = 4
        col = 5
row = 5 col = 1    print
                    5 10 15 20 25
        col = 2
        col = 3
        col = 4
        col = 5
 """

