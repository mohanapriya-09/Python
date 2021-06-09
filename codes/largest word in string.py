string = str(input())
length = 0
for i in string.split():
    if(length < len(i)):
        largest_string = i
        length = len(i)
print(largest_string)
