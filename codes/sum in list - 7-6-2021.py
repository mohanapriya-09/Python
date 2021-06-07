lists = []
sum = 0
n = int(input('Enter the number elements you want to sum'))
for i in range(n):
    x = int(input())
    lists.append(x)
    sum += x

for i in lists:
    if(lists.index(i)!=n-1):
        print(i,end = "+")
    else:
        print(i,end = "= ")
print(sum)
print(min(lists)+max(lists))
