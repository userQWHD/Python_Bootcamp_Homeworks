a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

if (a < b < c) or (a < c < b):
    print(f'{a} is smaller than others')
elif(b < a < c) or (b < c < a):
    print(f'{b} is smaller than others')
elif(c < b < a) or (c < a < b):
    print(f'{c} is smaller than others')