a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

if(a < b < c):
    a2 = a 
    b2 = b
    c2 = c

    a2 *= 2
    b2 *= 2
    c2 *= 2
    print('a:', a2)
    print('b:', b2)
    print('c:', c2)
else:
    a2 = b
    b2 = c
    c2 = a
    print('a:', b2)
    print('b:', c2)
    print('c:', a2)