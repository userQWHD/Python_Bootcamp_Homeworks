import math

x1 = float(input("Give a value for 'x1': "))
y1 = float(input("Give a value for 'y1': "))
x2 = float(input("Give a value for 'x2': "))
y2 = float(input("Give a value for 'y2': "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance: ", distance)
