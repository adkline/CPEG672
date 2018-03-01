import collections, math


#############################################################
def doubles(text):
    doubles_list = []
    doubles_output = {}
    bi = 0
    while bi < len(text):
        if len(text[bi:bi+2]) == 2:
            if ord(text[bi]) == ord(text[bi+1]):
                doubles_list.append(text[bi:bi+2])
        bi = bi+1
    cnt = collections.Counter()
   # print bigrams_list
    
    for item in doubles_list:
        #print item
        cnt[item] += 1
        #print item
    
    #now take all the elements in the counter and put into a normal lsit for ease
    #for item in cnt:
        doubles_output[item] = cnt[item]
    #print bigrams_output
    return cnt

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
    
def grams(text):
    grams_list = []
    grams_output = {}
    gram = 0
    while gram < len(text):
        if len(text[gram]) == 1:
            grams_list.append(text[gram])
        gram = gram+1
    cnt = collections.Counter()
   # print bigrams_list
    
    for item in grams_list:
        #print item
        cnt[item] += 1
    #now take all the elements in the counter and put into a normal lsit for ease
    for item in cnt:
        grams_output[item] = cnt[item]
    #print bigrams_output
    return cnt


def log_list(list) :
# This function takes a list and produces the log frequency of each of the grams in the list, and returns a list of these frequencies, to be used for 
#fitness calculatiosn. 
    total_grams = 0
    gram_frequencies = {}
    gram_logscore = {}
    # Sum over all items to determine total count
    for item in list:
        total_grams = total_grams + list[item]
    
    #print total_grams
    
    for item in list:
       gram_frequencies[item] = (float(list[item])/float(total_grams))
    
    #print gram_frequencies
    
    print ('\n')
    
    for item in list:
        gram_logscore[item] = math.log10(float(list[item])/float(total_grams))
        
    #print gram_logscore
    return gram_logscore

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





### This stuff used for testing. ###################################
encrypted = file('warandpeace.txt', 'r')
encryptedtext = encrypted.read()
#encryptedtext = 'lfnvmbpiofzdfijmiedbkubajzofvgbabpfnfofeztlfefofkyvzbfmvccffdjztflavjdnfimakkunvmzefmmlzbpavbbpfnlzbpbpfnzbmwkiediedwkfibpalyvzcrcanfbpfkfimaemtakiggkaozewlpiblfjzrfnvbmczfecfjzrfbpfmgfikaticpzjjfmciecvkfbpflavedmlpzcppfkmfjtzetjzcbmbanfcaemczavmbpibuavikfzweakiebzmiwkfibmbfgbarealjfdwfidofebvkfkpfbpibwafmavbbanffblpibfofkniucanflfjjbpibzmlpiblfijjdazebpflakjdaefliuakieabpfkeaaefzmfofkbaaajdbadaitaajzmpbpzewbpijjnirfpznjivwpiebpfkfmealbimwaadtakzjjtajrimjivwpzezmnabpfkmiummpfnfjzfofmimpijtipavkmwaadjivwpfofkunakezevdcvkficpigimlimnirzekfidutakbugpvmtfofklfjfiketkantizjvkfeabtkanmvccfmm'
onlyletters = filter(lambda x: x.isalpha(), encryptedtext)
loweronly = onlyletters.lower()

twos_output =  bigrams(loweronly)
threes_output = trigrams(loweronly)
four = quadgrams(loweronly)
dub = doubles(loweronly)


print "For the War and Peace Text"
print dub.most_common(10)
print('Most Comon Bigrams\n')
print twos_output.most_common(10)
print('Most Comon Trigrams\n')
print threes_output.most_common(10)
print('Most Comon Quadgrams\n')
print four.most_common(10)

print ('\n')


encrypted = file('Challange_5.txt', 'r')
encryptedtext = encrypted.read()

#encryptedtext = 'qjememfkqilzgvjwzxvurfhdrfykpiwifhbfuiqiseyzcexwxokdkwestzogawvnziujoewfpihrnpdcpinqqivt'
onlyletters = filter(lambda x: x.isalpha(), encryptedtext)
loweronly = onlyletters.lower()
#print fitnessscore(scorelist, scorelist)

twos_output =  bigrams(loweronly)
threes_output = trigrams(loweronly)
four = quadgrams(loweronly)
dub = doubles(loweronly)
single = grams(loweronly)

print "For the Encrypted Text"
print dub.most_common(10)
print('\n')
print single.most_common(26)
print('Most Comon Bigrams\n')
print twos_output.most_common(20)
print('Most common trigrams\n')
print threes_output.most_common(10)
print('MostCommon Quad\n')
print four.most_common(10)

# key = input('put in the key to try')

# alphabet = 'abcdefghijklmnopqrstuvwxyz' 


def decrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)
    
#print loweronly

