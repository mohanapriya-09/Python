def round_sum(a):
    rem = a % 10
    if rem >= 5:
        a = a - (rem-5) + 5
    else:
        a = a - rem
    return a


nums = []
sum_of_values = 0
n = int(input("Enter the n value"))
for i in range(n):
    nums.append(int(input()))
for i in range(n):
    sum_of_values = sum_of_values + round_sum(nums[i])
print(sum_of_values)
