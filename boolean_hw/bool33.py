a=int(input("|a|:"))
b=int(input("|b|:"))
c=int(input("|c|:"))

q = (a + b > c) and (b + c > a) and (c + a > b)
print("Result: ", q)
