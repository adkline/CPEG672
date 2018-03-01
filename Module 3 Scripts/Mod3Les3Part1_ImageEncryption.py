import urllib, urllib2, requests, os, binascii
import hashlib
from PIL import Image
from Crypto import Random
from Crypto.Cipher import AES



url = 'http://vip.udel.edu/crypto/heckert_gnu.png'

urllib.urlretrieve(url, "heckert_gnu.png")

im = Image.open('heckert_gnu.png')

image_info = [im.tostring(), im.size, im.mode]

#print image_info

password = hashlib.sha256("tonysimage").digest()


print 'the password using sha 256 is ', password
print 'with a length of ', len(password)


IV = binascii.hexlify(os.urandom(32))

print 'The IV is ', IV
print 'With a length of ', len(IV)

cipher = AES.new(password, AES.MODE_ECB, IV)

enc_image = cipher.encrypt(image_info[0])

#print enc_image

Image.frombytes(image_info[2], image_info[1], enc_image).save('output.png')