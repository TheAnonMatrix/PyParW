#!/usr/bin/env python
# -*- coding: UTF-8 -*

import urllib
import urllib2
from lib.httpfetch import HTTP
from base64 import b64encode
from bs4 import BeautifulSoup
import os


url = "http://wikileaks.org/syria-files/docs/2089579_.html"
req = urllib2.Request(url)
response = urllib2.urlopen(req)
source = response.read()

print source

soup = BeautifulSoup(source)

header = soup.find(text="Email-ID")
print header.next_element.next_element.get_text()
dictt = {"Email-ID": "", "Date": "", "From": "", "To": "", "Title": "", "Body": "", "Attachment"}
for k in dictt.keys():
    if k == "Title" or k == "Body":
        pass
    else:
        headerinf = soup.find(text=k)
        dictt[k] = headerinf.next_element.next_element.get_text()
subject = soup.find("h2")
body = soup.find(id="doc-description")

dictt["Title"] = subject.get_text()
dictt["Body"] = body.get_text()

if soup.find(id="file-list"):
    source = soup.find(id="file-list")
    for link in source.find_all('a')
        file = HTTP("http://wikileaks.org"+link.get('href').encode('utf-8'))
        path = os.getcwd()
        dictt['Attachment'].append(file)
return dictt