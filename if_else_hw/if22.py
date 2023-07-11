x = float(input("|x|: "))
y = float(input("|y|: "))

if x > 0 and y > 0:
    print('point lies on the first quarter (Q1)')
elif x < 0 and y > 0:
    print('point lies on the second quarter (Q2)')
elif x < 0 and y < 0:
    print('point lies on the third quarter (Q3)')
elif x > 0 and y < 0:
    print('point lies on the fourth quarter (Q4)')


#Just Now time is 22:22
print("""
                ↑
    Q II       5|       Q I
    (-,+)      4|      (+,+)
               3|    
               2|    
               1|  1  2  3  4  5
←———————————————0———————————————→
  -5 -4 -3 -2 -1|-1
                |-2
                |-3
                |-4
    Q III       |-5      Q IV  
    (-,-)       ↓        (+,-)   
""")