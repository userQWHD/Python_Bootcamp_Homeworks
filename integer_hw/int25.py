print("Remember -> you must enter an integer from 1 to 365!")

k = (int(input("|k|: ")))

q = (k + 3) % 7  

print(f"The {k}-th day of the year falls on day number {q}")