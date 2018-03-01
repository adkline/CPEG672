import os, binascii, math, hashlib

Plaintext = "Andy ROX!"

key = os.urandom(9)

PlainHex = binascii.hexlify(Plaintext)
PlainInt = int(PlainHex,16)
PlainBin = bin(PlainInt)

print "The plain text in Hex is", PlainHex

KeyHex = binascii.hexlify(key)
KeyInt = int(KeyHex,16)
KeyBin = bin(KeyInt)

print "Your key in Hex is", KeyHex

Encrypted = PlainInt ^ KeyInt
EncryptedHex = hex(Encrypted)
EnryptedBin = bin(Encrypted)

print "The encrypted message is ", EncryptedHex
print "The encrypted message is  in integer form is ",  Encrypted

Decrypted = Encrypted ^ KeyInt

#Create Decrypted in hex form
DecryptedHex = hex(Decrypted)
DecryptedHex = DecryptedHex[2:]

print "The Decrypted message is ", DecryptedHex

# Take this, find the length. If greater than  and remove the L 
#First determine the type. If long, we need to remove the "L" 

if type(Encrypted) is long:
    print 'Encrypted is LONG Type - Removing "L"'
    length_Message = len(DecryptedHex)
    DecryptedHex = DecryptedHex[0:(length_Message-1)]

print 'Decrypting message ' , DecryptedHex
#Calculate the length again. 
length_Message = len(DecryptedHex)

print "The original message is of length ", length_Message

if length_Message > 16:
    shift = 16 - (length_Message%16)
    print "Length over 16, we must pad with ", shift, "spaces at the end"
    #DecryptedHex >> shift
    Padding = ['20'] * shift
    m = 0
    while m < len(Padding):
        DecryptedHex = DecryptedHex + Padding[m]
        m = m+1
        
num_segments = len(DecryptedHex)/16


DecryptedText = ''
i = 0    

while i < num_segments:
    #starting point
    j = i*16
    #
    #DecryptedText.append(binascii.unhexlify(DecryptedHex[j:j+16]))
    DecryptedText = DecryptedText + binascii.unhexlify(DecryptedHex[j:j+16])
    i = i+1
    
print DecryptedText




