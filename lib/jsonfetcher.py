#!/usr/bin/env python
# -*- coding: UTF-8 -*

import os
import json

class FileInfo(object):
	"""Opens a file containing a json to pass used urls"""
	def __init__(self):
		self.path = os.getcwd()
		self.jsondict = {'source': [], 'urls': []}

	def check(self):
		f = open(self.path+"/output/info", "rb")
		fread = f.read()
		try:
			ret = json.loads(fread)
		except ValueError:
			ret = self.jsondict
		f.close()
		return ret

	def json_add(self, source=None, urls=None):
		if source:
			self.jsondict['source'].append(source)
		if urls:
			self.jsondict['urls'] = urls
		self.jsonwrite()

	def jsonwrite(self):
		f = open(self.path+"/output/info", "wb")
		ret = json.dumps(self.jsondict, indent=4)
		f.write(ret)
		f.close()
		