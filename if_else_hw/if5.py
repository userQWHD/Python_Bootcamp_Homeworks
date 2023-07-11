a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

q = 0
w = 0
if a > 0:
    q+=1
else:
    w+=1
##############
if b > 0:
    q+=1
else:
    w+=1
#############
if c > 0:
    q+=1
else:
    w+=1
    
print('positive integer(s):', q)
print('negative integer(s):', w)