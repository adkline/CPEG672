import math, fractions, random


def eulertot(n):
    count = 0
    i = 0
    while i < n:
        if fractions.gcd(i,n) == 1:
            count +=1
        
        i +=1
    
    return count
    
print eulertot(2147483648)
