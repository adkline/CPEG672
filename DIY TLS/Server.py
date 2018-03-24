import socket, random, binascii, math, re, hashlib, base64
from Crypto.PublicKey import RSA
from Crypto.Util.number import *


from Crypto.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Crypto.Random import get_random_bytes


############################################
############################################
############ ECC Functions#################
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
    # print "n hex is : ", n_hex
    # print "priv_hex is : ", priv_hex
    # print "n int is: ", n_int
    # print "priv_int is : ", priv_int
    
    return (n_int, priv_int, e)



#Sign the integer form of a message!!
def sign_stuff(m, n, d):
   # m = "I solemnly swear to learn applied cryptography. Even though there are not enough graded assignments to incentivize the needed hours I will: 1) work problems 2) ask questions 3) ponder start-ups 4) think in a paranoid fashion 5) get it done without excuse"
    #m_hex = binascii.hexlify(m)
    #m_int = int(m_hex,16)
    sigma = pow(m,d,n)
    
    return sigma
    
def verify(m, sigma, e, n):
    #m_hex = binascii.hexlify(m)
    #m_int = int(m_hex,16)
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
BUFFER_SIZE = 2048  # Normally 1024, but we want fast response
e = 65537

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
 
conn, addr = s.accept()
print 'Connection address:', addr


# This is Bob

while 1:
    
    #########Recieve from Alice her RSA public key
    Alice_public_RSA_msg = conn.recv(BUFFER_SIZE)
    if not Alice_public_RSA_msg: break
    Alice_public_RSA = re.split(':?', Alice_public_RSA_msg)
    
    ## now check both mod and exponent for tampering
    print "Recieved from Alice", Alice_public_RSA, '\n'
    
    #check1 = verify(int(Alice_public_RSA[0]), int(Alice_public_RSA[2]), int(Alice_public_RSA[1]), int(Alice_public_RSA[0]))
    check2 = verify(int(Alice_public_RSA[1]), int(Alice_public_RSA[3]), int(Alice_public_RSA[1]), int(Alice_public_RSA[0]))

    if check2 == 1:
        print "Alice RSA public verified no tampering"
    
    ######Genearate Bob's Pulic
    Bob_RSA_Key = genRSAkey(e)
    print "Generating an RSA signature for Bob's session ", Bob_RSA_Key, "\n"

    ## Bob signs RSA 
    Bob_signed_RSA = str(sign_stuff(Bob_RSA_Key[0], Bob_RSA_Key[0], Bob_RSA_Key[1])) + ':' + str(sign_stuff(Bob_RSA_Key[2], Bob_RSA_Key[0], Bob_RSA_Key[1]))
    RSA_message = str(Bob_RSA_Key[0]) +':'+ str(Bob_RSA_Key[2]) +':' + Bob_signed_RSA
    print "Sending an RSA signed public key for Bob's session ", RSA_message, "\n"
    conn.send(RSA_message)
    
    #Recieve Alice ECC Parameters
    Alice_Public_ECC_msg= conn.recv(BUFFER_SIZE)
    Alice_public_ECC = re.split(':?', Alice_Public_ECC_msg)
    print "Bob Received ECC Public From Alice", Alice_Public_ECC_msg, "\n"
    
    print "Alice's Public split message is: ", Alice_public_ECC, "\n"
    
    # ## Now verify from Alice
    check1 = verify(int(Alice_public_ECC[0]), int(Alice_public_ECC[2]), int(Alice_public_RSA[1]), int(Alice_public_RSA[0]))
    check2 = verify(int(Alice_public_ECC[1]), int(Alice_public_ECC[3]), int(Alice_public_RSA[1]), int(Alice_public_RSA[0]))
    
    print "The status of check 1 : ", check1, " The status of check 2: ", check2, "\n"
    # #print check1, " ", check2
    
    if check1 == 1 and check2 == 1:
        print "Alice ECC public verified"
    
    ## Bob Generate's ECC Parameters
    Bob_priv_pub = generate_priv_pub()
    print "Generated Bob's ECC Parameters. HIs ECC parameters are ", Bob_priv_pub, "\n"
    
    # #Create the message
    message = str(Bob_priv_pub[0])+":"+ str(Bob_priv_pub[1])
    
    #sign the message
    message_signature= str(sign_stuff(Bob_priv_pub[0], Bob_RSA_Key[0], Bob_RSA_Key[1]))+':'+str(sign_stuff(Bob_priv_pub[1], Bob_RSA_Key[0], Bob_RSA_Key[1]))
    signed_message = message +':'+ message_signature 
    print "Sending Alice Public Signed ECC Parameters Message: ", signed_message, "\n"
   
    conn.send(signed_message)
    
    #Generate the shared ECC Key
    Bob_shared_key = generate_shared(int(Alice_public_ECC[0]),int(Alice_public_ECC[1]),Bob_priv_pub[2])
    print "With Alice's public key, Bob generates the follow shared key:", Bob_shared_key, "\n"
    
    aes_key = str(Bob_shared_key[0])[:32]
    nonce = str(Bob_shared_key[0])[-32:]
    
    print  "The AES Key is: ", aes_key, "\n"
    print "The Nonce is: ", nonce, "\n"
    
    ## Recieve Alice Message
    
    Alice_msg2 = conn.recv(BUFFER_SIZE)
    Alice_msg2_int = re.split(':?', Alice_msg2)
    
    print "Alice's split message is: ", Alice_msg2_int, "\n"
    
    ## Now verify from Alice
    check1 = verify(int(Alice_msg2_int[0]), int(Alice_msg2_int[1]), int(Alice_public_RSA[1]), int(Alice_public_RSA[0]))
    
    if check1 == 1:
        print "Alice message verified"
        
    back2hex = hex(int(Alice_msg2_int[0]))[2:-1]
    #print back2hex
    ciphered = binascii.unhexlify(str(back2hex))
    decrypted = decrypt_GCM(ciphered, aes_key,nonce)
    print "Bob decrypted a message: ", decrypted, '\n'
    
    ## Now Bob replies with a message
    MESSAGE3 = 'Wasting bandwidth just to say? :' + decrypted
    
    print "Encrypting message ", MESSAGE3, "\n"
    MESSAGE3_enc = encrypt_GCM(MESSAGE3, aes_key,nonce)
    # #Sign the encrypted message First convert to integer format
    MESSAGE3_enc_int = int(binascii.hexlify(MESSAGE3_enc[0]),16)
    #print "Encrypted message as int is : ", MESSAGE2_enc_int 
    
    sign_MSG3 = str(sign_stuff(MESSAGE3_enc_int, Bob_RSA_Key[0], Bob_RSA_Key[1]))
    signed_message3 = str(MESSAGE3_enc_int) +':'+ sign_MSG3 
    
    # #send Bob the message
    print "Sending Alice Signed Message (as int)  Message: ", signed_message3, "\n"
    conn.send(signed_message3)
    
        

    # # conn.send(signed_message)  # echo
conn.close()