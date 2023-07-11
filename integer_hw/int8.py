print("Remember -> you must enter two-digit integer!")

td_i = int(input("||: "))

ten = td_i // 10
one = td_i % 10
r = one * 10 + ten

print("replaced: ", r)
