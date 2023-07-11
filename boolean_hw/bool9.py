print("Remember -> you must enter odd integer(s)!")

a = int(input("|a|: "))
b = int(input("|b|: "))
q = (a % 2 == 1 or b % 2 == 1)

print("result: ", q)
