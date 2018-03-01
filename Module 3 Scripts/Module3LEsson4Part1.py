import os, math, binascii
from Crypto.Cipher import AES
from Crypto.Util import Counter

plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

key = 'andy love simone'
IV = 'Not very random.'

cipher = AES.new(key, AES.MODE_OFB, IV)


ciphertext = cipher.encrypt(plain)

print binascii.hexlify(ciphertext)




cipherCTR = AES.new(key, AES.MODE_CTR, counter = Counter.new(128, initial_value = int(binascii.hexlify('Not very random.'), 16)))


cipherout = cipherCTR.encrypt(plain)

print binascii.hexlify(cipherout)