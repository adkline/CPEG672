from Crypto.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Crypto.Random import get_random_bytes



def encrypt_GCM(data, key,nonce):
    #data = "a message to encrypt"
    #Must make a new nonce each time!
       #print "The Nonce is", nonce, "\n" 
    cipher = AES.new(key, AES.MODE_GCM, nonce = nonce)
    #cipher = AES.new(key, AES.MODE_GCM)
    ciphertext = cipher.encrypt(data)
    #print "Outputs ciphertext: " , ciphertext
    return (ciphertext, nonce)

def decrypt_GCM(cipher, key,nonce):
    #data = "a message to encrypt"
    #key = get_random_bytes(16)
    #Must make a new nonce each time!
     #print "The Nonce is", nonce, "\n" 
    # print "Outputs ciphertext: " , ciphertext
    decipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    #decipher = AES.new(key, AES.MODE_GCM)
    plaintext = decipher.decrypt(cipher)
    return (plaintext)

nonce = get_random_bytes(16)
key = get_random_bytes(16)
m = "This is a message for Bob"
ciphertext = encrypt_GCM(m,key,nonce)

print ciphertext

deciphered = decrypt_GCM(ciphertext[0], key,nonce)

print deciphered    
