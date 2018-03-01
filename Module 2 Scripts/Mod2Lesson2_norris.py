import re, urllib


response = urllib.urlopen("http://www.icndb.com/the-jokes-2/")
html = response.read()        #Gets an array of bytes!
strHTML = html.decode()       #Convert to a string

print html

# Find the PRE section


#begin_bin = re.findall('[01]{8}', strHTML)





