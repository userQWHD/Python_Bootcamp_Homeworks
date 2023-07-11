week = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    7 : 'Sunday'
}

q = int(input('[1-7] -> '))
if q in range(1,8):
    print('Day Of the week: ', week[q].capitalize())
else:
    print('oops, something goes wrong.')


