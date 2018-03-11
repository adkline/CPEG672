import math, binascii, urllib
import hashlib
from PIL import Image
from Crypto import Random
from Crypto.Cipher import AES

print ("Choose an AES Encryption/Decryption Scheme:")
print ("ECB, CBC, CTR or OFB  ")

## Here we determine the format of the incoming image file and save as that type.
## Testing this code, but couldn't get to work in time. 
def format_modifier(n):
    out = ''
    if n == 'JPEG':
        out = '.jpg'
        
    if n == 'PNG':
        out = '.png' 
        
    return out

mode = raw_input(' ')

## Pad the bytes on the images 
def pad_image(m):
    
    remain = len(m)%16
    num_to_add = 16 - remain
    for i in range (0,num_to_add):
        m = m + '0'
    
    #print len(m)%16
    return m

def tonycount():
    global cntr
    temp_hash = str (hashlib.sha224(cntr).hexdigest())
    cntr = str(int(cntr,16)^int(temp_hash,16))[:16]
    return cntr
    
    
print mode

if mode != 'ecb'and mode != 'ECB' and mode != 'CBC' and mode != 'cbc' and mode != 'OFB' and mode != 'ofb' and mode != 'CTR' and mode != 'ctr':
    
    print "Mode entered not found, please execute again. "


if mode == 'ECB' or mode =='ecb':
    
    print " Executing the AES_ECB scheme : "
    mode = raw_input("Do you want to encrypt or decrypt? e/d ")
    
    if mode == 'e' or mode == 'E':
        print "You chose to Encrypt using AES_ECB: "
        text_name = raw_input("Type the name of the file to encrypt with the extension: ")
        
        key_size = input("Enter the required key size (16, 24, 32 bytes): ")
        
        if key_size != 32:
            ask_size=  raw_input("Do you want to go to 32 byte to be more secure?? y/n ")
            
            if ask_size == 'y' or ask_size == 'Y':
                key_size = 32
        
        key = raw_input("Enter the key for encryption: ")
        
        if len(key) < key_size:
            print "Your key is less than ", key_size, " characters. To prevent padding, do you want to enter one that is length ", key_size, "?"
            ask_key = raw_input("y/n ")
            
            if ask_key == 'y' or ask_key == 'Y': 
                key = raw_input("Enter the new key for encryption with proper length ")
        
        key_pad = key
        
        if len(key) < key_size:
            print "Key is less than required, we must pad with ", key_size-len(key), '?' 
            while len(key_pad) <  key_size:
                key_pad = key_pad + '?'
            print "Using key: ", key_pad
        
        if len(key_pad) > key_size:
            print "Key is greater than block size, we must truncate "
            key_pad = key_pad[:key_size]
            print "Using key: ", key_pad
        
        iv = Random.new().read(AES.block_size)
        im = Image.open(text_name)
        image_info = [im.tostring(), im.size, im.mode]
        cipher = AES.new(key_pad, AES.MODE_ECB)
        
        # We must pad the image if it isn't a multpile of 16
        image_to_use = image_info[0]
        
        if len(image_info[0])%16 != 0:
            print "we must pad the input image to be a multiple of 16"
            
            image_to_use = pad_image(image_info[0])
        
        enc_image = cipher.encrypt(image_to_use)
        
        Image.frombytes(image_info[2], image_info[1], enc_image).save("encrypted_ECB.png")
        #print image_info

    if mode == 'd' or mode == 'D':
        print "You chose to Deccrypt using AES_ECB: "
        text_name = raw_input("Type the name of the file to decrypt with the extension: ")
        key = raw_input("Enter the key for encryption: ")
        key_size = input("Enter the required key size 16, 24, 32 bytes: ")
        
        key_pad = key
        
        if len(key) < key_size:
            print "Key is less than required, we must pad with ", key_size-len(key), '?' 
            while len(key_pad) <  key_size:
                key_pad = key_pad + '?'
            print "Using key: ", key_pad
        
        if len(key_pad) > key_size:
            print "Key is greater than block size, we must truncate "
            key_pad = key_pad[:key_size]
            print "Using key: ", key_pad
        
        iv = Random.new().read(AES.block_size)
        im = Image.open(text_name)
        image_info = [im.tostring(), im.size, im.mode]
        cipher = AES.new(key_pad, AES.MODE_ECB)
        image_to_use = image_info[0]
          # We must pad the image if it isn't a multpile of 16
        if len(image_info[0])%16 != 0:
            print "we must pad the input image to be a multiple of 16"
            
            image_to_use = pad_image(image_info[0])
        
        #dec_image = image_info[0]
        dec_image = cipher.decrypt(image_to_use)
       
        Image.frombytes(image_info[2], image_info[1], dec_image).save('decrypted_ECB.png')
    
  

if mode == 'CBC' or mode =='cbc':
    
    print "Executing the AES_CBC scheme :"
    mode = raw_input("Do you want to encrypt or decrypt? e/d ")
    
    if mode == 'e' or mode == 'E':
        
        print "You chose to Encrypt using AES_CBC :" 
        text_name = raw_input("Type the name of the file to encrypt with the extension: ")
        key_size = input("Enter the required key size (16, 24, 32 bytes): ")
        
        if key_size != 32:
            ask_size=  raw_input("Do you want to go to 32 byte to be more secure?? y/n ")
            
            if ask_size == 'y' or ask_size == 'Y':
                key_size = 32
        
        key = raw_input("Enter the key for encryption: ")
        
        if len(key) < key_size:
            print "Your key is less than ", key_size, " characters. To prevent padding, do you want to enter one that is length ", key_size, "?"
            ask_key = raw_input("y/n ")
            
            if ask_key == 'y' or ask_key == 'Y': 
                key = raw_input("Enter the new key for encryption with proper length ")
        
        key_pad = key
        
        if len(key) < key_size:
            print "Key is less than required, we must pad with ", key_size-len(key), '?' 
            while len(key_pad) <  key_size:
                key_pad = key_pad + '?'
            print "Using key: ", key_pad
        
        if len(key_pad) > key_size:
            print "Key is greater than block size, we must truncate "
            key_pad = key_pad[:key_size]
            print "Using key: ", key_pad
        
        iv = Random.new().read(AES.block_size)
        
        print " Your IV.hexdigest() for this encryption is : ", binascii.hexlify(iv)
        
        im = Image.open(text_name)
        image_info = [im.tostring(), im.size, im.mode]
        cipher = AES.new(key_pad, AES.MODE_CBC, iv)
        
        image_to_use = image_info[0]
          # We must pad the image if it isn't a multpile of 16
        if len(image_info[0])%16 != 0:
            print "we must pad the input image to be a multiple of 16"
            
            image_to_use = pad_image(image_info[0])
        
        enc_image = cipher.encrypt(image_to_use)
        
        Image.frombytes(image_info[2], image_info[1], enc_image).save('encrypted_CBC.png')
    
    if mode == 'd' or mode == 'D':
        print "You chose to Deccrypt using AES_CBC: "
        text_name = raw_input("Type the name of the file to decrypt with the extension: ")
        key = raw_input("Enter the key for encryption: ")
        key_size = input("Enter the required key size 16, 24, 32 bytes: ")
        IV = raw_input("Input the HEXDIGEST of the IV :")
        
        key_pad = key
        
        if len(key) < key_size:
            print "Key is less than required, we must pad with ", key_size-len(key), '?' 
            while len(key_pad) <  key_size:
                key_pad = key_pad + '?'
            print "Using key: ", key_pad
        
        if len(key_pad) > key_size:
            print "Key is greater than block size, we must truncate "
            key_pad = key_pad[:key_size]
            print "Using key: ", key_pad
        
        iv = binascii.unhexlify(IV)
        im = Image.open(text_name)
        image_info = [im.tostring(), im.size, im.mode]
        cipher = AES.new(key_pad, AES.MODE_CBC, iv)
          # We must pad the image if it isn't a multpile of 16
        image_to_use = image_info[0]
          # We must pad the image if it isn't a multpile of 16
        if len(image_info[0])%16 != 0:
            print "we must pad the input image to be a multiple of 16"
            
            image_to_use = pad_image(image_info[0])
        
        dec_image = cipher.decrypt(image_to_use)
        
        
        Image.frombytes(image_info[2], image_info[1], dec_image).save('decrypted_CBC.png')
    

     

if mode == 'OFB' or mode =='ofb':
    
    print "Executing the AES_OFB scheme :"
    mode = raw_input("Do you want to encrypt or decrypt? e/d ")
    
    if mode == 'e' or mode == 'E':
        
        print "You chose to Encrypt using AES_OFB :" 
        text_name = raw_input("Type the name of the file to encrypt with the extension: ")
        key_size = input("Enter the required key size (16, 24, 32 bytes): ")
        
        if key_size != 32:
            ask_size=  raw_input("Do you want to go to 32 byte to be more secure?? y/n ")
            
            if ask_size == 'y' or ask_size == 'Y':
                key_size = 32
        
        key = raw_input("Enter the key for encryption: ")
        
        if len(key) < key_size:
            print "Your key is less than ", key_size, " characters. To prevent padding, do you want to enter one that is length ", key_size, "?"
            ask_key = raw_input("y/n ")
            
            if ask_key == 'y' or ask_key == 'Y': 
                key = raw_input("Enter the new key for encryption with proper length ")
        
        key_pad = key
        
        if len(key) < key_size:
            print "Key is less than required, we must pad with ", key_size-len(key), '?' 
            while len(key_pad) <  key_size:
                key_pad = key_pad + '?'
            print "Using key: ", key_pad
        
        if len(key_pad) > key_size:
            print "Key is greater than block size, we must truncate "
            key_pad = key_pad[:key_size]
            print "Using key: ", key_pad
        
        iv = Random.new().read(AES.block_size)
        
        print " Your IV.hexdigest() for this encryption is : ", binascii.hexlify(iv)
        
        im = Image.open(text_name)
        image_info = [im.tostring(), im.size, im.mode]
        cipher = AES.new(key_pad, AES.MODE_OFB, iv)
              # We must pad the image if it isn't a multpile of 16
        image_to_use = image_info[0]
          # We must pad the image if it isn't a multpile of 16
        if len(image_info[0])%16 != 0:
            print "we must pad the input image to be a multiple of 16"
            
            image_to_use = pad_image(image_info[0])
        
        enc_image = cipher.encrypt(image_to_use)
        
        Image.frombytes(image_info[2], image_info[1], enc_image).save('encrypted_OFB.png')
    
    if mode == 'd' or mode == 'D':
        print "You chose to Deccrypt using AES_OFB: "
        text_name = raw_input("Type the name of the file to decrypt with the extension: ")
        key = raw_input("Enter the key for encryption: ")
        key_size = input("Enter the required key size (16, 24, 32 bytes): ")
        IV = raw_input("Input the HEXDIGEST of the IV :")
        
        key_pad = key
        
        if len(key) < key_size:
            print "Key is less than required, we must pad with ", key_size-len(key), '?' 
            while len(key_pad) <  key_size:
                key_pad = key_pad + '?'
            print "Using key: ", key_pad
        
        if len(key_pad) > key_size:
            print "Key is greater than block size, we must truncate "
            key_pad = key_pad[:key_size]
            print "Using key: ", key_pad
        
        iv = binascii.unhexlify(IV)
        im = Image.open(text_name)
        image_info = [im.tostring(), im.size, im.mode]
        cipher = AES.new(key_pad, AES.MODE_OFB, iv)
        
              # We must pad the image if it isn't a multpile of 16
        image_to_use = image_info[0]
          # We must pad the image if it isn't a multpile of 16
        if len(image_info[0])%16 != 0:
            print "we must pad the input image to be a multiple of 16"
            
            image_to_use = pad_image(image_info[0])
        
        dec_image = cipher.decrypt(image_to_use)
    
        
        Image.frombytes(image_info[2], image_info[1], dec_image).save('decrypted_OFB.png')
    

     


if mode == 'CTR' or mode =='ctr':
    
    print "Executing the AES_CTR scheme :"
    mode = raw_input("Do you want to encrypt or decrypt? e/d ")
    
    if mode == 'e' or mode == 'E':
        
        print "You chose to Encrypt using AES_CTR :" 
        text_name = raw_input("Type the name of the file to encrypt with the extension: ")
        key_size = input("Enter the required key size (16, 24, 32 bytes): ")
        
        if key_size != 32:
            ask_size=  raw_input("Do you want to go to 32 byte to be more secure?? y/n ")
            
            if ask_size == 'y' or ask_size == 'Y':
                key_size = 32
        
        key = raw_input("Enter the key for encryption: ")
        
        if len(key) < key_size:
            print "Your key is less than ", key_size, " characters. To prevent padding, do you want to enter one that is length ", key_size, "?"
            ask_key = raw_input("y/n ")
            
            if ask_key == 'y' or ask_key == 'Y': 
                key = raw_input("Enter the new key for encryption with proper length ")
        
        key_pad = key
        
        if len(key) < key_size:
            print "Key is less than required, we must pad with ", key_size-len(key), '?' 
            while len(key_pad) <  key_size:
                key_pad = key_pad + '?'
            print "Using key: ", key_pad
        
        if len(key_pad) > key_size:
            print "Key is greater than block size, we must truncate "
            key_pad = key_pad[:key_size]
            print "Using key: ", key_pad
    
    
    
        IVphrase = raw_input("Input an IV starting phrase : ")
    
        if len(IVphrase) <  16 :
            print "Your IV phrase is too short, we are padding : "
            while len(IVphrase) <  16:
                IVphrase = IVphrase + '0'
            print "New IV phrase is " , IVphrase
            
        if len(IVphrase) > 16:
            print "Your IV phrase is too long, we are truncating : "
            IVphrase = IVphrase[:16]
            print "New IV phrase is " , IVphrase
            
        IVphrase_hex = binascii.hexlify(IVphrase)
        
        #print "Your Hexdigest of the IV is ", IVphrase_hex
        
        ctr1 = str(int((hashlib.sha224(IVphrase_hex[:16]).hexdigest()),16)^int((hashlib.sha224(IVphrase_hex[16:32]).hexdigest()),16))
        cntr = ctr1[:16]
    
       
        
        cipher = AES.new(key_pad, AES.MODE_CTR, counter=tonycount)
        im = Image.open(text_name)
        image_info = [im.tostring(), im.size, im.mode]
              # We must pad the image if it isn't a multpile of 16
        image_to_use = image_info[0]
          # We must pad the image if it isn't a multpile of 16
        if len(image_info[0])%16 != 0:
            print "we must pad the input image to be a multiple of 16"
            
            image_to_use = pad_image(image_info[0])
        
        enc_image = cipher.encrypt(image_to_use)
        
        Image.frombytes(image_info[2], image_info[1], enc_image).save('encrypted_CTR.png')
        

    if mode == 'd' or mode == 'D':
        print "You chose to Deccrypt using AES_CTR: "
        text_name = raw_input("Type the name of the file to decrypt with the extension: ")
        key = raw_input("Enter the key for encryption: ")
        key_size = input("Enter the required key size (16, 24, 32 bytes): ")
        
        key_pad = key
        
        IVphrase = raw_input("Input an IV starting phrase : ")
    
        if len(IVphrase) <  16 :
            print "Your IV phrase is too short, we are padding : "
            while len(IVphrase) <  16:
                IVphrase = IVphrase + '0'
            print "New IV phrase is " , IVphrase
            
        if len(IVphrase) > 16:
            print "Your IV phrase is too long, we are truncating : "
            IVphrase = IVphrase[:16]
            print "New IV phrase is " , IVphrase
            
        IVphrase_hex = binascii.hexlify(IVphrase)
        
        ctr1 = str(int((hashlib.sha224(IVphrase_hex[:16]).hexdigest()),16)^int((hashlib.sha224(IVphrase_hex[16:32]).hexdigest()),16))
        cntr = ctr1[:16]
        
        im = Image.open(text_name)
        image_info = [im.tostring(), im.size, im.mode]
        cipher = AES.new(key_pad, AES.MODE_CTR, counter=tonycount)
        
              # We must pad the image if it isn't a multpile of 16
        image_to_use = image_info[0]
          # We must pad the image if it isn't a multpile of 16
        if len(image_info[0])%16 != 0:
            print "we must pad the input image to be a multiple of 16"
            
            image_to_use = pad_image(image_info[0])
        
        dec_image = cipher.decrypt(image_to_use)
    
        
        Image.frombytes(image_info[2], image_info[1], dec_image).save('decrypted_CTR.png')
    
    

print "Execution of suite completed"
    

