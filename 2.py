#! /usr/bin/env python

def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    print environ
    print '\n\n\n\nBangladesh\n\n\n\n'

    #print environ
    print '---'
    print environ['HTTP_NAME']
    print '---'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    print 'Hi World'
    s =[1,2,3,4]
    ss = environ.get('HTTP_NAME')
    print type(ss)
    if ss:
    	print "Here -->"

    #return ['Hello world!\nHi World\nbeautiful bangladesh\n']
    #return ['only beautiful bangladesh is real\nOthers are fake :3\n']
    if not ss:
        return ":("
    else:
    	#print 'im in else'
        #return str(ss)
        #print hasattr([], '__iter__')
        return "bangla "+ss
    #print '1234'
    #return ['Hi World!\n']

def middleware_welcome(environ, start_response):
	print "\n\n >>> Middleware Welcome <<< \n\n"
	print environ
	print "\n\n"
	print environ.get['HTTP_NAME']
	jb = environ.get['HTTP_NAME']
	jb = "Welcome "+jb
	print jb
	environ['HTTP_NAME'] = jb
	httpserver.serve(simple_app, host = '192.168.8.105', port = '8080')

if __name__ == '__main__':
    #int 'line 1'
    from paste import httpserver
    #print 'hello :D '
    #print 'hi :D'
    httpserver.serve(simple_app, host = '192.168.8.105', port = '8080')
    print 'Jishnu Banerjee'
