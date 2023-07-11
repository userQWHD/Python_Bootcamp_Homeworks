print("Remember -> you must enter three-digit integer!")

td_i = int(input("||: "))

one = td_i % 10
ten = (td_i // 10) % 10
hundred = td_i // 100

r = (ten * 100) + (hundred * 10) + (one*1)
print(r)
