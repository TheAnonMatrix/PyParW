#!/usr/bin/env python
# -*- coding: UTF-8 -*

import urllib
import urllib2
import os

def HTTP(url):
    while True:
        try:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
        except:
            print "Lost connection to wikileaks! retrying connection!"
        else:
            source = response.read()
            return source