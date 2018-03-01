import hmac, hashlib, binascii

message = 'e0eff00f3c46e96c8d5bd181283e4605348e3fa10b47945de3dcc159ae86e7bd3fdb13f2ada2c313fce6a69efa49a470689b1ef05aab778ae15dd35fe6fd1e3a59d351c68cf8f0ffd968d7e78b57377afcc9dce3fa5db1f06f6985c4414c0fcc780030f49fef791a6c08edc2a311080c373f00e4b2044a79d82860f0871bc259'

print len(message)
# message = message[:10]
# print len(message)
# print message

#key ='6f35628d65813435534b5d67fbdb54cb'
#key = '6f35628d65813435'

key = '17b52858e3e135be4440d7df0ca996f41ccb78b7d8cc1924d830fe81e0fd279c131ce3546303e95a'
#key = key[:20]

print binascii.unhexlify(key)
print binascii.unhexlify(message)


######### WHen performing this, we must unhexlify we don't want the hex digest going into the HMAC function!@!
print hmac.new(binascii.unhexlify(key), binascii.unhexlify(message),  hashlib.sha256).hexdigest()


print hmac.new("secretkey", "forge this punks", hashlib.sha256).hexdigest()