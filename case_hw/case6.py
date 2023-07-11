# Offf, I solved this problem like "If Else"
 

print('The units of length ↓ \n\n1 = decimeter\n2 = kilometer\n3 = meter\n4 = millimeter\n5 = centimeter')
n = int(input('enter the operation number [1-5] -> '))
l = int(input('enter the length -> '))
if (n > 4) or (n < 1):
    print('Remember ↓ \n\n1 = decimeter\n2 = kilometer\n3 = meter\n4 = millimeter\n5 = centimeter')

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

print(f'Result: {result} meter.')