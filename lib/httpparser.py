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
    pass