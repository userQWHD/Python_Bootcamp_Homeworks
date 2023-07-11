print('The Arithmetic Operations ↓ \n\n1 = addition\n2 = subtraction\n3 = multiplication\n4 = division\n')
on = int(input('enter the operation number [1-4] -> '))
if (on > 4) or (on < 1):
    print('Remember ↓ \n\n1 = addition\n2 = subtraction\n3 = multiplication\n4 = division\n')
fn = int(input('enter the first number -> '))
sn = int(input('enter the second number -> '))

result = 0

if on == 1:
    result = fn + sn
elif on == 2:
    result = fn - sn
elif on == 3:
    result = fn * sn
elif on == 4:
    result = fn / sn
else:
    print('error...')

print('Result: ', result)