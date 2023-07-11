a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

if (c < a < b) or (c > a > b):
    print(f'{a} between the minimum and the maximum.')
elif(c < b < a) or (c > b > a):
    print(f'{b} between the minimum and the maximum.')
elif(a < c < b) or (a > c > b):
    print(f'{c} between the minimum and the maximum.')