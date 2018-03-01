import os, math, binascii
from Crypto.Cipher import AES

def XOR_hex(h1, h2):
    ans_hex = hex(int(h1, 16) ^ int(h2, 16))[2:]
    if (ans_hex[-1] == "L"):
        ans_hex = ans_hex[:-1]
    return ans_hex.zfill(len(h1))

def XOR_raw(r1, r2):
    return binascii.unhexlify(XOR_hex(binascii.hexlify(r1), binascii.hexlify(r2)))

class ChainedCBC:
    def __init__(self, key):
        IV = os.urandom(16)
        self.IV = IV
        self.F_k = AES.new(key)
        self.first_message = True
    def encrypt(self, pt):
        lpt = len(pt)
        if lpt % 16 > 0:
            padding = (16 - (lpt % 16))*"x"
        else:
            padding = ""
        padded_pt = pt + padding
        ciphertext = ""
        if self.first_message:
            self.first_message = False
            ciphertext += self.IV
        for i in range(len(padded_pt)/16):
            inputi = XOR_raw(self.IV, padded_pt[i:i+16])
            self.IV = self.F_k.encrypt(inputi)
            ciphertext += self.IV
        return ciphertext

import random

class ChallengeProblem:
    def __init__(self):
        self.messages = ["The 1st message.", "The 2nd message."]
    def beginChallenge(self):
        self.cipher = ChainedCBC(os.urandom(16))
        self.__secret_index = ord(os.urandom(1)) % 2
        print self.messages[self.__secret_index]
        return self.encrypt(self.messages[self.__secret_index])
    def encrypt(self, pt):
        return self.cipher.encrypt(pt)
    def isTheSecret(self, guessed_index):
        # your goal is to have this function return true
        # more than 50% of the time
        return guessed_index == self.__secret_index

#sample challenge
mychallenge = ChallengeProblem()
ciphertext = mychallenge.beginChallenge()
print " The cipher text is ", ciphertext, '\n'
print 'The cipher as hex is ', binascii.hexlify(ciphertext)


test1 = mychallenge.encrypt("a")
test2 = mychallenge.encrypt("a")

## XOR the test1 output (IV) with plaintext - this is the input to the CBC encryption

test1_hex = binascii.hexlify(test1)
test2_hex = binascii.hexlify(test2)

print 'The test1 as hex is ' , test1_hex

inputCBC = binascii.hexlify(XOR_raw(test1,"aa"))

print " The input to the CBC block for test 2  is ", inputCBC

print 'The test2 as hex is ' , test2_hex


#do work on the cipher text here to figure out message one or message two

myguess = 1

if mychallenge.isTheSecret(myguess):
    print "I was right!"
else:
    print "I was wrong"