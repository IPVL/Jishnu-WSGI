#! usr/bin/env python

class Connection:
	def __init__(self,one,two):
		self.one = one+two
		print self.one
	def __call__(self,environ,start_response):
		status = '200 OK'
		print environ
		response_headers = [('Content-Type', 'text/plain')]
		start_response(status, response_headers)
		return ['%s\n' % (self.one)]


def hisab(global_config, one="1", two="2"):
	return Connection(one, two)