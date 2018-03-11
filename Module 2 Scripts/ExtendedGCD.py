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