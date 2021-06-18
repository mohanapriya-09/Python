def encode(sen,padding):
    new =''
    length = len(sen)
    if(length < padding):
        mult = padding - length
        value ='0'
        new = value*mult
    for i in sen.split(" "):
        new = new + i.capitalize() + " "
    return new



sen = input()
padding = int(input())
sen = encode(sen,padding)
print(sen)
