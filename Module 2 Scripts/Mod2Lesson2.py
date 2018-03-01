import re, urllib


response = urllib.urlopen("http://www.befria.nu/elias/pi/binpi.html")
html = response.read()        #Gets an array of bytes!
strHTML = html.decode()       #Convert to a string

print strHTML

# Find the PRE section


begin_bin = re.findall('[01]{8}', strHTML)

#print begin_bin

print begin_bin[0]



