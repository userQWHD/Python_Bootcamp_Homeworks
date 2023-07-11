month = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December'
}

q = int(input('[1-12] Month number -> '))
if q in range(1,13):
    print('Month -> ', month[q].capitalize())
else:
    print('Month -> Donkey Month.')
