import urllib2, random, collections, re, sys, time

#response = urllib2.urlopen("http://vip.udel.edu/crypto/encrypted_mobydick.txt")

response = file('Challange_5.txt', 'r')
warandpeace = response.read()
onlyletters = filter(lambda x: x.isalpha(), warandpeace)

onlyletters = onlyletters.replace(' ', '')
loweronly = onlyletters.lower()


string = loweronly

def bigrams(text):
    bigrams_list = []
    bi = 0
    while bi < len(text):
        bigrams_list = text[bi,bi+1]
        bi = bi+1
        
    return bigrams_list

def count_ngrams(lines, min_length=2, max_length=2):
    """Iterate through given lines iterator (file object or list of
    lines) and return n-gram frequencies. The return value is a dict
    mapping the length of the n-gram to a collections.Counter
    object of n-gram tuple and number of times that n-gram occurred.
    Returned dict includes n-grams of length min_length to max_length.
    """
    lengths = range(min_length, max_length + 1)
    
    ngrams = {length: collections.Counter() for length in lengths}
    print 'Test ings'   
    print ngrams
    
    queue = collections.deque(maxlen=max_length)

    # Helper function to add n-grams at start of current queue to dict
    def add_queue():
        current = tuple(queue)
        for length in lengths:
            if len(current) >= length:
                ngrams[length][current[:length]] += 1

    # Loop through all lines and words and add n-grams to dict
    for line in lines:
        for word in tokenize(line):
            queue.append(word)
            if len(queue) >= max_length:
                add_queue()

    # Make sure we get the n-grams at the tail end of the queue
    while len(queue) > min_length:
        queue.popleft()
        add_queue()

    return ngrams


def print_most_frequent(ngrams, string, num= 25):
    ngram_list ={}
    """Print num most common n-grams of each length in n-grams dict."""
    for n in sorted(ngrams):
       # print('----- {} most common {}-grams -----'.format(num, n))
        
        for gram, count in ngrams[n].most_common(num):
            print('{0}: {1}'.format(' '.join(gram), float(count)/float(len(string))))
            tempstring = (''.join(gram))
            # log likelihood
            #count the 
            percent = float(count)/float(len(string))
            #print tempstring
            ngram_list[tempstring] = percent
        print('')
        
     
    return ngram_list


ngrams = count_ngrams(string)

#print_most_frequent(ngrams, string)

ngrams = print_most_frequent(ngrams, string)
 
print ngrams 

## Now we clear out the working text.

#WorkingColumn = file("WorkingColumn_Text.txt", 'r')



    