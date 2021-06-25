# Performing square, cube, and add using a function
def get_input():
    a = int(input())
    add(square(a), cube(a))


def square(a):
    square = a*a
    return square


def cube(a):
    cube = a*a*a
    return cube


def add(a, b):
    print(f"{a}+{b}={a+b}")


get_input()
