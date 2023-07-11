v1_x = int(input("Enter the x coordinate of vertex 1: "))
v1_y = int(input("Enter the y coordinate of vertex 1: "))
v2_x = int(input("Enter the x coordinate of vertex 2: "))
v2_y = int(input("Enter the y coordinate of vertex 2: "))
v3_x = int(input("Enter the x coordinate of vertex 3: "))
v3_y = int(input("Enter the y coordinate of vertex 3: "))

if v1_x == v2_x:
    x4 = v3_x
elif v1_x == v3_x:
    x4 = v2_x
else:
    x4 = v1_x

if v1_y == v2_y:
    y4 = v3_y
elif v1_y == v3_y:
    y4 = v2_y
else:
    y4 = v1_y

# Print the coordinates of the fourth vertex
print("The coordinates of the fourth vertex are: ({}, {})".format(x4, y4))