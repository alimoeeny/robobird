# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web

#### needed for loggly logging
import urllib2 


### Move to TA
import bpgsql

# exc_info is used for getting exceptions info
from sys import exc_info


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(getMainPage())
        logLoggly("homepage" + self.request.path.__str__() + self.request.arguments.__str__() + self.request.headers.__str__())

class ErrorHandler(tornado.web.RequestHandler):
    """Generates an error response with status_code for all requests."""
    def __init__(self, application, request, status_code):
        tornado.web.RequestHandler.__init__(self, application, request)
        self.set_status(status_code)
    
    def get_error_html(self, status_code, **kwargs):
        logLoggly("ERROR" + self.request.path.__str__() + self.request.arguments.__str__() + self.request.headers.__str__()+ "ERROR" + status_code.__str__())
        #self.require_setting("static_path")
        #if status_code in [404, 500, 503, 403]:
        #    filename = os.path.join(self.settings['static_path'], '%d.html' % status_code)
        #    if os.path.exists(filename):
        #        f = open(filename, 'r')
        #        data = f.read()
        #        f.close()
        #        return data
        return "<html><title>%(code)d: %(message)s</title>" \
                "<body class='bodyErrorPage'>%(code)d: %(message)s</body></html>" % {
            "code": status_code,
            "message": "ERROR HERE", #httplib.responses[status_code],
        }
    
    def prepare(self):
        raise tornado.web.HTTPError(self._status_code)

  
  
  
        

application = tornado.web.Application([
    (r"/", MainHandler),
])

## override the tornado.web.ErrorHandler with our default ErrorHandler
tornado.web.ErrorHandler = ErrorHandler


def getMainPage():
	s = ""
	s += getPageHeader()
	s += getMainPageBody()
	s += getPageFooter()
	return s


def getPageHeader():
	t = ""
	t += '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">'
	t += '<head>'
	t += '<meta name="author" content="Ali Moeeny" />'
	t += '<meta name="description" content="Ali Moeeny, robobird, twitter mind reader" />'
	t += '<meta name="keywords" content="Ali Moeeny, twitter, robot, robobird, mind, whats on your mind, Brain" />'
	t += '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
        t += '<meta name="google-site-verification" content="" />'
        t += '<title>RoboBird</title>'
	t += ''
        t += '<!-- link rel="stylesheet" href="alihome.css" type="text/css" / -->'
#        t += '<link rel="alternate" type="application/rss+xml" title="RSS Feed for ali.moeeny.com" href="http://alimoeeny.posterous.com/rss.xml" />'
#        t += '<link rel="alternate" type="application/rss+xml" title="RSS Feed for Ali\'s twitter timeline" href="http://twitter.com/statuses/user_timeline/14156637.rss" />'
	t += '<!-- link rel="shortcut icon" href="AliNastalighW.png" / -->'
	t += '<link rel="apple-touch-icon" href="http://ali.moeeny.com/AliNastalighW.png" />'
	t += '<style type="text/css">'
	t += '/*'
	t += 'h1 {color:#FF3333; font:150% Verdana,Helvetica; font-weight:bold;}'
	t += 'h2 {color:#AA3333; font:100% Verdana,Helvetica; font-weight:bold;}'
	t += 'p {color:#121314; font:85% Monaco,Courier New,DejaVu Sans Mono,Bitstream Vera Sans Mono,monospace;*font-size:100%;}'
	t += 'p.farsi {font:Tahoma, Koodak; color:#131618;}'
	t += 'li {color:#232399; font:85% Monaco,Courier New,DejaVu Sans Mono,Bitstream Vera Sans Mono,monospace;*font-size:100%;}'
	t += '*/'
	t += '</style>'
	t += ''
	t += '</head>'
	t += '<body>'
	return t
	
def getPageFooter():
	t = ""
	t += ''
	t += '	<script type="text/javascript">'
	t += ''
	t += "  var _gaq = _gaq || [];"
	t += "  _gaq.push(['_setAccount', 'UA-21229568-1']);"
	t += "  _gaq.push(['_setDomainName', 'none']);"
	t += "  _gaq.push(['_setAllowLinker', true]);"
	t += "  _gaq.push(['_trackPageview']);"
	t += ""
	t += "  (function() {"
	t += "    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;"
	t += "    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';"
	t += "    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);"
	t += '  })();'
	t += ''
	t += '</script>'
	t += ''	
	t += "</body>"
	t += "</html>"
	return t

def getMainPageBody():
	t = ''
	t += '<div id="wholepage" style="background-color:#F5EEFF;width:95%;margin-left:10px; margin-top:20px; padding:15px; border-radius:20px;">'
	t += ""
	t += "<h1>Where are people awake and tweeting?!</h1>"
	t += topTweetingCountries()
	t += "<h1>What are people tweeting about</h1>"
	t += whatArePeopleTweetingAbout()	
	t += ""
	return t

def topTweetingCountries():
	t = ''
	t += '<lo>'
	ttc = TA_topTweetingCountries()
	for c in ttc:
		if c.__len__()>0:
		    t += '<li>' + c.__str__().split(",")[0].split('(')[1].replace('"','') 
		    t += ' - ' + c.__str__().split(",")[1].split(')')[0].replace('"','')
		    t += ' [ ' + round(float(c.__str__().split(",")[2].split(')')[0].replace('"','')),3).__str__() + ' % ]' 
	t += '</lo>'	
	return t

def whatArePeopleTweetingAbout():
	t = ''
	t += '<table>'
	ttc = TA_whatArePeopleTweetingAbout()
	for c in ttc:
		if c.__len__()>0:
		    t += '<tr>'
		    t += '<td>' + c.__str__().split(",")[0].split('(')[1].replace('"','') + '</td>'
		    t += '<td>' + c.__str__().split(",")[1].split(')')[0].replace('"','') + '</td>'
		    #t += ' [ ' + round(float(c.__str__().split(",")[2].split(')')[0].replace('"','')),3).__str__() + ' % ]' 
		    t += '</tr>'
	t += '</table>'	
	return t


###############################  T A 
def TA_topTweetingCountries():
	r = [];
	f = open("TA_topTweetingCountries.Cache","r");
	s = f.read().split(";");
	f.close()
	for i in s:
		r.append(i);
	return r;

	
def TA_whatArePeopleTweetingAbout():
	r = [];
	f = open("TA_whatArePeopleTweetingAbout.Cache","r");
	s = f.read().split(";");
	f.close()
	for i in s:
		r.append(i);
	return r;



#############################

def logLoggly(s):
    try:
        urllib2.urlopen(config["logglywwwurl"], data=s);   
        return 0
    except:
        print "Loggly failed", exc_info()[0]
        return 1


def loadConfig():
	config = {}
	f = open("server.txt")
	s = f.readlines()
	f.close()
	for c in s:
		try:
			config[c.split("=")[0]] = c.split("=")[1].replace("\r","").replace("\n","")
		except:
			print "."
	return config

def main():
	global config;
	config = loadConfig();
	#print config
	print "We are in %(env)s !" % {"env":config["environment"]}
	print "Database server is at %(env)s !" % {"env":config["servername"]}
	print "RoboBird db name is %(env)s !" % {"env":config["databasename"]}
	if config["environment"] == 'development':
		http_server = tornado.httpserver.HTTPServer(application)
    		http_server.listen(8888)
    		tornado.ioloop.IOLoop.instance().start()
	elif config["environment"] == 'production':
		http_server = tornado.httpserver.HTTPServer(application)
    		http_server.listen(4321)
    		tornado.ioloop.IOLoop.instance().start()
	else:
		print " W O H O ! ! What's going on here ! ! ! !"
		

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		quit()

