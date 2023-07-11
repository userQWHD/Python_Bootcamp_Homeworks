a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

if (a < c < b) or (a < b < c):
    print(f'{a} is minimum.')
elif(b < c < a) or (b < a < c):
    print(f'{b} is minimum.')
elif(c < a < b) or (c < b < a):
    print(f'{c} is minimum.')

if (a > c > b) or (a > b > c):
    print(f'{a} is maximum.')
elif(b > c > a) or (b > a > c):
    print(f'{b} is maximum.')
elif(c > a > b) or (c > b > a):
    print(f'{c} is maximum.')