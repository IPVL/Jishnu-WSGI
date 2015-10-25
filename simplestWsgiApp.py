#! /usr/bin/env python

def simple_app(environ, start_response):
    """simplest possible application object"""
    status = '200 OK'
    response_header = [('Content-Type', 'text/plain')]
    start_response(status, response_header)
    return ['Hello world!\n']

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(simple_app, host='192.168.8.105', port='8080')
