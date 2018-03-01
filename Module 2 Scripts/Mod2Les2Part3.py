import math

def gcd_extend(a,b):
    if b == 0:
        return a
        
    else:
        i = 2
        
        #set up some arrays
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
        
        print r[0]
        while  r[i-1] > 0:
            
            print r[i-1]/r[i-2]
            q.append(r[i-1]/r[i-2])
            r.append(r[i-1]%r[i-2])
            
            s.append(s[i-2]-q[i-1]*s[i-1])
            t.append(t[i-2]-q[i-1]*t[i-1])
            
            print ' here is stuff after '
            print r
            print q
            print s
            print t
            print q
            
            i = i+1
        
        return  (r[i-1], s, t )

print gcd_extend(240, 46)