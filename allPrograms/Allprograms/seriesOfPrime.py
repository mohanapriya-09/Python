# Prime series in a given range
start = int(input('Enter the starting value'))
end = int(input('Enter the ending value'))
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)