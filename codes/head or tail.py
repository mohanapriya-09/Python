import random
toss = ["HEAD","TAIL"]
choice = str(input())
random.shuffle(toss)
answer = random.choice(toss)
print(answer)
if answer == choice:
    print("You won the toss")
else :
    print("Toss is won by opponent")
