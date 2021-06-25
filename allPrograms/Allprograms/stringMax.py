# Finding Largest String
sen = str(input())
List = []

for i in sen.split(" "):
    if i.isdigit() and '9' not in i:
        List.append(i)
if len(List) <= 0 :
    maximum = -1
else:
    maximum = max(List)
print(maximum)

