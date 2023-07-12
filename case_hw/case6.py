q = {
    1: 'addition',
    2: 'subtraction',
    3: 'multiplication',
    4: 'division'
}

print('The units of length ↓ \n\n1 = decimeter\n2 = kilometer\n3 = meter\n4 = millimeter\n5 = centimeter')
n = int(input('enter the operation number [1-5] -> '))
if n not in q:
    print('PLEASE TRY AGAIN.')

else:
    try:
        
        l = float(input('enter the length -> '))
        
        result = 0

        if n == 1:
            result = l / 10
        elif n == 2:
            result = l * 1000
        elif n == 3:
            result = l
        elif n == 4:
            result = l / 1000
        elif n == 5:
            result = l / 100
        else:
            print('error...')
        print(f'Result of {q[n]}: {result:.2f} meter.')
    except ValueError:
        print('Error: Invalid input. Please enter valid numbers.')
