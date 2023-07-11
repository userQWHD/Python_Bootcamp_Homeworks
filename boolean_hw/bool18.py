print("Remember -> you must enter integers there is at least one pair of equal ones!")

a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

q = a == b or b == c or c  == a

print("result: ",q)