print("Remember -> you must enter two positive integer(s)!")

a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

q = (a > 0 and b > 0 and c < 0) or (b > 0 and a >
                                    0 and c < 0) or (c > 0 and b > 0 and a < 0)
print("result: ", q)

print("Alternative ↓")

a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

q = a > 0
w = b > 0
e = c > 0

r = (q and w and not e) or (w and q and not e) or (e and w and not q)

print("alternative result: ", r)
