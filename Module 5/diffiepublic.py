from Crypto.Util.number import *


p = getStrongPrime(512)
a = getRandomRange(2, p-2) 
print GCD(a, p-1)

while GCD(b, p-1) != 1:
    a = getRandomRange(2, p-2) 
    
base = 2
A = pow(base, a, p)
print "a is " , a
print " p = " , p
print " g = " , base
print " A = " , A








# a = getRandomRange(2, p-2) 
# print GCD(a, p-1)

# while GCD(a,p-1) != 1:
#     a = getRandomRange(2, p-2) 
#     print GCD(a, p-1)


# base = 2
# B = pow(base, b, p)
# print "b is " , b
# print " p = " , p
# print " g = " , base
# print " B = " , B

# #K = pow(A, b, p)

# print "K is = " ,  K