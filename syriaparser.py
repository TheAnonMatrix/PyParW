#!/usr/bin/env python
# -*- coding: UTF-8 -*

from lib.httpparser import LinkFetch
from lib.httpparser import mailparse
from lib.httpfetch import HTTP
from lib.jsonfetcher import FileInfo
from lib.emlwrite import EMLWriter
import os

def main():
    source = HTTP("http://wikileaks.org/syria-files/releases.html")
    links = LinkFetch(source)
    jsonclass = FileInfo()
    json = jsonclass.check()
    for i in links:
        if i not in json['source']:
            source = HTTP("http://wikileaks.org"+i)
            linksn = LinkFetch(source)
            jsonclass.json_add(source=i)
            for n in linksn:
                if n not in json['urls']:
                    source = HTTP("http://wikileaks.org"+n)
                    mail = mailparse(source)
                    EMLWriter(mail)
                    jsonclass.json_add(urls=n)
        pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.exit()