print("Remember -> you must enter odd integer(s)!")

a = int(input("|a|: "))
b = int(input("|b|: "))
q = (a % 2 == 1)
w = (b % 2 == 1)

print("a: ", q)
print("b: ", w)

print("Alternative ↓")

a = int(input("|a|: "))
b = int(input("|b|: "))
q = (a  % 2 == 1 and b  % 2 == 1)

print("result: ", q)
