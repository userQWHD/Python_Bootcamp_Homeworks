print("Remember -> you must enter an integer  1 - 365 and 0-7!")

k = (int(input("|k|: ")))
n = (int(input("|n|: ")))

q = ((k-1) + (n-1)) % 7 + 1

print(f"The {k}-th day of the year falls on day number {q}")

