print("Remember -> you must enter four-digits or more than integer!")

fd_i = int(input("||: "))

q = (fd_i // 1000) % 100

print("thousands: ", q)