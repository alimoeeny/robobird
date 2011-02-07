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

# exc_info is used for getting exceptions info
from sys import exc_info


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
	t += '<meta name="description" content="Ali Moeeny, robobird, twitter mind reader" />'
	t += '<meta name="keywords" content="Ali Moeeny, twitter, robot, robobird, mind, whats on your mind, Brain" />'
	t += '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
        t += '<meta name="google-site-verification" content="" />'
        t += '<title>RoboBird</title>'
	t += ''
        t += '<link rel="stylesheet" href="alihome.css" type="text/css" />'
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
	try:
		dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
		curg = dbg.cursor()
		curg.execute("SELECT topTweentingCountries()");
		for c in curg.fetchall():
			r.append(c);
		dbg.close();
	except:
		print "PGsql topTweetingCountries failed!", exc_info()[0]

	return r;
	
def TA_whatArePeopleTweetingAbout():
	r = [];
	try:
		dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
		curg = dbg.cursor()
		#curg.execute("SELECT whatArePeopleTweetingAbout()");
		curg.execute("SELECT whatsignificantthingsarepeopletweetingabout()");
		for c in curg.fetchall():
			r.append(c);
		dbg.close();
	except:
		print "PGsql whatArePeopleTweetingAbout failed!", exc_info()[0]

	return r;


def loadConfig():
	config = {}
	f = open("server.txt")
	s = f.readlines()
	f.close()
	config["environment"] = s[0].split("=")[1].replace("\r","").replace("\n","")
	return config

def main():
	config = loadConfig();
	print "We are in %(env)s !" % {"env":config["environment"]}
	http_server = tornado.httpserver.HTTPServer(application)
    	http_server.listen(8888)
    	tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		quit()

