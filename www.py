# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web

### Move to TA
servername = 'localhost'
username = 'ali'
userpass = 'testpassword' 
databasename = 'robobird'
import bpgsql
pguser="postgres"
pgpass="testpassword"



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(getMainPage())

application = tornado.web.Application([
    (r"/", MainHandler),
])


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
	t += '<meta name="description" content="Ali Moeeny, Who am I, What am I doing and more" />'
	t += '<meta name="keywords" content="Ali Moeeny, Motahar, Motaharsadat, Hosseini, Brain, TED, Farsi, Translation, Neuroscience, Vision Science, Iran, Iranian, Irani, علی معینی, مطهر, نوروساینس, مغز, اعصاب ,تد, ترجمه , فارسی" />'
	t += '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
        t += '<meta name="google-site-verification" content="d6GHRUvsrXc4vtd7vdNHDBDvBzoim75jI6Z32-iWqpc" />'
        t += '<title>Ali Moeeny - علی معینی</title>'
	t += ''
        t += '<link rel="stylesheet" href="alihome.css" type="text/css" />'
        t += '<link rel="alternate" type="application/rss+xml" title="RSS Feed for ali.moeeny.com" href="http://alimoeeny.posterous.com/rss.xml" />'
        t += '<link rel="alternate" type="application/rss+xml" title="RSS Feed for Ali\'s twitter timeline" href="http://twitter.com/statuses/user_timeline/14156637.rss" />'
	t += '<!-- link rel="shortcut icon" href="AliNastalighW.png" / -->'
	t += '<link rel="apple-touch-icon" href="AliNastalighW.png" />'
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
	t += ""
	t += "</body>"
	t += "</html>"
	return t

def getMainPageBody():
	t = ''
	t += '<div id="wholepage" style="background-color:#F5EEFF;width:95%;margin-left:10px; margin-top:20px; padding:15px; border-radius:20px;">'
	t += ""
	t += "<h1>Tweeting Countries/ Where are people awake and tweeting!</h1>"
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
		t += '<li>' + c.__str__().split(",")[0].split('(')[1].replace('"','') + ' - ' + c.__str__().split(",")[1].split(')')[0].replace('"','')
	t += '</lo>'	
	return t

def whatArePeopleTweetingAbout():
	t = ''	
	return t


###############################  T A 
def TA_topTweetingCountries():
	r = [];
	try:
		dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
		curg = dbg.cursor()
		curg.execute("SELECT topTweentingCountries()");
		for c in curg.fetchall():
			r.append(c);
		dbg.close();
	except:
		print "PGsql checkinword failed!", exc_info()[0]

	return r;
	
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
