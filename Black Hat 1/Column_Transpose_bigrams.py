import urllib2, random, collections, re, sys, time, itertools, math

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

## Columns are of between 8 - 10 columns
## Challange 3

cipher = file('Challange_3.txt', 'r')
ciphertext = cipher.read()

possible_permutations = 10
Columns = []

ColumnLength_Float = (float(len(ciphertext))/float(possible_permutations))
ColumnLength = (len(ciphertext)/possible_permutations)

print "The length of the cipher text is " , len(ciphertext)
print "Divided by the number of permutations ", possible_permutations, " = ", ColumnLength_Float

#Check column lengths, if input text not divisible by possible permutations, add 1 to the length

if ColumnLength_Float - float(ColumnLength) != 0:
    print "We must add one to the column length to account for non - divisibility"
    ColumnLength = ColumnLength +1


i = 0
while i < len(ciphertext):
    Columns.append(ciphertext[i:i+ColumnLength])
    i = i+ColumnLength

print Columns
print len(Columns)
    
# Loop through columns and create text file from each string

#WorkingColumn = file("WorkingColumn_Text.txt", 'a')

WorkingColumn = ''

# now permutate through each iteration of column arrangement
score_old = 9999999

trainset = file('warandpeace.txt', 'r')

trainsettext = trainset.read()
trainletters = filter(lambda x: x.isalpha(), trainsettext)
trainlower = trainletters.lower()

trainbi = bigrams(trainlower)
trainrelfreq = rel_freq(trainbi)


output  = file('Challange_3_out.txt', 'a')


for item in itertools.permutations(Columns):
    p = 0
    WorkingColumn = ''
    # Put the text into a file. 
    # This is too much computation....
    # take and look at each "first letter"
    # # then get a fitness score
    
   
    #WorkingColumn.write('\n')
    # #compute a fitness score
    #   workingquad = quadgrams(WorkingColumn)
    # workingfreq = rel_freq(workingquad)
    numrows = 11
    testorder = ''
    for j in range(0, numrows):
        for i in range(0,len(item)):
            testorder = testorder + item[i][j]
      
    testbi = bigrams(testorder)
    testbifreq = rel_freq(testbi) 
    
    score = fitnessscore(testbifreq,trainrelfreq)
            
    if score <=  score_old: 
        n = 0
        m = 0
        while m < ColumnLength:
            n= 0
            while n < len(item):
                #check if out position is in "item", add to working text
                if m < len(item[n]):
                    WorkingColumn = WorkingColumn + item[n][m]
                n = n+1
            m = m+1
            
        print "Possible Text with score ", score
        print ('\n')
        print WorkingColumn
        print ('\n')
      
        score_old = score
#workingColumn.close()

#COmpute the n grams for the working text

#WorkingColumn = file("WorkingColumn_Text.txt", 'r')






