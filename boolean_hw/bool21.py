a = int(input("|a|: "))

ones = a % 10
tens = (a // 10) % 10
hundreds = a // 100

q = (hundreds < tens < ones) 

print("Result: ", q)