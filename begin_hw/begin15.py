import math

S = float(input("Enter the area of the circle: "))

D = math.sqrt((4 * S) / math.pi)

L = math.pi * D

print("The diameter of the circle is:", D)
print("The length of the circumference is:", L)