def separate(num1, num2):
    rem1 = num1 % 10
    quo1 = num1//10
    rem2 = num2 % 10
    quo2 = num2//10
    return add(rem1, rem2, quo1, quo2)


def add(rem1, rem2, quo1, quo2):
    return (rem1+quo2) + (rem2+quo1)


num1 = int(input())
num2 = int(input())
sum = separate(num1, num2)
print(sum)
