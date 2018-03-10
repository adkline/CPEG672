import binascii

m1 = "andy love simone"

m1_ashex = binascii.hexlify(m1)

m1_asint = int(m1_ashex,16)

m1_asbin = bin(m1_asint)[2:]

## COnvert back. Take convert int to binary, then take each byte and convert to hex. put into string

## Pad the front 

while len(m1_asbin)% 8 != 0:
    m1_asbin = '0' + m1_asbin
    

m1_backtext =''
# Take each byte and convert to int, then hexlify, then put in string.
    


for i in range(0,len(m1_asbin),8):
    tempint = int(m1_asbin[i:i+8],2)
    print "As int is ", tempint
    temphex = hex(tempint)[2:]
    print "As hex is" , temphex
   
    m1_backtext = m1_backtext + binascii.unhexlify(str(temphex))
    print m1_backtext
    
    
print m1_backtext