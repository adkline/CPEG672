import operator, collections

d = {'aaaa' : .001, 'bsbc' : .1, 'cdhf' :.05}

sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_d)

print sorted(d.values())