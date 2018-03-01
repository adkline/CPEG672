import urllib2, random, itertools, math, collections

def shiftBy(c, n):
        return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))

def decryptby(c, n):
        return chr(((ord(c) - ord('a') - n) % 26) + ord('a'))

normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}


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
    
### import the challange ciphered text    
f = file('Challange_4.txt', 'r')
Encrypted = f.read()
Working_Text = Encrypted.replace(' ', '')
text_length = len(Working_Text)


## Find the "4grams" for fitness score
trainset = file('warandpeace.txt', 'r')

trainsettext = trainset.read()
trainletters = filter(lambda x: x.isalpha(), trainsettext)
trainlower = trainletters.lower()

#trainbi = bigrams(trainlower)
trainquad = quadgrams(trainlower)
trainrelfreq = rel_freq(trainquad)

#keyset = [8, 11, 14, 24, 3, 11, 20, 22, 8, 19, 8 , 11, 14, 24, 3, 11, 20, 22, 8, 19 ]


#possible_keyset = [[8, 23], [11], [14], [9, 11, 24], [3, 18], [1, 11], [7, 20], [7, 22], [8, 12], [4, 7, 8, 19], [4, 8, 15], [11, 24], [14], [9, 24], [3, 18], [11], [7, 16, 20], [22], [8, 12], [15, 19]]

possible_keyset = [[8, 23], [11], [14], [24], [3], [1, 11], [7, 20], [22], [8, 12], [4, 8, 19], [4, 8, 15], [11, 24], [14], [24], [3, 18], [11], [7, 20], [22], [8], [15, 19]]
#Now the fun part... decrypting!!
D = file('Decrypted.txt', 'w')
key = 20

##W Set our inital score reaaaally high - Score 0 is "perfect"

score_old = 99999999999


for item in itertools.product(*possible_keyset):
  plain = ''
  D = file('Decrypted.txt', 'a')
  keyset = item
  q = 0
  while q < text_length:
      
    #  Figure out the shift 
    y=q%key
    s = keyset[y]
    #D.write(decryptby(Working_Text[q],s) ) 
    plain = plain + decryptby(Working_Text[q],s)
    q = q+1
    
  #print plain
#D.close()
  
  decrypted_ngrams = quadgrams(plain)
  decrypted_ngramsrefreq= rel_freq(decrypted_ngrams)
        
  score = fitnessscore(decrypted_ngramsrefreq, trainrelfreq)  
  
  
  if score <=  score_old: 
    print "Possible new key ", item,  "with score ", score
    print ('\n')
    print ('\n')
    print plain
    score_old=score
    D.write('\n')
    D.write(plain) 
    D.close()
    
  
  

