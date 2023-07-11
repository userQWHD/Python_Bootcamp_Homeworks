a=int(input("|a|:"))
b=int(input("|b|:"))
c=int(input("|c|:"))

q = (a*a + b*b == c*c) or (b*b + c*c == a*a) or (a*a + c*c == b*b)

print("Result: ", q)
