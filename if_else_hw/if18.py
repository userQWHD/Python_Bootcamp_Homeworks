a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

if (a == b) and (c != b):
    print('different number is:', c)
elif (b == c) and (b != a):
    print('different number is:', a)
elif (c == a) and (b != c):
    print('different number is:', b)

elif (a == b) and (b == c):
    print('no different numbers here, all the same.')
else:
    print('all numbers are different.')
