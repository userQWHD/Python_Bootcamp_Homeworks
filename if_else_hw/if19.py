a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))
d = int(input("|d|: "))

if (a == b == d) and (c != b) and (c != d) and (c != a):
    print('different number is:', c)
elif (b == c == d) and (b != a) and (d != a) and (c != a):
    print('different number is:', a)
elif (c == a == d) and (b != c) and (a != b) and (d != b):
    print('different number is:', b)
elif (c == a == b) and (d != c) and (a != d) and (d != b):
    print('different number is:', d)

elif (a == b) and (b == c) and (c == d):
    print('no different numbers here, all the same.')
else:
    print('all numbers are different.')
