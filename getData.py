from bs4 import BeautifulSoup
import json
import urllib2

import requests 
r = urllib2.urlopen('http://www.morewords.com/contains/ch/').read()

soup = BeautifulSoup(str(r))
data=soup.find_all("a")
print data
#data = data[2:]
f=file("wordLogiostem.txt","w")
for a in data:
    if 'href="/word/' in str(a):
        print str(a).split(">")[1].split("<")[0]
        f.write(str(a).split(">")[1].split("<")[0]+"\n")

f.close()
        