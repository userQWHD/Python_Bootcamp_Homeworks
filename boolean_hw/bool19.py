print("Remember -> you must enter integers there is at least one pair of opposite ones!")

a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

q = (a < 0 and b > 0) or (a > 0 and b < 0) or (b < 0 and c > 0) or (
    b > 0 and c < 0) or (c < 0 and a > 0) or (c > 0 and a < 0)
print("result: ", q)
