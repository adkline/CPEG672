Encrypted = input('Enter the Encrypted text ')

Working_Text = Encrypted.replace(' ', '')
Num_enc = []

print Working_Text

length=len(Working_Text)

Alpha = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

y=0
i = 0
while i <= length-1:
    while y < 26:
        if  Working_Text[i] == Alpha[y]:
            Num_enc.append(y)    
        y = y+1
       
    y = 0
    i= i+1

k = 0

while k < 26:
    num_mod = []
    decrypted = []
    i = 0
    while i <= length-1:
        num_mod.append((Num_enc[i]-k)%26)
        i = i+1
        
    i = 0
    
    f = file('Decrypted.txt', 'a')
    
    while i <= length-1:
        
        decrypted.append(Alpha[num_mod[i]])
        f.write(decrypted[i])
        i = i+1  
        
    f.write("\n")
    f.close
    k = k+1
    
    
    


    




