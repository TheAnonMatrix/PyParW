#!/usr/bin/env python
# -*- coding: UTF-8 -*

from bs4 import BeautifulSoup

def LinkFetch(source):
    soup = BeautifulSoup(source)
    newsoup = soup.find("table","cable")
    parsed = []
    for link in newsoup.find_all('a'):
        n = link.get('href')
        parsed.append(n)
    parsed = sorted(set(parsed))
    return parsed

def mailparse(source):
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
            dictt['Attachment'].append(b64encode(file))
    return dictt