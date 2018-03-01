import math
sub_group = []

for x in range(0,100):
    
   
    sub_group_element = 3*x % 10 
    
    print ' sub group is ', sub_group_element
    print x
    
    if sub_group_element in sub_group:
      break 
    
    if sub_group_element not in sub_group:
        sub_group.append(sub_group_element)
       
        
print len(sub_group)
    
    