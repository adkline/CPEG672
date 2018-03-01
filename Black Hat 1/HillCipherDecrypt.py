import math, random, collections, itertools

def extendgcd(a,b):
        
    if b == 0: 
        return a
    else:
    
        i = 2
        r = []
        r.append(a)
        r.append(b)
        
        q = []
        q.append(0)
        q.append(0)
        
        s = []
        s.append(1)
        s.append(0)
        
        t = []
        t.append(0)
        t.append(1)
        
        
        while r[i-1] != 0:
            
            q.append(r[i-2]/r[i-1])
            r.append(r[i-2]%r[i-1])
 
            s.append(s[i-2]-q[i]*s[i-1])
            t.append(t[i-2]-q[i]*t[i-1])
            
            i = i+1
    found = 0 
    
    for i in range(0, len(r)):    
        if r[i] == 1:
            found = 1
            out = s[i]
    if found == 0: 
        out = 0
    
    return  out
    
def bigrams(text):
    bigrams_list = []
    bigrams_output = {}
    bi = 0
    while bi < len(text):
        if len(text[bi:bi+2]) == 2:
            
            bigrams_list.append(text[bi:bi+2])
        bi = bi+1
    cnt = collections.Counter()
   # print bigrams_list
    
    for item in bigrams_list:
        #print item
        cnt[item] += 1
        #print item
    
    #now take all the elements in the counter and put into a normal lsit for ease
    #for item in cnt:
        bigrams_output[item] = cnt[item]
    #print bigrams_output
    
    
    return cnt  

def quadgrams(text):
    quadgrams_list = []
    quadgrams_output = {}
    quad = 0
    while quad < len(text):
        if len(text[quad:quad+4]) == 4:
            quadgrams_list.append(text[quad:quad+4])
        quad = quad+1
    cnt = collections.Counter()
   # print bigrams_list
    
    for item in quadgrams_list:
        #print item
        cnt[item] += 1
        #print item
    return cnt
    
def rel_freq(list) :
# This function takes a list and produces the relative frequency  of each of the grams in the list, and returns a list of these frequencies, to be used for 
#fitness calculations. 
    total_grams = 0
    gram_frequencies = {}
    # Sum over all items to determine total count
    for item in list:
        total_grams = total_grams + list[item]
    #print total_grams
    for item in list:
       gram_frequencies[item] = (float(list[item])/float(total_grams))

    #print gram_logscore
    return gram_frequencies

def fitnessscore(testlist, trainlist):
    #to get a fitness score of the input testlist (input as a list of "grams and their relative frequencies (based on total grams)" )
    # find the corresponding value in the training list and their relative frequencies
    
    fitness = 0
    for item in testlist:
        if item in trainlist:
            fitness = fitness + abs(math.log10((float(testlist[item])/float(trainlist[item]))))
        
        ### Add a ton if we aren't in the list!!!!    
        if item not in trainlist:
             fitness = fitness + 0.9
            
    return fitness

def decryptHill_2by2(text, key):
  
    decryptedout = ''
    # Find the inverse of the key. TO do this, we find det and find it's gcd with 26. 
    # this is then multiplied by each element per ususla in invere
    
    det = (key[0][0]*key[1][1]-key[0][1]*key[1][0])
    
    multiplier = extendgcd(det,26)
    
    print multiplier
    
    KeyInv = [[key[1][1]*multiplier%26, -key[0][1]*multiplier%26],[-key[1][0]*multiplier%26, key[0][0]*multiplier%26]]
    print KeyInv
    
    decrypted = ''
    for i in range(0,len(text),2):
        
        #Add some shifting if text length isn't even
        #temptext = numpy.array([[ord(text[i])-97], [ord(text[i+1])-97]])
       # temp = numpy.dot(KeyInv, temptext)%26
        
        temp1 = (KeyInv[0][0]*(ord(text[i])-97)+KeyInv[0][1]*(ord(text[i+1])-97))%26
        temp2 = (KeyInv[1][0]*(ord(text[i])-97)+KeyInv[1][1]*(ord(text[i+1])-97))%26
        
        
        decrypted = decrypted +(chr(temp1+97))+(chr(temp2+97))
        print decrypted
    
    return decrypted


def decryptHill_2by2_input(text, str1, str2):
  
    decryptedout = ''
    # Find the inverse of the key. TO do this, we find det and find it's gcd with 26. 
    # this is then multiplied by each element per ususla in invere
    #compare the two input strings against the matrix of "th" and "he"
    
    th_he = [[4, -7], [-7,19]]
 
    #input_text = [[ord(str1[0])-97, ord(str1[1])-97], [ord(str2[0])-97, ord(str2[1])-97]]
    
    input_text = [[ord(str1[0])-97, ord(str2[0])-97], [ord(str1[1])-97, ord(str2[1])-97]]
    
    print input_text
    
    key = [[(input_text[0][0]*th_he[0][0]+input_text[0][1]*th_he[1][0])%26,(input_text[0][0]*th_he[0][1]+input_text[0][1]*th_he[1][1])%26],[(input_text[1][0]*th_he[0][0]+input_text[1][1]*th_he[1][0])%26,(input_text[1][0]*th_he[0][1]+input_text[1][1]*th_he[1][1])%26]]
    
    print "the Key is ",  key
    #now find the inverse of the key

    det = (key[0][0]*key[1][1]-key[0][1]*key[1][0])
    
    multiplier = extendgcd(det,26)
    
    KeyInv = [[key[1][1]*multiplier%26, -key[0][1]*multiplier%26],[-key[1][0]*multiplier%26, key[0][0]*multiplier%26]]
    print KeyInv
    
    decrypted = ''
    for i in range(0,len(text),2):
        
        #Add some shifting if text length isn't even
        #temptext = numpy.array([[ord(text[i])-97], [ord(text[i+1])-97]])
       # temp = numpy.dot(KeyInv, temptext)%26
        
        temp1 = (KeyInv[0][0]*(ord(text[i])-97)+KeyInv[0][1]*(ord(text[i+1])-97))%26
        temp2 = (KeyInv[1][0]*(ord(text[i])-97)+KeyInv[1][1]*(ord(text[i+1])-97))%26
        
        
        decrypted = decrypted +(chr(temp1+97))+(chr(temp2+97))
        #print decrypted
    
    return decrypted

cipher = 'nyulfzvuxifotokikubupmwlzgxvsgrdlsibnxbqulckpdjpsznyyfiysshghepehjdkkuemlqbukysgzkgqdcejawidooxrbumeuulofzlsjqbqtgkujudjrmaxwavzzvagzqfmckmqjrldcukuchftgorakubqpeszbqyrbqncbqulldcukubqyrnylfiybuochglshelusgdcullddjpzjtyuanhtagnksidqnnzixibbnnmqulhtrmaxwavzzvagaxrdyuanhtnttpbqbmfmulkikyswnnzikvbbhjepyonnagvziupkrsaxbobqbmfmckftmqcihtgoibiypebsnyhgulhtiyhgdculprzwjomoemutqwyskewtptkikuhekecqsitskedculhthvldkijulfqylfiyczzdgofmlfiyjivlkedueakuzvdzhtxvbbxuzklqpkzksznnnokugipdszzkgqmqnlwmylpmeqhtgyqadkulwqzpwqbbshsghjjofitpmqimkuemcxvlqumqnlwmurkidjxutgkuemanhfnghgpekvvlquvvkuidkirmprbqiubuqytehjae'
#inkey = [[25, 22], [2, 13]]
#tempdecrypted = decryptHill_2by2_input(cipher, 'xa', 'sv')
#print tempdecrypted
#print decryptHill_2by2('fzyqdoyqcncidmtxadhwkddobidokesdkmtozmqccikcdzgakvmpfxkiqofacqokpoobttwibnsdrmtikxsdwzcihmdo', inkey )

############Set up our training set for english as war and peace

trainset = file('warandpeace.txt', 'r')

trainsettext = trainset.read()
trainletters = filter(lambda x: x.isalpha(), trainsettext)
trainlower = trainletters.lower()

trainquad = quadgrams(trainlower)
trainrelfreq = rel_freq(trainquad)



#key = [[17, 12], [0,5]]

cipherbi = bigrams(cipher)
cipherbi = cipherbi.most_common(60)
print " The most common bigrams are ", cipherbi 

# take all the items in bigrams list, and iterate over all possible permutations 
test_list = []

#stopcode = input('put somethings here')
for item in cipherbi:
    test_list.append(item[0])
    
#print "Bigrams without frequencies are " , test_list

score_old = 99999999

filedumper = file('HillOUt', 'a')

for items in itertools.permutations(test_list,2):
    # print items[0]
    # print items[1]

    # Now input these strings into the decyrpter and get a score
    str1 = items[0]
    str2 = items[1]
    
    print str1
    print str2
    filedumper = file('HillOUt', 'a')
    
    tempdecrypted = decryptHill_2by2_input(cipher, str1, str2)
    
    output = 'Possible solution is below using  ' + str1 + '  '+ str2
    
    filedumper.write(output)
    filedumper.write('\n')
    filedumper.write(tempdecrypted)
    filedumper.write('\n')
    
    workingquad = quadgrams(tempdecrypted)
    workingfreq = rel_freq(workingquad)
    
    score = fitnessscore(workingfreq,trainrelfreq)
            
    if score <=  score_old: 
        print "Possible Text with score ", score
        print ('\n')
        print tempdecrypted
        print ('\n')
      
        score_old=score
    filedumper.close()

