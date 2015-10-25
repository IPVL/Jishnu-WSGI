#! /usr/bin/env python

def green(environ, start_response):
    """simplest possible application object"""
    status = '200 OK'
    response_header = [('Content-Type', 'text/plain')]
    start_response(status, response_header)
    return ['%s\n' % environ.get('GREETING', 'Hello World!')]

def greetingSetter(environ, start_response):
    def _curried(environ, start_response):
        environ['GREETING'] = 'Bonjour le monde!'
        return app(environ, start_response)
    return _curried
