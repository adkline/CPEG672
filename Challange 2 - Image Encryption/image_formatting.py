import math, binascii, urllib
import hashlib
from PIL import Image
from Crypto import Random
from Crypto.Cipher import AES

#text_name = raw_input("Type the name of the file to encrypt with the extension: ")
text_name = '128.BMP'


im = Image.open(text_name)
image_info = [im.tostring(), im.size, im.mode]

#image_info[2] = 'P'

print im.mode
print im.info
print im.format
print im.tostring()


#text_name = 'encrypted_ECB.bmp'
text_name = 'decrypted_ECB.png'

iv = Random.new().read(AES.block_size)
im = Image.open(text_name)
image_info = [im.tostring(), im.size, im.mode]

converted = im.convert('RGB')

print converted.mode
print converted.info
print converted.format
print converted.tostring()

Image.frombytes(converted.mode, converted.size, converted.tostring()).save("test.bmp")

converted.show()

text_name = 'test.bmp'
print "File open is ", text_name 

iv = Random.new().read(AES.block_size)
im = Image.open(text_name)
image_info = [im.tostring(), im.size, im.mode]

#image_info[2] = 'P'

print im.mode
print im.info
print im.format
print im.tostring()


#cipher = AES.new(key_pad, AES.MODE_ECB)