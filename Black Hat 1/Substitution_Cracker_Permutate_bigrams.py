import urllib2, random, itertools, collections, re, sys, time, math

def decrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)
    
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

def quadgrams(text):
    # input is text and how many grams we want to have (100??)
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
    
    #now take all the elements in the counter and put into a normal lsit for ease
    for item in cnt:
        quadgrams_output[item] = cnt[item]
    #print bigrams_output
    return quadgrams_output



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

def trigrams(text):
    trigrams_list = []
    trigrams_output = {}
    tri = 0
    while tri < len(text):
        if len(text[tri:tri+3]) == 3:
            trigrams_list.append(text[tri:tri+3])
        tri = tri+1
    cnt = collections.Counter()
   # print bigrams_list
    
    for item in trigrams_list:
        #print item
        cnt[item] += 1
        #print item
    
    #now take all the elements in the counter and put into a normal lsit for ease
    for item in cnt:
        trigrams_output[item] = cnt[item]
    #print bigrams_output
    return cnt



#### Read in the training set for the fitness

trainset = file('warandpeace.txt', 'r')

trainsettext = trainset.read()
trainletters = filter(lambda x: x.isalpha(), trainsettext)
trainlower = trainletters.lower()

trainbi = bigrams(trainlower)
trainquad = quadgrams(trainlower)
trainrelfreq = rel_freq(trainquad)


encrypted = file('Challange_1.txt', 'r')
encryptedtext = encrypted.read()
#encryptedtext = 'lfnvmbpiofzdfijmiedbkubajzofvgbabpfnfofeztlfefofkyvzbfmvccffdjztflavjdnfimakkunvmzefmmlzbpavbbpfnlzbpbpfnzbmwkiediedwkfibpalyvzcrcanfbpfkfimaemtakiggkaozewlpiblfjzrfnvbmczfecfjzrfbpfmgfikaticpzjjfmciecvkfbpflavedmlpzcppfkmfjtzetjzcbmbanfcaemczavmbpibuavikfzweakiebzmiwkfibmbfgbarealjfdwfidofebvkfkpfbpibwafmavbbanffblpibfofkniucanflfjjbpibzmlpiblfijjdazebpflakjdaefliuakieabpfkeaaefzmfofkbaaajdbadaitaajzmpbpzewbpijjnirfpznjivwpiebpfkfmealbimwaadtakzjjtajrimjivwpzezmnabpfkmiummpfnfjzfofmimpijtipavkmwaadjivwpfofkunakezevdcvkficpigimlimnirzekfidutakbugpvmtfofklfjfiketkantizjvkfeabtkanmvccfmm'
onlyletters = filter(lambda x: x.isalpha(), encryptedtext)
loweronly = onlyletters.lower()
normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

frequency = {}
for ascii in range(ord('a'), ord('a')+26):
    frequency[chr(ascii)] = float(encryptedtext.count(chr(ascii)))/len(loweronly)

sum_freqs_squared = 0.0
for ltr in frequency:
    sum_freqs_squared += frequency[ltr]*frequency[ltr]

possible_keysets = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

temp_key_dict = {}


l = 0
for letters in range(ord('a'), ord('a')+26):
    tempstring = ''
    tempvalues = []
    temp_key_dict = {}
    #Loop through the knwon frequencies
    for alpha in range(ord('a'), ord('a')+26):
        
        if abs(frequency[chr(letters)] - normal_freqs[chr(alpha)]) < .018:
           ## print a found value
            print "A possible substituion for the letter " , chr(letters), " is ", chr(alpha), "With closeness of " , abs(frequency[chr(letters)] - normal_freqs[chr(alpha)])
            # put the letter in a temp string
            
            tempstring = tempstring + possible_keysets[(letters)-97] + chr(alpha)
            # put the value into an array to sort later.
            
            tempvalues.append(abs(frequency[chr(letters)] - normal_freqs[chr(alpha)]))
            # add to dict
            
            temp_key_dict[chr(alpha)] = abs(frequency[chr(letters)] - normal_freqs[chr(alpha)])
            
    # sort our values
    tempvalues.sort()
    tempvalues = tempvalues[:6]
    
    print tempvalues
    print tempstring
    #loop through
    sortedkeys = ''
    for pos in range(0,len(tempvalues)):
      for char in range(0,len(tempstring)): 
        if temp_key_dict[tempstring[char]] == tempvalues[pos]:
            sortedkeys = sortedkeys + (tempstring[char])
      
    
    possible_keysets[(letters)-97] = sortedkeys

print('\n')   

print possible_keysets, ' With a length of ' , len(possible_keysets)

print('\n')

cipherbis = bigrams(loweronly)
print cipherbis.most_common(40)
print trainbi.most_common(25)

old_testkey = ''
score_old = 999999999
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
iteration = 0

testbis = cipherbis.most_common(40)
trainbigrams =trainbi.most_common(25)
trainbigrams_list = []
print trainbigrams

for item in trainbigrams:
    temp = item[0]
    tempstr = ''
    for i in range(0,len(temp)):
        tempstr = tempstr+ chr(ord(temp[i])-32)
    
    trainbigrams_list.append(tempstr)

print trainbigrams_list
print testbis


for testset in itertools.permutations(trainbigrams_list):
    decrypted =''
    
    for i in range(0,len(testset)): 
        decypted = decrypted.replace(testbis[i][0],testset[i])
        
    
    print decrypted
    decrypted = decrypted.lower()
    decrypted_4grams = quadgrams(decrypted)
    decrypted_4gramsrefreq= rel_freq(decrypted_4grams)
    
    score = fitnessscore(decrypted_4gramsrefreq,trainrelfreq)
        
    if score <  score_old: 
       
        print "Possibly decrypted"
        print decrypted[:100]
        print ('\n')
        print decrypted
        print ('\n')
        score_old=score
        print iteration

            
    iteration +=1
    
    
    