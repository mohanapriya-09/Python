multiple = int(input('Enter the multiple:'))
start = int(input('enter the starting range:'))
ending = int(input('enter the ending range:'))
for i in range(start,ending+1,1):
    product = multiple * i
    print(i,"*",multiple,"=",product)
