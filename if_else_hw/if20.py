
a = int(input("|a|: "))
b = int(input("|b|: "))
c = int(input("|c|: "))

ab = abs(a-b)
ac = abs(a-c)

if ab < ac:
    print(f'---------------------------------\nB is closer to A than C\n\nDistance: {ab}\n---------------------------------')
else:
    print(f'---------------------------------\nC is closer to A than B\n\nDistance: {ac}\n---------------------------------')
