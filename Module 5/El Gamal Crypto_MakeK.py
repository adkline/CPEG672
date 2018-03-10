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


a = 22552976422029838320875424094738648769713666765137934057417100959077115625606567084907185210208881763384529113716061147552289656242459647800324625745596833863949313725211871106713783733707586249196695347636081372434710190467930470812040700165975742375757976803094767252749574097888163171872446657793482377783


B = 160755097558399418084545451142594262297110587564422719495044637697418471031120843485272546396503262945374606743483663005592046280570113428041057301416160635682362952726059981032556915079748632809630924911701637494328194126801231552565775064334470258159857294155486978663470872866805557373247692044844139421052

C = 27719699985236574639360861744739361939821131420699575640147828294800411537468758657061984340746460480550729354622071695590590684349658282675679235937734764895189227189828401736789479203534367101740202351476108308803592324811634923356445911705392890384695975336151781664712110548882950142575224299480628315538

K = pow(B, a, p)


print "K, my secret key is ", K

K_inv = extendgcd(K,p)

#m = "my message to be made into ciphertext should be easy hopefully!"

#m_asint = int(binascii.hexlify(m),16)

#C = (m_asint*K)%p

m = (C*K_inv)%p
#print m

Decyrpt = binascii.unhexlify(hex(m)[2:-1])
print Decyrpt

message_to_encrypt = '1123581321345589144'

mes_ashex = binascii.hexlify(message_to_encrypt)

cipher = (int(mes_ashex,16)*K)%p

print "The cipher text should be: ", cipher

print "Decrypting should be ", binascii.unhexlify(hex((cipher*K_inv)%p)[2:-1])