#! /usr/bin/env python

class Pantho:
	def __init__(self, app, name):
		print name
		self.app = app
		self.name = name + "banerjee"
		#self.box = box
		name = name+' banerjee'
		print self.name
	def __call__(self, environ, start_response):
		print 'abcd'
		#print 'name -> '+ name
		#print environ
		for i in self.app(environ, start_response):
			yield i.upper()
			print i
		print "self.name -> "+self.name

def new_func(app, global_config, name, box, ovi, vim="4"):
	print "name -> "+name
	print "vim ->  "+vim
	#print "box ->  "+box
	return Pantho(app, name)
