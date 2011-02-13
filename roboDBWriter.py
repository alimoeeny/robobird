
import tweepy
import time
from googlelangdetect import detect_language_v2


# exc_info is used for getting exceptions info
from sys import exc_info

from nltk import pos_tag, word_tokenize

import bpgsql
import re

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
	r = r.replace("<"," ");
	r = r.replace(">"," ");
#	r = r.replace(":"," ");
	r = r.replace("\t"," ");
	r = r.replace("\r"," ");
	r = r.replace("\n"," ");
	return r


def isNotToBeIgnored(w):
  
  return True

def CheckinWord(curs, w):
	#print "word", w
	if ((w<>"") & (w<>" ")):
		try:
			curs.execute("SELECT checkinword(E'%s')" % w.lower());
		except:
			print "PGsql checkinword failed!", exc_info()[0]


def CheckinLink(curs, lk):
	print "LINK:", lk 
	if ((lk<>"") & (lk<>" ")):
		try:
			curs.execute("SELECT checkinlink(E'%s')" % lk);
		except:
			print "PGsql checkinlink failed!", exc_info()[0]

def SetinStatusCountry(curs, w, tid, country):
	#print w, tid, country
	if ((w<>"") & (w<>" ")):
		try:
			curs.execute("SELECT setinstatecountry(E'%(w)s', %(ts)d, %(tid)s, '%(country)s' )" % {"w":w.lower(), "ts":0, "tid":tid, "country":country});
		except: 
			print "PGsql setinstate failed", exc_info()[0]
			
def SetinStatusCountryPlace(curs, w, tid, country, place):
	#print w, tid, country, place
	if ((w<>"") & (w<>" ")):
		try:
			#print type(place)
			#print "SELECT setinstatecountryplace(E'%(w)s', %(ts)d, %(tid)s, '%(country)s', '%(place)s' )" % {"w":w.lower(), "ts":0, "tid":tid, "country":country, "place": re.escape(unicode(place))};
			curs.execute("SELECT setinstatecountryplace(E'%(w)s', %(ts)d, %(tid)s, E'%(country)s', E'%(place)s' )" % {"w":w.lower(), "ts":0, "tid":tid, "country":country, "place": re.escape(unicode(place))});
		except: 
			print "PGsql setinstate failed", exc_info()[0]


def SetLinkinStatusCountryPlace(curs, lk, tid, country, place):
	if ((lk<>"") & (lk<>" ")):
		try:
			curs.execute("SELECT setlinkinstatecountryplace(E'%(lk)s', %(ts)d, %(tid)s, E'%(country)s', E'%(place)s' )" % {"lk":lk, "ts":0, "tid":tid, "country":country, "place": re.escape(unicode(place))});
		except: 
			print "PGsql setlinkinstate failed", exc_info()[0]



def extractEmails(s):
  r = []
  s_rem = s
  m = re.findall('[\w.]+@[\w]+\.[\w.]+', s)
  if m:
    for lk in m:
      r.append(lk)
      s_rem = s_rem.replace(lk,'')
  r.append(s_rem)
  return r


def extractLinks(s):
  r = []
  s_rem = s
  m = re.findall('http[s]?://\w+[\w./!#]*', s)
  if m:
    for lk in m:
      r.append(lk)
      s_rem = s_rem.replace(lk,'')
  r.append(s_rem)
  return r


def extractLinksorEmails(s):
  r = []
  s_rem = s
  m = re.findall('http[s]?://\w+[\w./!#]*|[\w.]+@[\w]+\.[\w.]+', s)
  if m:
    for lk in m:
      r.append(lk)
      s_rem = s_rem.replace(lk,'')
  r.append(s_rem)
  return r




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
					place = t.place;
					p = t.place['country'];
					print p
				else:
					place = ""
					p = ""
				linkified = extractLinksorEmails(t.text)
				#print "LINKIFIED:", linkified
				for lk in linkified[:-1]:
					CheckinLink(curg, lk)
					SetLinkinStatusCountryPlace(curg, lk, t.id.__str__(), p, place)

				for w in word_tokenize(sanitize(linkified[-1])):
					try:
						if isNotToBeIgnored(w):
							sw = w
							CheckinWord(curg, sw)
							SetinStatusCountryPlace(curg, sw, t.id.__str__(), p, place)
					except:
						print "Failed", exc_info()[0], sw
				dbg.close()


		except:
			print "Somthing went wrong here", exc_info()[0]
		finally:
			print time.time()
		time.sleep(30);

