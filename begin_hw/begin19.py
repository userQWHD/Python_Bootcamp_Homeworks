x1 = float(input("Give a value for 'x1': "))
y1 = float(input("Give a value for 'y1': "))
x2 = float(input("Give a value for 'x2': "))
y2 = float(input("Give a value for 'y2': "))

length = abs(x2-x1)
width = abs(y2-y1)

perimeter = 2 * (length + width)
area = length * width


print("length of the ractangle is: ", length)
print("width of the ractangle is: ", width)
print("perimeter of the ractangle is: ", perimeter)
print("area of the ractangle is: ", area)
