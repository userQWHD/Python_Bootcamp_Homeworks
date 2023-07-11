x = float(input("Enter the value of x: "))

if x <= 0:
    result = -x
elif 0 < x < 2:
    result = x ** 2
else:
    result = 4

print("The value of f(x) is:", result)