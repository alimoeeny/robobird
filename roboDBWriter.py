
import tweepy
import time
from googlelangdetect import detect_language_v2


# exc_info is used for getting exceptions info
from sys import exc_info

from nltk import pos_tag, word_tokenize

import bpgsql


def sanitize(w):
	r = w;
	r = r.replace("!"," ");
	r = r.replace("'"," ");
	r = r.replace('"',' ');
#	r = r.replace("#","");
#	r = r.replace("@","");
#	r = r.replace("$","");
#	r = r.replace("%","");
#	r = r.replace("^","");
#	r = r.replace("&","");
#	r = r.replace("*","");
	r = r.replace("("," ");
	r = r.replace(")"," ");
	r = r.replace("{"," ");
	r = r.replace("}"," ");
	r = r.replace("["," ");
	r = r.replace("]"," ");
	r = r.replace("<"," ");
	r = r.replace(">"," ");
#	r = r.replace("/"," ");
	r = r.replace("\\"," ");
	r = r.replace("|"," ");
	r = r.replace("+"," ");
	r = r.replace(";"," ");
#	r = r.replace(":"," ");
	r = r.replace("\t"," ");
	r = r.replace("\r"," ");
	r = r.replace("\n"," ");
	return r


def CheckinWord(curs, w):
	#print w
	if ((w<>"") & (w<>" ")):
		try:
			curs.execute("SELECT checkinword(E'%s')" % w.lower());
		except:
			print "PGsql checkinword failed!", exc_info()[0]


def SetinStatusCountry(curs, w, tid, country):
	#print w, tid, country
	if ((w<>"") & (w<>" ")):
		try:
			curs.execute("SELECT setinstatecountry(E'%(w)s', %(ts)d, %(tid)s, '%(country)s' )" % {"w":w.lower(), "ts":0, "tid":tid, "country":country});
		except: 
			print "PGsql setinstate failed", exc_info()[0]
			


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


if __name__ == "__main__":
    config = loadConfig()
    while (True):
		try:
			pub_tw = tweepy.api.public_timeline();
			print "Got %d tweets" % pub_tw.__len__()
			for t in pub_tw:
				time.sleep(0.3);
				dbg = bpgsql.Connection(host=config["servername"], username= config["pguser"], password=config["pgpass"], dbname=config["databasename"])			
				curg = dbg.cursor()
				if t.place:
					p = t.place['country'];
					print p
				else:
					p = ""
				for w in word_tokenize(sanitize(t.text)):
					try:
						sw = w					
						CheckinWord(curg, sw)
						SetinStatusCountry(curg, sw, t.id.__str__(), p)
					except:
						print "Failed", exc_info()[0], sw
				dbg.close()


		except:
			print "Somthing went wrong here", exc_info()[0]
		finally:
			print time.time()
		time.sleep(30);

