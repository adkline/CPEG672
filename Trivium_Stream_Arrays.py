import math

reg1 = []
reg2 = []
reg3 = []

for i in range (0,80):
    reg1.append(1)
for j in range(0, 13):
    reg1.append(0)
    
for k in range(0, 80):
    reg2.append(1)
for l in range(0, 4):
    reg2.append(0)

for k in range(0, 108):
    reg3.append(0)
for l in range(0, 3):
    reg3.append(1)
    
print len(reg1)
print len(reg2)
print len(reg3)


output = ''

for iterations in range (1, 1312):
    reg1_out = reg1[65]^reg1[92]
    print reg1_out
    
    reg2_out = reg2[68]^reg2[83]
    print reg2_out
    
    reg3_out = reg3[65]^reg3[110]
    print reg3_out

    reg1_in = reg1[68]^(reg3_out^(reg3[108]*reg3[109]))
    print 'reg1_in', reg1_in
    
    reg2_in = reg2[77]^(reg1_out^(reg1[90]*reg1[91]))
    print 'reg2_in',reg2_in
    
    reg3_in = reg3[86]^(reg2_out^(reg2[81]*reg2[82]))
    
    print 'reg3_in', reg3_in
    z_out = reg1_out^reg2_out^reg3_out
    
    print iterations ,  '   gives output', z_out
    
    
    reg1 = [reg1_in] + reg1[:-1]
    reg2 = [reg2_in] + reg2[:-1]
    reg3 = [reg3_in] + reg3[:-1]
   
   
   # print '\n'


    if iterations >= 1152:
        output = output + str(z_out)
    
print output