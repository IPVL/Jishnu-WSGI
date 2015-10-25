#! /usr/bin/env python

def simple_app(environment, start_response):
    """simplest possible application object"""
    status = '200 OK'
    response_header = [('Content-Type', 'text/plain')]
    start_response(status, response_header)
    return ['WSGI\n']

class Caseless:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, self_response):
        for chunk in self.app(environ, start_response):
        yield chunk.lower()

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(Caseless(simple_app), host = '192.168.8.105', port = '8080')
