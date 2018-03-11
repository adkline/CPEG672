import math, binascii, urllib
import hashlib
from PIL import Image
from Crypto import Random
from Crypto.Cipher import AES


block_size = 16
key= 'isitbeerthirty?'

key_len = len(key)
key_pad = key

while len(key_pad) <  block_size:
    key_pad = key_pad + '?'
    
if len(key_pad) > block_size:
    key_pad = key_pad[:block_size]
    
print len(key_pad)
print key_pad

IVphrase = 'StartingText'

while len(IVphrase) <  block_size:
    IVphrase = IVphrase + '0'
    
if len(IVphrase) > block_size:
    IVphrase = IVphrase[:block_size]

IVphrase_hex = binascii.hexlify(IVphrase)

ctr1 = str(int((hashlib.sha224(IVphrase_hex[:16]).hexdigest()),16)^int((hashlib.sha224(IVphrase_hex[16:32]).hexdigest()),16))
cntr = ctr1[:16]

outputcounters = file('output.txt', 'w')

def tonycount():
    global cntr
    temp_hash = str (hashlib.sha224(cntr).hexdigest())
    cntr = str(int(cntr,16)^int(temp_hash,16))[:16]
    outputcounters.write(cntr)
    outputcounters.write('\n')
    return cntr
    
cipher = AES.new(key_pad, AES.MODE_CTR, counter=tonycount)
im = Image.open('Beer.png')
image_info = [im.tostring(), im.size, im.mode]
enc_image = cipher.encrypt(image_info[0])
#print enc_image
Image.frombytes(image_info[2], image_info[1], enc_image).save('secret.png')
###Decrypt the image

ctr1 = str(int((hashlib.sha224(IVphrase_hex[:16]).hexdigest()),16)^int((hashlib.sha224(IVphrase_hex[16:32]).hexdigest()),16))

#print decrypting


cntr = ctr1[:16]

cipher = AES.new(key_pad, AES.MODE_CTR, counter=tonycount)
url = 'https://d1b10bmlvqabco.cloudfront.net/attach/jd4nzowqhkh3ja/j6xsx91dyga1ke/jebi7ibf6f5h/secret.png'

urllib.urlretrieve(url, "test.png")
im = Image.open('test.png')
image_info = [im.tostring(), im.size, im.mode]

dec_image = cipher.encrypt(image_info[0])

#print enc_image

Image.frombytes(image_info[2], image_info[1], dec_image).save('decrypt.png')

