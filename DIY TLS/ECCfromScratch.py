import math, random
from Crypto.Util.number import *

def add(x1,y1,x2,y2,p,a,b):
    s = ((y2 - y1) * inverse((x2-x1), p))%p
    x3 = (s**2 -x1 -x2)%p
    y3 = (s*(x1-x3)-y1)%p
    G = (x3,y3)
    return G

def double(x1,y1,x2,y2,p,a,b):
    s = ((3*x1**2 + a) * inverse((2*y1), p)) %p
    x3 = (s**2 -x1 -x2)%p
    y3 = (s*(x1-x3)-y1)%p
    G = (x3,y3)
    return G

#USing P-256 Curve Parameters
## compute dp 
def generate_priv_pub():
    p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    a = 115792089210356248762697446949407573530086143415290314195533631308867097853948
    b = 41058363725152142129326129780047268409114441015993725554835256314039467401291
    G = (48439561293906451759052585252797914202762949526041747995844080717082404635286,36134250956749795798585127919587881956611106672985015071877198253568414405109)
    N = 115792089210356248762697446949407573529996955224135760342422259061068512044369

    d = getRandomRange(2, p-2) 
    while GCD(d,p-1) !=1:
        d = getRandomRange(2,p-2) 
    dbin = bin(d)[2:]
    length=  len(bin(d)[2:])
    P = G
    Q = G
    #find the length, this will be "m"
    i = 0
    for i in range(1,length):
        #print "For i equal ", i
        #print "The bin values is ", dbin[i]
        Q = double(Q[0],Q[1],Q[0],Q[1],p,a,b)
       # print "Double Q equals", Q
        if dbin[i] == '1':
            Q = add(Q[0],Q[1],P[0],P[1],p,a,b)
            #print "Add Q and P equals", Q
        #print "\n"
    return(Q[0],Q[1],d)    

def generate_shared(pub_x1,pub_x2,priv):
    p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    a = 115792089210356248762697446949407573530086143415290314195533631308867097853948
    b = 41058363725152142129326129780047268409114441015993725554835256314039467401291
    G = (pub_x1,pub_x2)
    N = 115792089210356248762697446949407573529996955224135760342422259061068512044369
    d = priv
    dbin = bin(d)[2:]
    length=  len(bin(d)[2:])
    P = G
    Q = G
    #find the length, this will be "m"
    i = 0
    for i in range(1,length):
        #print "For i equal ", i
        #print "The bin values is ", dbin[i]
        Q = double(Q[0],Q[1],Q[0],Q[1],p,a,b)
       # print "Double Q equals", Q
        if dbin[i] == '1':
            Q = add(Q[0],Q[1],P[0],P[1],p,a,b)
            #print "Add Q and P equals", Q
        #print "\n"
    return(Q[0],Q[1])   

Alice = generate_priv_pub()    
print "Alice's keys are", Alice, "\n"

Bob = generate_priv_pub()    
print "Bob's keys are", Bob, "\n"

shared = generate_shared(Alice[0],Alice[1],Bob[2])

print "The shared key is", shared, "\n"