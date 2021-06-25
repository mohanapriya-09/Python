# Length of a String
sentence = str(input())
count = 0
length = len(sentence.split(" "))
print(f"Your sentence has {length} word(s)")
for i in (sentence.split(" ")):
    print(len(i), end=" ")
print("characters")
