month = int(input("Enter the number of the month [1-12] -> "))

days = 0

if month == 2:
    days = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
else:
    days = 31

print(f"The month number {month} has {days} days.")