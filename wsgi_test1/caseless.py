#! /usr/bin/env python
class Caseless:

	def __init__(self, app):
		print 'Caseless : __init__ : first'
		self.app = app

	def __call__(self, environ, start_response):
		print 'Caseless : __call__ : first'
		#print 'name -> '+ self.name
		for chunk in self.app(environ, start_response):
			yield chunk.lower()


def filter_factory(app, global_config):
	print 'wer'
	return Caseless(app)
