# LOAD DATA LOCAL INFILE '~/pubT.txt' INTO TABLE Drops COLUMNS TERMINATED BY '\t' LINES TERMINATED BY 'T#S%\r\n' (TID, UID, AuthorId, CreatedAt, tlang, SourceURL, tplace, Body);

import tweepy
import time
from googlelangdetect import detect_language_v2
import guess_language

# exc_info is used for getting exceptions info
from sys import exc_info

import MySQLdb
from nltk import pos_tag, word_tokenize

servername = 'localhost'
username = 'ali'
userpass = 'testpassword' 
databasename = 'robobird'

###################
#import psycopg2
import bpgsql
pguser="postgres"
pgpass="testpassword"


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


def CheckinWord(w):
	#print w
	if ((w<>"") & (w<>" ")):
		try:
			dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
			curg = dbg.cursor()
			# THIS IS TO BE FIXED POSSIBLE SQL INJECTION PROBLEM HERE
			curg.execute("SELECT checkinword(E'%s')" % w.lower());
			dbg.close();
		except:
			print "PGsql checkinword failed!", exc_info()[0]


def SetinStatus(w, tid):
#	print w, hnscore, inTitle, tid
	if ((w<>"") & (w<>" ")):
		try:
			#print "SELECT setinstate(E'%(w)s', %(ts)d, %(tid)s )" % {"w":w.lower(), "ts":0, "tid":tid}
			dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
			curg = dbg.cursor()
			curg.execute("SELECT setinstate(E'%(w)s', %(ts)d, %(tid)s )" % {"w":w.lower(), "ts":0, "tid":tid});
			dbg.close();
		except: 
			print "PGsql setinstate failed", exc_info()[0]
			


if __name__ == "__main__":
	while (True):
		try:
			pub_tw = tweepy.api.public_timeline();
			print "Got %d tweets" % pub_tw.__len__()
			for t in pub_tw:
				for w in word_tokenize(sanitize(t.text)):
					try:
						sw = w					
						CheckinWord(sw)
						SetinStatus(sw, t.id.__str__())
					except:
						print "Failed", exc_info()[0], sw



		finally:
			print time.time()
		time.sleep(30);

