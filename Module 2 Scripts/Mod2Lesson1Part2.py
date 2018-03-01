import math
i = 0

test_list = []

print "Group is equal to "
for i in range(1, 23):
    test_list.append(i)
    
    
print test_list  
print len(test_list)

for j in test_list:
    sub_group = []
    stop = 0
    sub_group.append(j)
    sub_group_element = j
    ''
    while stop == 0:
        sub_group_element = (sub_group_element*sub_group_element) % 23
        
        if sub_group_element in sub_group:
            stop = 1  
        
        if sub_group_element not in sub_group:
            sub_group.append(sub_group_element)
            i = i+1
        
       
    
    print sub_group
    print "Length of " , len(sub_group)
    
    sub_group = []