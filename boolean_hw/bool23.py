a = int(input("|a|: "))

ones = a % 10
tens = (a // 10) % 10
hundreds = (a // 100) % 10
thousands = a // 1000

q = (thousands == hundreds == tens == ones)\
    or (thousands == ones != hundreds == tens)

print("result: ", q)
