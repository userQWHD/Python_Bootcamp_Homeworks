print("Remember -> you must enter three positive integers!")

a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

q = a // c
w = b // c

total_squares = q * w
unused_area = a * b - total_squares * (c * c)

print("Number of squares placed on the rectangle:", total_squares)
print("Area of unused part of the rectangle:", unused_area)