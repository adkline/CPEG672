import binascii, re

text = file('RSA_text', 'r')
string = text.read()

### Work on finding the modulus
begin_modulus = re.search('modulus:', string)
end_modulus = re.search('publicExponent', string)

pos1 = int(begin_modulus.end())
pos2 = int(end_modulus.start())

mod =  string[pos1:pos2]
linebreaks = re.subn('\n', '', mod)[0]
spaces = re.subn(' ', '', linebreaks)[0]
colon = re.subn(':', '', spaces)[0]

mod_ashex = colon
mod_asint = int(mod_ashex,16)

print "The modulus as hex is " , mod_ashex
print '\n'
print "The modulus as int is " , mod_asint
print '\n'

### Now work on the public key. 


begin_prub = re.search('publicExponent:', string)
end_pub = re.search('privateExponent:', string)

pos1 = int(begin_prub.end())
pos2 = int(end_pub.start())



pub =  string[pos1:pos2]
remove_end = int(re.search('\(', pub).start())
pub = pub[:remove_end]

linebreaks = re.subn('\n', '', pub)[0]
spaces = re.subn(' ', '', linebreaks)[0]
colon = re.subn(':', '', spaces)[0]

print "The public key as int is " , colon
print '\n'

### Now work on the private key. 


begin_priv = re.search('privateExponent:', string)
end_priv = re.search('prime1', string)

pos1 = int(begin_priv.end())
pos2 = int(end_priv.start())

priv =  string[pos1:pos2]
linebreaks = re.subn('\n', '', priv)[0]
spaces = re.subn(' ', '', linebreaks)[0]
colon = re.subn(':', '', spaces)[0]

priv_ashex = colon
priv_asint = int(priv_ashex,16)

print "The private key as hex is " , priv_ashex
print '\n'
print "The private key as int is " , priv_asint
print '\n'




# print "Private as hex is " , priv_ashex
# print "Private as int is"  , priv_int
# print "Your key pair is  (", mod_asint, "," , public, ')'



# #### To encrypt

# M = "Have a great weekend"

# M_ashex = binascii.hexlify(M)
# M_asint = int(M_ashex,16)

# C = pow(M_asint, 65537, 93339945660270539362035014539643567593237643039465143261515213817)
# #C = pow(M_asint,public, mod_asint)

# print "Using the public key, I've encrypted ",  C

# ### Decrypting

# piazzaC  = int('82687178927585845614796337538285152927922992193064853353669883238')

# # Using the below you may need to paddddd.

# Decyrpt = binascii.unhexlify(hex(pow(piazzaC,priv_int,mod_asint))[2:-1])

# print Decyrpt


# # m1_asbin = bin(Decyrpt_asint)[2:]
# # ## COnvert back. Take convert int to binary, then take each byte and convert to hex. put into string
# # ## Pad the front 
# # while len(m1_asbin)% 8 != 0:
# #     m1_asbin = '0' + m1_asbin
# # m1_backtext =''
# # # Take each byte and convert to int, then hexlify, then put in string.
# # #for i in range(0,len(m1_asbin),8):
# #  #   tempint = int(m1_asbin[i:i+8],2)
# #   #  temphex = hex(tempint)[2:]
# #   #  m1_backtext = m1_backtext + binascii.unhexlify(str(temphex))
# # print m1_backtext



