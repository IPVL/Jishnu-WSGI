#! /usr/bin/env python


class Configured:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return ['%s, %s!\n' % (self.greeting, self. name)]


def app_factory(global_config, name='johnny', greeting='Howdy'):
    return Configured(name, greeting)


if __name__ == '__main__':
    from paste import httpserver
    from paste.deploy import loadapp
    httpserver.serve(loadapp('config:config.ini', relative_to = '.'), host='192.168.8.105', port = '8080')


