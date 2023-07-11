print("Remember -> you must enter two even integer(s)!")

a = (int(input("|a|: ")))

w = (a // 10)
q = (a % 2 == 0 and w % 2 == 0 and 10 <= a <= 99) 

print("Result: ",q)