def formula(a,b):
    return add(a,b) * add(a,b)
def add(a,b):
    return a+b
a = int(input())
b = int(input())
print(formula(a,b))
