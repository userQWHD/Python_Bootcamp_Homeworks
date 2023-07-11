a = float(input("Give a value for 'a': "))
b = float(input("Give a value for 'b': "))
c = float(input("Give a value for 'c': "))


d = a
e = d
a = b
b = c
c = e

print("A value is: ", a)
print("B value is: ", b)
print("C value is: ", c)

