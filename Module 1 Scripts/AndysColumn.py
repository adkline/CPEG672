import random
import urllib2

#words = res.read().split()

#random.shuffle(quotes)
#random.shuffle(words)


def col_trans(plain):
    cols = random.randint(8,10)
    key = range(cols)
    random.shuffle(key)
    return "".join(plain[i::cols].lower() for i in key), key
    

plaintext = 'Trying to figure out how this works'    
plaintext = plaintext.replace(' ', '')

print plaintext

print col_trans(plaintext)
