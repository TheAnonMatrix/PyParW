#!/usr/bin/env python
# -*- coding: UTF-8 -*

class Variables(object):
	"""Stores variables to be used in other modules"""
	def __init__(self):
		self.variables = {}

	def add(self, **kwargs):	
		for i, k in kwargs.items():
			self.variables[i] = k

	def get(self, var):
		try:
			return self.variables[var]
		except KeyError:
			return ""

	def get_all(self):
		fetched = self.variables.copy()
		try:
			del fetched['output']
		except:
			return fetched
		else:
			return fetched

VARIABLES = Variables()