import math, binascii


tag1= '9ff9bd8e3b1d0657cad7fe89b31130a8'
tag2 = '8aa501578b405e709c2a46cb808f70b9'
tag1tag2 = 'c9eb264b3e5fd526efaf0530f10e9119'

mes1 = 'the 1st message.'
mes2 = 'the 2nd message.'
mes1mes2 = 'the 1st message.the 2nd message.'

# new could be mes2||mes1 XOR Mac (2)

hex_mes = binascii.hexlify(mes2+mes1)
print " Hex of message 2 || message 1 =  ", hex_mes
newmessage = binascii.hexlify(str(int(hex_mes,16)^int(tag2,16)))
print " The new message is :  ", newmessage


newmessage_string = ''
length_Message = len(newmessage)

print "The original message is of length ", length_Message

mes1_hex = binascii.hexlify(mes1)
mes2_hex = binascii.hexlify(mes2)

tempstring =  binascii.hexlify(str(int(mes1_hex,16)^int(tag2,16)))

print tempstring

#newM = mes2 +()

# if length_Message > 16:
#     shift = 16 - (length_Message%16)
#     print "Length over 16, we must pad with ", shift, "spaces at the end"
#     #DecryptedHex >> shift
#     Padding = ['20'] * shift
#     m = 0
#     while m < len(Padding):
#         newmessage = newmessage + Padding[m]
#         m = m+1
        
# num_segments = len(newmessage)/16
# DecryptedText = ''
# i = 0    

# while i < num_segments:
#     #starting point
#     j = i*16
#     #
#     #DecryptedText.append(binascii.unhexlify(DecryptedHex[j:j+16]))
#     newmessage_string = newmessage_string + binascii.unhexlify(newmessage[j:j+16])
#     i = i+1
    
# print newmessage_string