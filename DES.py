from Crypto.Cipher import DES
import binascii
scheme = DES.new('smnsdddy', DES.MODE_ECB)
ciphertext = scheme.encrypt('testnote')

#ciphertext = '7a689d7aa98bd217'

print binascii.hexlify(ciphertext)

cipher = binascii.hexlify(ciphertext)

cipher_unhex = binascii.unhexlify(cipher)

decrypted = scheme.decrypt(cipher_unhex)

print decrypted
#cipher_as_hex = binascii.hexlify(ciphertext)

# Decrypted = scheme.decrypt(ciphertext)

# print binascii.hexlify(Decrypted)

# num_segments = len(Decrypted)/16

# DecryptedText = ''
# i = 0    

# while i <= num_segments:
#      #starting point
#     j = i*16
#     #
#     #DecryptedText.append(binascii.unhexlify(DecryptedHex[j:j+16]))
#     DecryptedText = DecryptedText + binascii.hexlify(Decrypted[j:j+16])
#     i = i+1
    
# print DecryptedText
