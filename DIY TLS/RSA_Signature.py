import random, binascii,re, hashlib, base64
from Crypto.PublicKey import RSA

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
    sigma = pow(m_int,d,n)
    
    return sigma
    
def verify(m, sigma, e, n):
    #m_hex = binascii.hexlify(m)
    #m_int = int(m_hex,16)
    verify = pow(sigma,e,n)
    status = 0
    if verify == m:
        status = 1
    return status

myKey = genRSAkey(65537)
    
m = "I solemnly swear to learn applied cryptography. Even though there are not enough graded assignments to incentivize the needed hours I will: 1) work problems 2) ask questions 3) ponder start-ups 4) think in a paranoid fashion 5) get it done without excuse"
m_hex = binascii.hexlify(m)
m_int = int(m_hex,16)

test_sign = sign_stuff(m_int, myKey[0], myKey[1])

print test_sign

print verify(m_int, test_sign, myKey[2], myKey[0])




