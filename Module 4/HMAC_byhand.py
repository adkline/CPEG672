import binascii, hashlib

k = '93e7402cb2b1b594670e656a6ca4ef247231ac09b7cce194d76e3919e4b072aa'
msg = 'cb2a072d74a5749481030ee46edce28c471ef412c8a4814ac40b87cbc3c188a3ef5e8a4a313862d59731326cf9d431fedca1aa3396a448a3b34d9045987baf2a66da766b216fa36012716212695b13f3273f4ecd3b5d24f9ebf4a8d17658af67f845d3788d73be9bb96aa5be089812d3f1a1e7c700f6a0b435a9d857a7800ec4'

kplus = k + "\x00"*(64-len(k))
ipad = "\x36"*64
opad = "\x5C"*64

print len(k)
print len(kplus)
print "\x00"
print ipad
print opad

def XOR(raw1, raw2):
  return binascii.unhexlify(format(int(binascii.hexlify(raw1), 16) ^ int(binascii.hexlify(raw2), 16), 'x'))

tag = hashlib.sha256(XOR(kplus, opad) + hashlib.sha256(XOR(kplus, ipad) + msg).digest()).digest()

print binascii.hexlify(tag)