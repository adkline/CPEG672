import socket, random, binascii, math, re, hashlib, base64
from Crypto.PublicKey import RSA
from Crypto.Util.number import *

from Crypto.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Crypto.Random import get_random_bytes



def add(x1,y1,x2,y2,p,a,b):
    s = ((y2 - y1) * inverse((x2-x1), p))%p
    x3 = (s**2 -x1 -x2)%p
    y3 = (s*(x1-x3)-y1)%p
    G = (x3,y3)
    return G

def double(x1,y1,x2,y2,p,a,b):
    s = ((3*x1**2 + a) * inverse((2*y1), p)) %p
    x3 = (s**2 -x1 -x2)%p
    y3 = (s*(x1-x3)-y1)%p
    G = (x3,y3)
    return G

#USing P-256 Curve Parameters
## compute dp 
def generate_priv_pub():
    p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    a = 115792089210356248762697446949407573530086143415290314195533631308867097853948
    b = 41058363725152142129326129780047268409114441015993725554835256314039467401291
    G = (48439561293906451759052585252797914202762949526041747995844080717082404635286,36134250956749795798585127919587881956611106672985015071877198253568414405109)
    N = 115792089210356248762697446949407573529996955224135760342422259061068512044369

    d = getRandomRange(2, p-2) 
    while GCD(d,p-1) !=1:
        d = getRandomRange(2,p-2) 
    dbin = bin(d)[2:]
    length=  len(bin(d)[2:])
    P = G
    Q = G
    #find the length, this will be "m"
    i = 0
    for i in range(1,length):
        #print "For i equal ", i
        #print "The bin values is ", dbin[i]
        Q = double(Q[0],Q[1],Q[0],Q[1],p,a,b)
       # print "Double Q equals", Q
        if dbin[i] == '1':
            Q = add(Q[0],Q[1],P[0],P[1],p,a,b)
            #print "Add Q and P equals", Q
        #print "\n"
    return(Q[0],Q[1],d)    

def generate_shared(pub_x1,pub_x2,priv):
    p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    a = 115792089210356248762697446949407573530086143415290314195533631308867097853948
    b = 41058363725152142129326129780047268409114441015993725554835256314039467401291
    G = (pub_x1,pub_x2)
    N = 115792089210356248762697446949407573529996955224135760342422259061068512044369
    d = priv
    dbin = bin(d)[2:]
    length=  len(bin(d)[2:])
    P = G
    Q = G
    #find the length, this will be "m"
    i = 0
    for i in range(1,length):
        #print "For i equal ", i
        #print "The bin values is ", dbin[i]
        Q = double(Q[0],Q[1],Q[0],Q[1],p,a,b)
       # print "Double Q equals", Q
        if dbin[i] == '1':
            Q = add(Q[0],Q[1],P[0],P[1],p,a,b)
            #print "Add Q and P equals", Q
        #print "\n"
    return(Q[0],Q[1])  
    
############################################
############################################
############ RSA Functions#################
def genRSAkey(e):
    #gen_key = RSA.generate(2048, e = 65537)
    gen_key = RSA.generate(2048, e = e)
    #public_key = gen_key.publickey().exportKey("PEM") 
    private_key = gen_key.exportKey("PEM") 
    #For testing
    rsa_out = open("RSA_PEM.txt", 'wt')
    rsa_out.write(private_key)

    ### Work on formating the PEM output to somethign usable
    begin_key = re.search('-----BEGIN RSA PRIVATE KEY-----', private_key)
    end_key = re.search('-----END RSA PRIVATE KEY-----', private_key)
    priv_key = private_key[begin_key.end():end_key.start()]
    #convert from base 64
    key_hex = binascii.hexlify(base64.standard_b64decode(priv_key))
    #Now pull from PEM format
    n_hex = key_hex[22:536]
    priv_hex = key_hex[554:1066]
    n_int =  int(n_hex,16)
    priv_int = int(priv_hex,16)
    return (n_int, priv_int, e)

def sign_stuff(m, n, d):
    sigma = pow(m,d,n)
    
    return sigma
    
def verify(m, sigma, e, n):
    verify = pow(sigma,e,n)
    status = 0
    if verify == m:
        status = 1
    return status
#############
############
## AES Stuff

def encrypt_GCM(data, key,nonce):
    cipher = AES.new(key, AES.MODE_GCM, nonce = nonce)
    ciphertext = cipher.encrypt(data)
    return (ciphertext, nonce)

def decrypt_GCM(cipher, key,nonce):
    decipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = decipher.decrypt(cipher)
    return (plaintext)

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048
e = 65537

#Setup of connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#### Alice generates her RAS public information. 

Alice_RSA_Key = genRSAkey(e)
print "Generating an RSA signature for Alice's session ", Alice_RSA_Key, "\n"

## Alice signs RSA 

Alice_signed_RSA = str(sign_stuff(Alice_RSA_Key[0], Alice_RSA_Key[0], Alice_RSA_Key[1])) + ':' + str(sign_stuff(Alice_RSA_Key[2], Alice_RSA_Key[0], Alice_RSA_Key[1]))
RSA_message = str(Alice_RSA_Key[0]) +':'+ str(Alice_RSA_Key[2]) +':' + Alice_signed_RSA
print "Sending an RSA signed public key for Alice's session ", RSA_message, "\n"
s.send(RSA_message)

#### Recieve Bob's RSA public key pair.
Bob_public_RSA_msg = s.recv(BUFFER_SIZE)
Bob_public_RSA = re.split(':?', Bob_public_RSA_msg)
    
## now check both mod and exponent for tampering

#check1 = verify(int(Bob_public_RSA[0]), int(Bob_public_RSA[2]), int(Bob_public_RSA[1]), int(Bob_public_RSA[0]))
check2 = verify(int(Bob_public_RSA[1]), int(Bob_public_RSA[3]), int(Bob_public_RSA[1]), int(Bob_public_RSA[0]))
if check2 == 1:
    print "Bob RSA public verified no tampering"
    
# ###########################
# # Generate Alice's Pair of Pub/Priv
# ##########################

Alice_priv_pub = generate_priv_pub()
print "Generated Alice's ECC Parameters. Her ECC parameters are ", Alice_priv_pub, "\n"

# #Create the message
message = str(Alice_priv_pub[0])+":"+ str(Alice_priv_pub[1])

#sign the message
message_signature= str(sign_stuff(Alice_priv_pub[0], Alice_RSA_Key[0], Alice_RSA_Key[1]))+':'+str(sign_stuff(Alice_priv_pub[1], Alice_RSA_Key[0], Alice_RSA_Key[1]))
signed_message = message +':'+ message_signature 
print "Sending Bob Public Signed ECC Parameters Message: ", signed_message, "\n"
s.send(signed_message)


# #Recieve ECC Public from Bob

Bob_Public_ECC_msg= s.recv(BUFFER_SIZE)
Bob_public_ECC = re.split(':?', Bob_Public_ECC_msg)
print "Alice Received ECC Public From Bob", Bob_Public_ECC_msg, "\n"

print "Bob's Public split message is: ", Bob_public_ECC, "\n"

# ## Now verify from Alice
check1 = verify(int(Bob_public_ECC[0]), int(Bob_public_ECC[2]), int(Bob_public_RSA[1]), int(Bob_public_RSA[0]))
check2 = verify(int(Bob_public_ECC[1]), int(Bob_public_ECC[3]), int(Bob_public_RSA[1]), int(Bob_public_RSA[0]))

print "The status of check 1 : ", check1, " The status of check 2: ", check2, "\n"
# #print check1, " ", check2

if check1 == 1 and check2 == 1:
    print "Bob ECC public verified"

# Geneate the shared key for Alice

Alice_shared_key = generate_shared(int(Bob_public_ECC[0]),int(Bob_public_ECC[1]),Alice_priv_pub[2])
print "With Bob's public key, Alice generates the follow shared key:", Alice_shared_key, "\n"

#### Now we have a shared key. We first take and create hexlify of the shared X1, then use 16 bytes

aes_key = str(Alice_shared_key[0])[:32]
nonce = str(Alice_shared_key[0])[-32:]

print  "The AES Key is: ", aes_key, "\n"
print "The Nonce is: ", nonce, "\n"

## NOw we encrypt a message for Bob
MESSAGE2 = 'This message is for Bob'
print "Encrypting message ", MESSAGE2, "\n"
MESSAGE2_enc = encrypt_GCM(MESSAGE2, aes_key,nonce)
# #Sign the encrypted message First convert to integer format
MESSAGE2_enc_int = int(binascii.hexlify(MESSAGE2_enc[0]),16)
#print "Encrypted message as int is : ", MESSAGE2_enc_int 

sign_MSG2 = str(sign_stuff(MESSAGE2_enc_int, Alice_RSA_Key[0], Alice_RSA_Key[1]))
signed_message2 = str(MESSAGE2_enc_int) +':'+ sign_MSG2 

# #send Bob the message
print "Sending Bob Signed Message (as int)  Message: ", signed_message2, "\n"
s.send(signed_message2)


#Recieve from Bob
Bob_msg2 = s.recv(BUFFER_SIZE)
Bob_msg2_int = re.split(':?', Bob_msg2)

print "Bob's split message is: ", Bob_msg2_int, "\n"

## Now verify from Alice
check1 = verify(int(Bob_msg2_int[0]), int(Bob_msg2_int[1]), int(Bob_public_RSA[1]), int(Bob_public_RSA[0]))

if check1 == 1:
    print "Bob message verified"
    
back2hex = hex(int(Bob_msg2_int[0]))[2:-1]
#print back2hex
ciphered = binascii.unhexlify(str(back2hex))
decrypted = decrypt_GCM(ciphered, aes_key,nonce)
print "Alice decrypted a message: ", decrypted, '\n'


s.close()
 
#print "received data:", data