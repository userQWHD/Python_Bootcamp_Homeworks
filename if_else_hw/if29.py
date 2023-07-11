q = int(input('Enter an integer(s) -> '))

if q < 0 and q % 2 ==0:
    print(q, 'is negative even number.')    
elif q < 0 and q % 2 != 0:
    print(q, 'is negative odd number.')    
elif q > 0 and q % 2 ==0:
    print(q, 'is positive even number.')    
elif q > 0 and q % 2 !=0:
    print(q, 'is positive odd number.')    
else: 
    print(q, 'is nothing.')