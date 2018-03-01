import math


imax = 5
seed = 3

a = 1103515245
c = 12345
m =2**31

rold = seed
for i in range(0, imax):

    rnew = (a*rold + c)%m
    
    print rnew
    
    rold = rnew
    
    

r1 = 300562173

rem = 1
while rem != 0:
    mult = 0
    
    Rseed = ((m)*(mult)+ (r1-c))/a
    
    rem = ((m)*(mult)+ (r1-c))%a
    
    print rem
    mult += 1
    
print Rseed