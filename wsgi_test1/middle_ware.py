#! /usr/bin/env python

class Pantho:
    def __init__(self, app, name):
        self.app = app
        self.name = name + "banerjee"
        name = name+' banerjee'
        print self.name
    def __call__(self, environ, start_response):
    	print 'abcd'
    	print 'name -> '+ self.name
    	print environ
        for i in self.app(environ, start_response):
            yield i.upper()
            print i
        print "self.name -> "+self.name

def new_func(app, global_config):
	return Pantho(app, "name")
