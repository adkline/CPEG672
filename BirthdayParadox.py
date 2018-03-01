import math, random

def prob_share(n):

    prob = 1

    for i in range(1,n+1):
    
        prob = float(prob) *float((365-i)/float(365))
           
    
    return prob

print prob_share(22)



def collisions(n):

    for j in range(1,n+1):
        
        print "For attempt ", j
       
        random_set = []
        
        rand = random.randint(1,10000)  
        i = 0
        
        while rand not in random_set:
            i += 1
            random_set.append(rand) 
            rand = random.randint(1,10000)  
        
        print "A collision occured at iteration : ", i
    return 
    

print collisions(25)