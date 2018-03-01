import binascii
from Crypto.Cipher import AES
import hashlib

key = 'andy love simone'

#key_hex = binascii.hexlify(key)
##
###### If you start with hexidest, you must "unhexlify" to create a hex number of bytes. 
IV = binascii.unhexlify('000102030405060708090a0b0c0d0e0f')

cipher = AES.new(key, AES.MODE_CBC, IV)

msg = cipher.encrypt('abcdefghijklmnopqrstuvwxyzabcdef')

print ' Encrypted is ' , msg
print ' As hexdigest is ' , binascii.hexlify(msg)

#msg_hex = binascii.hexlify(msg)
# print msg_hex

decipher = AES.new(key, AES.MODE_CBC, IV)
decrypted = decipher.decrypt(msg)
print 'Decrypted is ', decrypted

#print binascii.hexlify(decrypted)
