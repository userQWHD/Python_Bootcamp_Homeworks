#case 4

month ={
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
q = int(input("Enter the number of the month [1-12] -> "))
days = 0

if q == 2:
    days = 28
    feb_ques = int(input('which year -> '))
    if (feb_ques % 4 == 0) and (feb_ques % 100 != 0 or feb_ques % 400 == 0):
        print(feb_ques, 'is a leap year and February 29 days.')
        days = 29
    else:
        print(feb_ques, 'is not a leap year.', days, 'days.')
    if q == 2:
        print()
    
elif q == 4 or q == 6 or q == 9 or q == 11:
    days = 30
else:
    days = 31 
if q in range(1,13):
    print('Month -> ', month[q].capitalize())
print(f"{month.get(q)} has {days} days.")

