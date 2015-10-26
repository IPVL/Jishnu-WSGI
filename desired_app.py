#! /usr/bin/env python

def O_O(environ, start_response):
	status = '200 OK'
	response_header = [('Content-Type', 'text/plain')]
	start_response(status, response_header)
	return ['%s\n' % environ.get('HTTP_NAME')]
	#return ['%s\n' % environ['HTTP_NAME']]
	return ['Hello\n']

def add_hello_message(app):
	def _hello(environ, start_response):
		environ['HTTP_NAME'] = 'Hello '+ environ['HTTP_NAME']
		return app(environ, start_response)

	return _hello

def add_full_name(app):
	def _full(environ, start_response):
		environ['HTTP_NAME'] = environ['HTTP_NAME']+ ' Banerjee'
		return app(environ, start_response)

	return _full

if __name__ == '__main__':
	from paste import httpserver
	httpserver.serve(add_full_name(add_hello_message(O_O)), host='192.168.8.105', port = '8080')