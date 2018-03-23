import math, binascii, urllib
import hashlib
from PIL import Image
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter

block_size = 16
key= 'helloworld'

key_len = len(key)
key_pad = key

while len(key_pad) < block_size:
    key_pad = key_pad + '*'
    
if len(key_pad) > block_size:
    key_pad = key_pad[:block_size]
    
print key_pad



# count=0
# def secret():
#     global count
#     count+=10
#     return str(hex(count).split('x')[-1].zfill(AES.block_size))
ctr = Counter.new(128)

#url = 'https://d1b10bmlvqabco.cloudfront.net/attach/jd4nzowqhkh3ja/j6xy2s8imyu2rr/je3nnwlel0y3/output.png'
#urllib.urlretrieve(url, "dwayne.png")
im = Image.open('Beer.png')
image_info = [im.tostring(), im.size, im.mode]
cipher = AES.new(key_pad, AES.MODE_CTR, counter = ctr)
dec_image = cipher.encrypt(image_info[0])
Image.frombytes(image_info[2], image_info[1], dec_image).save('encrypt.png')

