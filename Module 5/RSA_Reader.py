import binascii, re

# text = file('rsa_key', 'r')
# string = text.read()

# begin_prime1 = re.search('prime1:', string)

# print begin_prime1   

modulus = "00:ca:d2:a2:0f:2a:9d:50:7a:c5:b1:f1:53:2b:03:49:b6:73:91:49:cb:69:8f:d7:5e:6a:f8:ab"
mod_ashex = ''

for i in range(0,len(modulus),3):
    #print modulus[i:i+2]
    mod_ashex = mod_ashex + modulus[i:i+2] 
mod_asint = int(mod_ashex,16)

print "Mod as Hex is" , mod_ashex
print "Mod as int is"  , mod_asint
    
######

###C = put cipher int here
###print binascii.unhexlify(hex(pow(C,d,n))[2:-1])

public = 65537

private = "2f:d5:3d:23:16:89:c3:51:31:0e:a6:3b:57:02:d5:69:9b:3a:03:bf:57:2a:45:cc:7c:f6:01"
priv_ashex = ''

for i in range(0,len(private),3):
    #print private[i:i+2]
    
    priv_ashex = priv_ashex + private[i:i+2] 
priv_int = int(priv_ashex,16)

print "Private as hex is " , priv_ashex
print "Private as int is"  , priv_int
print "Your key pair is  (", mod_asint, "," , public, ')'



#### To encrypt

M = "Have a great weekend"

M_ashex = binascii.hexlify(M)
M_asint = int(M_ashex,16)

C = pow(M_asint, 65537, 93339945660270539362035014539643567593237643039465143261515213817)
#C = pow(M_asint,public, mod_asint)

print "Using the public key, I've encrypted ",  C

### Decrypting

piazzaC  = int('82687178927585845614796337538285152927922992193064853353669883238')

# Using the below you may need to paddddd.

Decyrpt = binascii.unhexlify(hex(pow(piazzaC,priv_int,mod_asint))[2:-1])

print Decyrpt


# m1_asbin = bin(Decyrpt_asint)[2:]
# ## COnvert back. Take convert int to binary, then take each byte and convert to hex. put into string
# ## Pad the front 
# while len(m1_asbin)% 8 != 0:
#     m1_asbin = '0' + m1_asbin
# m1_backtext =''
# # Take each byte and convert to int, then hexlify, then put in string.
# #for i in range(0,len(m1_asbin),8):
#  #   tempint = int(m1_asbin[i:i+8],2)
#   #  temphex = hex(tempint)[2:]
#   #  m1_backtext = m1_backtext + binascii.unhexlify(str(temphex))
# print m1_backtext



