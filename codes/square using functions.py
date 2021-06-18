def square():
    print("Square of a = ",a*a)

    
def cube():
    print("Cube of a = ",a*a*a)

    
def factorial():
    fact = 1
    for i in range(a,0,-1):
        fact = fact * i
    print("factorial of a = ",fact)

    
def sum_series():
    sum = 0
    for i in range(1,a+1,1):
        sum += i
        if(i != a):
            print(i,end=" + ")
        else:
            print(i,end=" = ")
    print(sum)

    
a = int(input("Enter the value of a:"))
square()
cube()
factorial()
sum_series()
