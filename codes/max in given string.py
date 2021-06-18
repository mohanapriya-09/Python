sen = str(input())
List = []

for i in sen.split(" "):
    if i.isdigit()and '9' not in i:
        List.append(i)
if len(List) <= 0 :
    max = -1
else:
    max = max(List)
print(max)
