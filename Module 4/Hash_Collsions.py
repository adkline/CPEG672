import math, binascii, hashlib

dict = file("dictionary_Mod4.txt", 'r')
#dict = file("test_text.txt", 'r')

dict_hash = file("hashed_dict", "w")
temp = dict.readline()

while temp != "":
    
    ### MD5 hash and output to dict_hash
    dict_hash.write(hashlib.md5(temp).hexdigest())
    dict_hash.write('\n')
    temp = dict.readline()
    
    
dict_hash.close() 
dict.close()


dict_hash = file()