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

#### Read in the training set for the fitness

trainset = file('warandpeace.txt', 'r')

trainsettext = trainset.read()
trainletters = filter(lambda x: x.isalpha(), trainsettext)
trainlower = trainletters.lower()

trainquad = quadgrams(trainlower)
trainrelfreq = rel_freq(trainquad)


##### Code is below
encrypted = file('Challange_1.txt', 'r')
encryptedtext = encrypted.read()
#encryptedtext = 'lfnvmbpiofzdfijmiedbkubajzofvgbabpfnfofeztlfefofkyvzbfmvccffdjztflavjdnfimakkunvmzefmmlzbpavbbpfnlzbpbpfnzbmwkiediedwkfibpalyvzcrcanfbpfkfimaemtakiggkaozewlpiblfjzrfnvbmczfecfjzrfbpfmgfikaticpzjjfmciecvkfbpflavedmlpzcppfkmfjtzetjzcbmbanfcaemczavmbpibuavikfzweakiebzmiwkfibmbfgbarealjfdwfidofebvkfkpfbpibwafmavbbanffblpibfofkniucanflfjjbpibzmlpiblfijjdazebpflakjdaefliuakieabpfkeaaefzmfofkbaaajdbadaitaajzmpbpzewbpijjnirfpznjivwpiebpfkfmealbimwaadtakzjjtajrimjivwpzezmnabpfkmiummpfnfjzfofmimpijtipavkmwaadjivwpfofkunakezevdcvkficpigimlimnirzekfidutakbugpvmtfofklfjfiketkantizjvkfeabtkanmvccfmm'
onlyletters = filter(lambda x: x.isalpha(), encryptedtext)
loweronly = encryptedtext.lower()

normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

frequency = {}
for ascii in range(ord('a'), ord('a')+26):
    frequency[chr(ascii)] = float(encryptedtext.count(chr(ascii)))/len(loweronly)

sum_freqs_squared = 0.0
for ltr in frequency:
    sum_freqs_squared += frequency[ltr]*frequency[ltr]

possible_keysets = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

l = 0
for letters in range(ord('a'), ord('a')+26):
    #Loop through the knwon frequencies
    for alpha in range(ord('a'), ord('a')+26):
        if abs(frequency[chr(letters)] - normal_freqs[chr(alpha)]) < .018:
           # keys.write(chr(alpha)) 
            tempstring =  possible_keysets[(letters)-97] + chr(alpha)
            possible_keysets[(letters)-97] =  tempstring
            #print "A possible substituion for the letter " , chr(letters), " is ", chr(alpha), "With closeness of " , abs(frequency[chr(letters)] - normal_freqs[chr(alpha)])
            l = l+1

print possible_keysets


alphabet = 'abcdefghijklmnopqrstuvwxyz'


#pick randomly a key from the possible keys
num_times = 0
score_old = 0

# Generate a random key based on the possible key sets
letters= range(26)
random.shuffle(letters)

print letters

for i in range(26):
    pt = chr(65+i)
    test_key = alphabet.replace(pt, chr(97+letters[i]))

old_testkey = test_key
score = 0

decrypted =  decrypt(loweronly, test_key, alphabet)
decrypted_ngrams = quadgrams(decrypted)
decrypted_ngramsrefreq= rel_freq(decrypted_ngrams)
        
old_score = fitnessscore(decrypted_ngramsrefreq, trainrelfreq)      

print ' The first test key is' , old_testkey
print ('\n')

print decrypted
print old_score


while num_times <= 5000000:
    t = random.randint(0,25)
    s = random.randint(0,25)
    temp_key = list(test_key)
    
    temp_s = test_key[s] 
    temp_t = test_key[t]

    temp_key[s] = temp_t
    temp_key[t] = temp_s
    test_key = "".join(temp_key)
    
    decrypted =  decrypt(loweronly, test_key, alphabet)
    
    decrypted_ngrams = quadgrams(decrypted)
    decrypted_ngramsrefreq= rel_freq(decrypted_ngrams)
        
    score = fitnessscore(decrypted_ngramsrefreq, trainrelfreq)   
    #print score 
    
    #print score
    
    if old_score >=  score: 
        print "Possible new key ", test_key,  "with score ", score
        print ('\n')
        print decrypted
        print ('\n')
        old_testkey = test_key
        old_score = score
        
    if score > old_score:
        test_key = old_testkey
        #print ('\n')
    
    

            

    
    
    num_times = num_times+1
    