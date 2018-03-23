
# ## Generate a 1024 DH strangth prime. 
# openssl dhparam -out dh1024.pem 1024

# generate the key
#openssl genpkey -paramfile dhparam.pem -out dhkey.pem

# # Interpret with 
# openssl asn1parse -in dh1024.pem

# now that prime is stored in .pem format we can get access to it by reading base64. import base64 and run base64.standard_b64decode on the parts that matter. This gives you raw bytes. Your prime is at raw[6:6+129]. 
# Get these bytes, convert to hex then an integer. The generator is probably the last byte (normally 2).


import base64, binascii, re

text = file('dh1024.pem', 'r')
string = text.read()
print string


begin_par = re.search('-----BEGIN DH PARAMETERS-----', string)
print begin_par.endpos

end_par = re.search('-----END DH PARAMETERS-----', string)
print end_par.pos



#string = 'MIGHAoGBAIhWDGKgOREPQEwFv+xvo8+WAo0s+YtUzZmeBpSeJGxTR4Cs0nUhTXLCuR96SefaTv5vgqmm8Uz4XdlTdq44S/jF5TedsBFyhCVkVKFdcknBZK8Immihd6WpadSoU7bMJKzuFep5grMW6r0DObub7BHdaYifog5QR6rtneTBPYZbAgEC' 

ashex = binascii.hexlify(base64.standard_b64decode(string))[14:270]


#ashex = '88560C62A039110F404C05BFEC6FA3CF96028D2CF98B54CD999E06949E246C534780ACD275214D72C2B91F7A49E7DA4EFE6F82A9A6F14CF85DD95376AE384BF8C5E5379DB0117284256454A15D7249C164AF089A68A177A5A969D4A853B6CC24ACEE15EA7982B316EABD0339BB9BEC11DD69889FA20E5047AAED9DE4C13D865B'
print " As hex is ", ashex

asint = int(ashex, 16)

print " As int is ", asint




