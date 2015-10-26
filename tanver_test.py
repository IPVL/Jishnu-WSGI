#! /usr/bin/env python

def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    print environ
    print environ['HTTP_NAME']
    environ['HTTP_NAME']='Tanvir Pantho'
    print environ['HTTP_NAME']
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    #return ['Hello\n']
    return environ

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(simple_app, host='192.168.8.105', port='8080')
