print("Remember -> you must enter three-digit integer!")

td_i = int(input("||: "))

one = td_i % 10
ten = td_i // 10
r = one * 100 + ten 


print("replaced: ", r)
