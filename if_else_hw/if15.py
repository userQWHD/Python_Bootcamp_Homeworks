a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

if (a >= b) and (a >= c):
    if (b >= c):
        q = a + b
    else:
        q = a + c
elif (b >= a) and (b >= c):
    if (a >= c):
        q = b + a
    else:
        q = b + c
else:
    if (a >= b):
        q = c + a
    else:
        q = c + b

print('Sum of the two largest numbers: ', q)