#! /usr/bin/env python

class Configured:
    def __init__(self, name, greeting):
        print 'Configured : __init__ : second'
        self.name = name
        self.greeting = greeting
        print " -->  "+ self.name +'  '+ self.greeting
    def __call__(self, environ, start_response):
        print 'Configured : __call__ : second'
        print 'name in Configured.py -> '+self.name
        #print 'box -> '+self.box
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return ['%s, %s, box=!\n' % (self.greeting, self.name)]

#name = "bogra"
def app_factory(global_config, name="OBAMA", greeting='Howdy'):
    print 'app_factory'
    print name
    #print "first box -> "+ box
    return Configured(name, greeting)

