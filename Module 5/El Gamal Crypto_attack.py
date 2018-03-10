from Crypto.Util.number import *
import binascii

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



p = int('E912ECF78A51FC5BBFA26A00E07A0CEC5ECEB897891643DD7DDD8056A51C71124258D52DAEF464B929F6397101F00C67CFC09B3D068B522E1C8B566431936C3A606A47928582F0D8D6B23F9019FF06A900CD5AD97E02CD3DEAA0495C968A2345858C6556623A61124C711DC0708999C08D5A349592F37DFE07A49C0D82241403',16)


g = 2


c1 = 18424891061981125566079466891923819180189054061023814911996244968757009636277781996991198589205553366877632626019687233233562516536979650853205499214249094240900255342184044396745719365913308597675593979310737613720122429835760055805218845303574586686599271581737663333099357124617446774817423136689946166367


m1 = "andy love simone"

m1_ashex = binascii.hexlify(m1)
m1_asint = int(m1_ashex, 16)

print "As hex is ", m1_ashex
print "As int is", m1_asint
#print "Hexlify from int is ", binascii.hexlify(str(m1_asint))

m1_inv = extendgcd(m1_asint, p)

K = (m1_inv*c1) % p

K_inv = extendgcd(K,p)


c2 = 147916986843316695573527469896022062497486746186799547986333428947128110557487364196308461373471989565404856104071324637254647685467504146965165326708794537673201648748801360926219432677374843811543425663953769549430785910736947688203941658591437841781348072102214897713002887676885484302975358896835374731746

m2_asint =  (c2*K_inv)%p

#rint m2_asint



m2_asbin = bin(m2_asint)[2:]

## COnvert back. Take convert int to binary, then take each byte and convert to hex. put into string

## Pad the front 

while len(m2_asbin)% 8 != 0:
    m2_asbin = '0' + m2_asbin
    

m2_backtext =''
# Take each byte and convert to int, then hexlify, then put in string.
    


for i in range(0,len(m2_asbin),8):
    tempint = int(m2_asbin[i:i+8],2)
    #print "As int is ", tempint
    temphex = hex(tempint)[2:]
    #print "As hex is" , temphex
   
    m2_backtext = m2_backtext + binascii.unhexlify(str(temphex))


print m2_backtext
    
