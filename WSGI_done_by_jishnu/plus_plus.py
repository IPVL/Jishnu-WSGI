#! /usr/bin/env python

class PlusPlus:
	def __init__(self, app):
		self.app = app
	def __call__(self, environ, start_response):
		print 'abcd'
		for i in self.app(environ, start_response):
			yield i

def add(app, global_config):
	return PlusPlus(app)
