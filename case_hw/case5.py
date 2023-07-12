operations = {
    1: 'addition',
    2: 'subtraction',
    3: 'multiplication',
    4: 'division'
}

print('The Arithmetic Operations ↓ \n\n1 = addition\n2 = subtraction\n3 = multiplication\n4 = division\n')
on = int(input('Enter the operation number [1-4]: '))

if on not in operations:
    print('Sorry about that but this calculator has only 4 operations and I was shown you at the beginning.')
else:
    try:
        a = float(input('enter the first number -> '))
        b = float(input('enter the second number -> '))

        result = 0
        
        if on == 1:
            result = a + b
        elif on == 2:
            result = a - b
        elif on == 3:
            result = a * b
        elif on == 4:
            result = a / b
        else:
            print('Error: division by zero is not allowd.')
        print(f'Result of {operations[on]}: {result:.2f} ') # {result:.2f} -daky .2f result-da cykyan sanyn 'decimal'-laryny 
    except ValueError:                                    # gorkezya(islesem 2f dalde 3f 4f hem edip bilyan) f hem float diymek bolya 
        print('Error: Invalid input. Please enter valid numbers.')
