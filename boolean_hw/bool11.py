print("Remember -> you must enter odd integer(s)!")

a = int(input("|a|: "))
b = int(input("|b|: "))
q = (a % 2 == 1 and b % 2 == 1 or b % 2 == 0 and a % 2 == 0)

print("result: ", q)

print("Alternative ↓")

a = int(input("|a|: "))
b = int(input("|b|: "))

q = (a % 2 == 1 and b % 2 == 1)
w = (a % 2 == 0 and b % 2 == 0)

e = (q!=w)

print("alternative result: ", e)
