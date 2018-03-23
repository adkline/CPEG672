from Crypto.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Crypto.Random import get_random_bytes



def encrypt_GCM(data, key):
    #data = "a message to encrypt"
    #key = get_random_bytes(16)
    #Must make a new nonce each time!
    nonce = get_random_bytes(16)
    #print "The Nonce is", nonce, "\n" 
    cipher = AES.new(key, AES.MODE_GCM, nonce = nonce)
    ciphertext = cipher.encrypt(data)
    #print "Outputs ciphertext: " , ciphertext
    return (ciphertext, nonce)

def decrypt_GCM(cipher, key, nonce):
    #data = "a message to encrypt"
    #key = get_random_bytes(16)
    #Must make a new nonce each time!
    nonce = get_random_bytes(16)
    #print "The Nonce is", nonce, "\n" 
    # print "Outputs ciphertext: " , ciphertext
    decipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = decipher.decrypt(ciphertext)
    return (plaintext)



#file_out = open("encrypted.bin", "wb")
#[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]