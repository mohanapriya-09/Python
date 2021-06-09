string = str(input())
#a = string.split()
for i in string.split():
    length = len(i)
    for j in range(length):
        if(j==0 or j==length-1):
            print(i[j].upper(),end="")
        else:
            print(i[j].lower(),end="")
    print(end = " ")
            
