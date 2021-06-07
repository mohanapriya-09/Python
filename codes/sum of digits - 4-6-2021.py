num = int(input('Enter the number'))
sum = 0
count =0
countt=0
number = num
while num !=0:
    num = num//10
    count+=1
while number!=0:
    n = number%10
    print(n,end="")
    if(count!=countt):
        print(end="+")
    sum = sum +n
    number = number//10
    countt+=1
    
print("=",int(sum))
"""
num = 123
    num     count
    12      1
    1       2
    0       3
number      n     sum
    12      3      3
    1       2      5
    0       1      6

"""
