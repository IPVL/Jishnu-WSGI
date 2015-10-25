#! /usr/bin/env python

def simple_app(environ, start_response):
    """simplest possible application object"""
    status = '200 OK'
    response_header = [('Content-Type', 'text/plain')]
    start_response(status, response_header)
    #return ['Hello\n']
    return ['%s\n' % environ.get('HTTP_NAME')]

def greetingSetter(app):
    def _curried(environ, start_response):
        environ['HTTP_NAME'] = 'Ovi'
        return app(environ, start_response)

    return _curried

class Caseless:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        for chunk in self.app(environ, start_response):
            yield chunk.lower()

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(Caseless(greetingSetter(simple_app)), host = '192.168.8.105', port = '8080')
    #httpserver.serve(greetingSetter(simple_app), host = '192.168.8.105', port = '8080')
    #httpserver.serve(simple_app, host = '192.168.8.105', port = '8080')
