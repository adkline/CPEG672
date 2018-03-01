import hashlib, random, math, binascii


Secret = 'This should be 64 characters long, if not add more or take away.'
Salt = 'This is the salt'

#print len(Secret)

Secret_hex = binascii.hexlify(Secret)


#Secret_hex = '46f5b72954dffae1951f738b3466eb9513fff03f9cdd5d1188f7766815c2bd27'
#print Secret_hex
#print len(Secret_hex)


# Now take and create a string of bits.

Secret_bin = ''

for i in range(0,len(Secret_hex), 2):
    
    temp_bin = bin(int(Secret_hex[i:i+2],16))[2:]
    num_zeros = 8 - len(temp_bin)
    j = 0 
    while j < num_zeros:
        temp_bin = '0' +temp_bin
        j +=1
    #print Secret_hex[i:i+2], ' ', temp_bin
    Secret_bin = Secret_bin + temp_bin

#print Secret_bin
#print len(Secret_bin)


L = ['','','','','']
R = ['','','','','']
Fk_hex = ['','','','','']
Fk_bin = ['','','','','']

L[0] = str(Secret_bin) [:256]
R[0] = str(Secret_bin)[256:]

print L[0], len(L[0])
print R[0], len(R[0])

### Iterate through each step
for i in range(1,2):
    ## Take RHS and store in L[i]    
    print '\n'
    print 'Iteration ', i , ' is as follows '
    print '\n'
    
    L[i] = R[i-1]
    
    print ' L ' , i ,  ' is ' , L[i]
    ## Take right hand side SHA256 it 
    
    Fk_hex[i] = hashlib.sha256(R[i-1]).hexdigest()
    
    print 'Fk ', i, 'hex is ' , Fk_hex[i]
    ## convert to Binary
    #print Fk_hex[i]
    
    for m in range(0,len(Fk_hex[i]), 2):
        
        temp_bin = bin(int(Fk_hex[i][m:m+2],16))[2:]
        
        num_zeros = 8 - len(temp_bin)
        
        j = 0 
        while j < num_zeros:
            temp_bin = '0' +temp_bin
            j +=1
    
        Fk_bin[i] = Fk_bin[i] +temp_bin
    
    print 'Fk  ', i, 'bin is ' , Fk_bin[i] 
    #print len(Fk_bin[i])
    ## XOR with left hand side
    
    R[i] = bin(int(Fk_bin[i],2) ^ int(L[i-1],2))[2:]
    
    print ' R ', i , ' is ', R[i]
    ## Store in R[i]
    
    #Repeat
    

print " Not to undo the process"

L[0] = L[4]
R[0] = R[4]
    
    
Fk_hex = ['','','','','']
Fk_bin = ['','','','','']

print L[0]
print R[0]

print len(L)

for i in range(1,2):
    ## Take RHS and store in L[i]    
    print '\n'
    print 'Iteration ', i , ' is as follows '
    print '\n'
    
    L[i] = R[i-1]
    
    print ' L ' , i ,  ' is ' , L[i]
    ## Take right hand side SHA256 it 
    
    #print "R is ", R[i-1]
    
    Fk_hex[i] = hashlib.sha256(R[i-1]).hexdigest()
    
    #print 'Fk ', i, 'hex is ' , Fk_hex[i]
    ## convert to Binary
    #print Fk_hex[i]
    
    for m in range(0,len(Fk_hex[i]), 2):
        
        temp_bin = bin(int(Fk_hex[i][m:m+2],16))[2:]
        
        num_zeros = 8 - len(temp_bin)
        
        j = 0 
        while j < num_zeros:
            temp_bin = '0' +temp_bin
            j +=1
    
        Fk_bin[i] = Fk_bin[i] +temp_bin
    
    print 'Fk  ', i, 'bin is ' , Fk_bin[i] 
    #print len(Fk_bin[i])
    ## XOR with left hand side
    
    R[i] = bin(int(Fk_bin[i],2) ^ int(L[i-1],2))[2:]
    
    print ' R ', i , ' is ', R[i]
    
print 'some stuff'
    

