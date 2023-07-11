print("Remember -> you must enter three-digit integer!")

td_i = int(input("||: "))

one = td_i % 10
ten = (td_i // 10) % 10
hundred = td_i // 100

sum = hundred + ten +one 
prod = hundred * ten * one

print("sum: ", sum)
print("product: ", prod)
