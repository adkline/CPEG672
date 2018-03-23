#import pycrypto
from Crypto.PublicKey import ECC

key = ECC.generate(curve='secp256r1')

print 'The entire key stuff for Alice is', key 
print '\n'

f = open('myprivatekey.pem', 'wt')
f.write(key.export_key(format='PEM'))
f.close()

f = open('Apublic.pem','wt')
Alicepub= key.public_key()
f.write(Alicepub.export_key(format='PEM'))
f.close()
print Alicepub
#key = ECC.import_key(f.read())
f = open('Apublic.pem','rt')
Alicepub= ECC.import_key(f.read())
print Alicepub

### Create BOB stuff

key = ECC.generate(curve='secp256r1')
print '\n'
print 'The entire stuff for Bob is', key 
print '\n'

f = open('myprivatekey.pem', 'wt')
f.write(key.export_key(format='PEM'))
f.close()

f = open('Bpublic.pem','wt')
Bobpub= key.public_key()
f.write(Bobpub.export_key(format='PEM'))
f.close()
print Bobpub
#key = ECC.import_key(f.read())
f = open('Bpublic.pem','rt')
Bobpub= ECC.import_key(f.read())
print Bobpub