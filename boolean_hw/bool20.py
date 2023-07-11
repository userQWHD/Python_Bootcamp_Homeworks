a = int(input("|a|: "))

ones = a % 10
tens = (a // 10) % 10
hundreds = a // 100

q = (hundreds != tens != ones) and (tens != hundreds != ones) 

print("Result: ", q)

print("Alternative ↓")

a = int(input("|a|: "))

hundredss = (a // 100)
tenss = (a - hundredss*100) / 10
oness = (a % 10)
sum =(oness!=tenss and oness!=hundredss and oness!=hundredss)

print(sum)
