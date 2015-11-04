#! /usr/bin/env python

if __name__ == '__main__':
    from paste import httpserver
    from paste.deploy import loadapp
    httpserver.serve(loadapp('config:config.ini', relative_to = '.'), host='192.168.8.105', port = '8080')


