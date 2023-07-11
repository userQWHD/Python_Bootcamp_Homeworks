from math import sin
x = float(input("Enter the value x: "))

if x > 0:
    result = 2 * sin(x)
else:
    result = 6 - x

print("The value of f(x) is:", result)