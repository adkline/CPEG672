import math
reg1 = ''
reg2 = ''
reg3 = ''

## Start the first register as noted in module
for i in range (0,80):
    reg1 = reg1+ '1'
for j in range(0, 13):
    reg1 = reg1+ '0'
    
for k in range(0, 80):
    reg2 = reg2+'1'
for l in range(0, 4):
    reg2 = reg2+ '0'

for k in range(0, 108):
    reg3 = reg3+'0'
for l in range(0, 3):
    reg3 = reg3+ '1'
    
# reg1= reg1[2:]
# reg2= reg2[2:]
# reg3= reg3[2:]

print len(reg1), ' ', reg1
print len(reg2), ' ', reg2
print len(reg3), ' ', reg3

# now for the fun part. 

output = ''

for iterations in range (1,85):
    reg1_out = int(reg1[65],2)^int(reg1[92],2)
    print reg1_out
    reg2_out = int(reg2[68],2)^int(reg2[83],2)
    print reg2_out
    reg3_out = int(reg3[65],2)^int(reg3[110],2)
    print reg3_out

    reg1_in = int(reg1[68],2)^int(bin(reg3_out),2)^(int(reg3[108],2)*int(reg3[109],2))
    print 'reg1_in', reg1_in
    
    reg2_in = int(reg2[77],2)^int(bin(reg1_out),2)^(int(reg1[90],2)*int(reg1[91],2))
    print 'reg2_in',reg2_in
    
    reg3_in = int(reg3[86],2)^int(bin(reg2_out),2)^(int(reg2[81],2)*int(reg2[82],2))
    
    print 'reg3_in', reg3_in
    z_out = int(bin(reg1_out),2)^int(bin(reg2_out),2)^int(bin(reg3_out),2)
    
    print iterations ,  '   gives output', z_out
   # print '\n'
    
    #print z_out
    reg1 = reg1[:-1]
    reg1 = str(reg1_in) + reg1
    
    reg2 = reg2[:-1]
    reg2 = str(reg2_in) + reg2
    
    
    reg3 = reg3[:-1]
    reg3 = str(reg3_in) + reg3
    
    print len(reg1), ' ', reg1
    print len(reg2), ' ', reg2
    print len(reg3), ' ', reg3
    #print 'OUTPUT at interation ', iterations, ' == ', z_out
    

    #print len(reg1), len(reg2), len(reg3)
    
    if iterations >= 1152:
        output = output + str(z_out)
        

#print output
#if reg1_in == 0:
    
    #Shift and add 0