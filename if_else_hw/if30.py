q = int(input('[1 - 999] -> '))

one = q < 10 and q > 0
ten = q > 9 and q < 100
hundred = q > 99 and q < 1000


if q > 0 and q % 2 == 0 and one:
    print(q, 'is one digit even number.')    
elif q > 0 and q % 2 != 0 and one:
    print(q, 'is one digit odd number.')    
elif q >= 10 and q % 2 ==0 and ten:
    print(q, 'is two digit even number.')    
elif q >= 10 and q % 2 !=0 and ten:
    print(q, 'is two digit odd number.')    
elif q >= 100 and q % 2 == 0 and hundred:
    print(q, 'is three digit even number.')    
elif q >= 100 and q % 2 != 0 and hundred:
    print(q, 'is three digit odd number.')
else:
    print('nothing...')
