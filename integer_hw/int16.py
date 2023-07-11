print("Remember -> you must enter three-digit integer!")

td_i = int(input("||: "))

ten = td_i % 10
one = (td_i // 10) % 10
hundred = td_i // 100

r = (hundred * 100) + (ten * 10) + (one*1)
print('replaced ->', r)
