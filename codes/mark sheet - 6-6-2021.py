mark = []
for i in range(5):
    x = int(input('Enter the mark'))
    mark.append(x)

print("Total=", sum(mark))
print("Average=", sum(mark)/len(mark))
