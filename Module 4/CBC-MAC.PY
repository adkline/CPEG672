import binascii
from Crypto.Cipher import AES


def XOR(raw1, raw2):
  return binascii.unhexlify(format(int(binascii.hexlify(raw1), 16) ^ int(binascii.hexlify(raw2), 16), 'x'))
  
  
IV = '\x00'*16
key = 'andy love simone'

Message = 'andy love simoneandy love simone'

H0 = IV

cipher = AES.new(key, AES.MODE_CBC, IV)


step1 = cipher.encrypt(Message[:16])
print step1

#######now we have to reinitialize this with the IV, then encrypt the previous step XORed with the new 
### stuff. 

print XOR(step1, Message[16:32])

cipher = AES.new(key, AES.MODE_CBC, IV)

MAC = cipher.encrypt(XOR(step1, Message[16:32]))
print MAC

print binascii.hexlify(MAC)