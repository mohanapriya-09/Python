sum = 0
for i in range(1,10,1):
    if(i%2==0):
        print(i,end="")
        sum = i + sum
    if((i+2)%2==0 and (i+2)<10):
        print(end="+")
    
print(end="=")
print(sum)

