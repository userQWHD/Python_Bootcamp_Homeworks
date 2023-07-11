x1 = float(input("Give a value for 'x1': "))
y1 = float(input("Give a value for 'y1': "))
x2 = float(input("Give a value for 'x2': "))
y2 = float(input("Give a value for 'y2': "))
x3 = float(input("Give a value for 'x3': "))
y3 = float(input("Give a value for 'y3': "))

a = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
b = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5

p = a + b + c

s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c))**0.5

print("Perimeter of the triangle is: ", p)
print("Area of the triangle is: ", area)

