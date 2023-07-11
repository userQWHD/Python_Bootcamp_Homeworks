print("Remember -> you must enter three-digit integer!")

td_i = int(input("||: "))

one = td_i % 10
ten = (td_i // 10) % 10
hundred = td_i // 100

r = (one * 100) + (ten * 10) + (hundred*1)
print(r)
