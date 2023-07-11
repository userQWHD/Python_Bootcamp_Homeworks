a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

q = 0

if a > 0:
    q+=1
elif a < 0:
    q-=1
if b > 0:
    q+=1
elif a < 0:
    q-=1
if c > 0:
    q+=1
elif a < 0:
    q-=1
    
print(q)