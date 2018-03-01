import binascii
def crand(seed):
    r=[]
    r.append(seed)
    for i in range(30):
        r.append((16807*r[-1]) % 2147483647)
        if r[-1] < 0:
            r[-1] += 2147483647
    for i in range(31, 34):
        r.append(r[len(r)-31])
    for i in range(34, 344):
        r.append((r[len(r)-31] + r[len(r)-3]) % 2**32)
    while True:
        next = r[len(r)-31]+r[len(r)-3] % 2**32
        r.append(next)
        yield (next >> 1 if next < 2**32 else (next - 2**32) >> 1)

# mygen = crand(1983)
# rands = [mygen.next() for i in range(4)]
# plaintext = "andy rules!!"
# hexplain = binascii.hexlify(plaintext)
# hexkey = "".join(map(lambda x: format(x, 'x')[-6:], rands))

# cipher_as_int = int(hexplain, 16) ^ int(hexkey, 16)
# cipher_as_hex = format(cipher_as_int, 'x')


## Decrypte

def enc_dec_stream(text, seed):
    import binascii
    def crand(seed):
        r=[]
        r.append(seed)
        for i in range(30):
            r.append((16807*r[-1]) % 2147483647)
            if r[-1] < 0:
                r[-1] += 2147483647
        for i in range(31, 34):
            r.append(r[len(r)-31])
        for i in range(34, 344):
            r.append((r[len(r)-31] + r[len(r)-3]) % 2**32)
        while True:
            next = r[len(r)-31]+r[len(r)-3] % 2**32
            r.append(next)
            yield (next >> 1 if next < 2**32 else (next - 2**32) >> 1)
    
    # Find the legnth of the text message. 
    
    message_length = len(text)
    
    if message_length%6 != 0:
        numtoadd = message_length%6
        for i in range(1,numtoadd):
            text = text + '0'
                
    numrands = len(text)/6
    print numrands
    mygen = crand(seed)
    rands = [mygen.next() for i in range(numrands)]

    print rands
    
    hexkey = "".join(map(lambda x: format(x, 'x')[-6:], rands))


    cipher_as_int = int(text, 16) ^ int(hexkey, 16)
    cipher_as_hex = format(cipher_as_int, 'x')
    
    if len(cipher_as_hex)%16 !=0:
        numtoadd = message_length%16
        for i in range(1,numtoadd):
            cipher_as_hex = cipher_as_hex + '20'
    
    print len(cipher_as_hex)
    
    num_segments = len(cipher_as_hex)/16
    print num_segments
    DecryptedText = ''
    i = 0    
    
    while i < num_segments:
         #starting point
        j = i*16
        #
        #DecryptedText.append(binascii.unhexlify(DecryptedHex[j:j+16]))
        DecryptedText = DecryptedText + binascii.unhexlify(cipher_as_hex[j:j+16])
        i = i+1
    
    #return cipher_as_hex
    
    return DecryptedText

print enc_dec_stream('e2d155756dc02723abcf7fdcd2709f04e9435a51af623fa0ee59ce3feedf', 54321)