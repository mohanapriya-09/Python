num = int(input('Enter the number'))
product = 1
for i in range(num,1,-1):
    print(i,end="*")
    product = product * i
print("1",end="=")
print(product)
