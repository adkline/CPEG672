import math

def extendgcd(a,b):
        
    if b == 0: 
        return a
    else:
    
        i = 2
        r = []
        r.append(a)
        r.append(b)
        
        q = []
        q.append(0)
        q.append(0)
        
        s = []
        s.append(1)
        s.append(0)
        
        t = []
        t.append(0)
        t.append(1)
        
        
        while r[i-1] != 0:
            
            q.append(r[i-2]/r[i-1])
            r.append(r[i-2]%r[i-1])
 
            s.append(s[i-2]-q[i]*s[i-1])
            t.append(t[i-2]-q[i]*t[i-1])
            
            i = i+1
    found = 0 
    
    for i in range(0, len(r)):    
        if r[i] == 1:
            found = 1
            out = s[i]
    if found == 0: 
        out = 0
    
    return  out


def add(x1,y1,x2,y2,p,a,b):
    temp = extendgcd((x2-x1), p)
    #print temp
    s = ((y2 - y1) * temp)% p
    x3 = (s**2 -x1 -x2)%p
    y3 = (s*(x1-x3)-y1)%p
    G = (x3,y3)
    return G

def double(x1,y1,x2,y2,p,a,b):
    temp = extendgcd((2*y1), p)
   #print temp
    s = ((3*x1**2 + a) * (temp)) % p
    x3 = (s**2 -x1 -x2)%p
    y3 = (s*(x1-x3)-y1)%p
    G = (x3,y3)
    return G

#print extendgcd(19,26)

## compute dp 
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
a = 115792089210356248762697446949407573530086143415290314195533631308867097853948
b = 41058363725152142129326129780047268409114441015993725554835256314039467401291


#ASlice's private

d = 63156948237106975501217193995943213925184252382216001293565541521908637175399

# Bob's Public
P = (111055456197691068259973612553108144258650332885086152727346614469542694563506,99885419492796423079439658813830520578617940818427688692439271159157602726625)

dbin = bin(d)[2:]
print bin(d)[2:]
length=  len(bin(d)[2:])

# Find the identity of P. We take and add Q = P +-P = (x,y) +(x,-y)

Q = (48439561293906451759052585252797914202762949526041747995844080717082404635286,36134250956749795798585127919587881956611106672985015071877198253568414405109)
#Q = P

#Q = (0,0)
#print Q
#find the length, this will be "m"
for i in range(0,length):
    Q = double(Q[0],Q[1],Q[0],Q[1],p,a,b)
    if dbin[i] == 1:
        Q = add(Q[0],Q[1],P[0],P[1],p,a,b)
    print Q
print Q

# N = P
# i = length-2
# while i > 0:
#     if dbin[i] == 1:
#         Q = add(Q[0],Q[1],N[0],N[1],p,a,b)
#     N = double(N[0],N[1],N[0],N[1],p,a,b)
#     i = i-1
#     print Q
# print Q


    