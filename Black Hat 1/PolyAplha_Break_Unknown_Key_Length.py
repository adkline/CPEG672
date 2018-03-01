import urllib2, random

def shiftBy(c, n):
        return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))

def decryptby(c, n):
        return chr(((ord(c) - ord('a') - n) % 26) + ord('a'))

normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

f = file('Challange_4.txt', 'r')
Encrypted = f.read()
Working_Text = Encrypted.replace(' ', '')
text_length = len(Working_Text)


keylimit = 20
key = 20

possible_keyset= [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

print len(possible_keyset)

while key <= keylimit:

    print("Testing Key Length of ", key)

    keyset = []
    
    k=0
    i = 0
    
    while k < key:
        i = k
        M = file('Sorted_Text.txt', 'w')
        while i <= text_length:
            if i < text_length:
                M.write(Working_Text[i])
            i = i+key
        
        M.close()
        
        response = file('Sorted_Text.txt', 'r')
        Crypto = response.read()
        
        onlyletters = filter(lambda x: x.isalpha(), Crypto)
        loweronly = onlyletters.lower()
        
        frequency = {}
        for ascii in range(ord('a'), ord('a')+26):
            frequency[chr(ascii)] = float(loweronly.count(chr(ascii)))/len(loweronly)
    
        sum_freqs_squared = 0.0
        for ltr in frequency:
            sum_freqs_squared += frequency[ltr]*frequency[ltr]
    
        for possible_key in range(1, 26):
            sum_f_sqr = 0.0
            for ltr in normal_freqs:
                caesar_guess = shiftBy(ltr, possible_key)
                sum_f_sqr += normal_freqs[ltr]*frequency[caesar_guess]
            if abs(sum_f_sqr - .065) < .013:
                print "Key is probably: ", possible_key, "for the ", k, "th letter", " f_sqr is ",sum_f_sqr
                keyset.append(possible_key) 
                possible_keyset[k].append(possible_key)
        k = k+1
        
    print keyset

    key = key+1

print possible_keyset