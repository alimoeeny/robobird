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
	r = r.replace("!","");
	r = r.replace("'","");
	r = r.replace('"','');
	r = r.replace("#","");
	r = r.replace("@","");
	r = r.replace("$","");
	r = r.replace("%","");
	r = r.replace("^","");
	r = r.replace("&","");
	r = r.replace("*","");
	r = r.replace("(","");
	r = r.replace(")","");
	r = r.replace("{","");
	r = r.replace("}","");
	r = r.replace("[","");
	r = r.replace("]","");
	r = r.replace("<","");
	r = r.replace(">","");
	r = r.replace("/","");
	r = r.replace("\\","");
	r = r.replace("|","");
	r = r.replace("+","");
	r = r.replace(";","");
	r = r.replace(":","");
	r = r.replace("\t","");
	r = r.replace("\r","");
	r = r.replace("\n","");
	return r


def CheckinWord(w):
	#print w
	if ((w<>"") & (w<>" ")):
#		try:
#			db = MySQLdb.Connect(servername, username, userpass, databasename, use_unicode=True)
#			cur = db.cursor()
#			cur.callproc('checkinword', [w.lower()]);
#			db.close();
#		except:
#			print "mysql checkinword failed!", exc_info()[0]

		try:
			dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
			curg = dbg.cursor()
			# THIS IS TO BE FIXED POSSIBLE SQL INJECTION PROBLEM HERE
			curg.execute("SELECT checkinword(E'%s')" % w.lower());
			dbg.close();
		except:
			print "PGsql checkinword failed!", exc_info()[0]


def SetinStatus(w, hnscore, inTitle, tid):
#	print w, hnscore, inTitle, tid
	if ((w<>"") & (w<>" ")):
#		try:
#			db = MySQLdb.Connect(servername, username, userpass, databasename, use_unicode=True)
#			cur = db.cursor()
#			cur.callproc('setinstate', [w.lower(), hnscore, inTitle, tid.__str__()]);
#			db.close();
#		except: 
#			print "mysql setinstate failed", exc_info()[0]
			
		try:
			#print "SELECT setinstate(E'%(w)s', %(ts)d, %(tid)s )" % {"w":w.lower(), "ts":0, "tid":tid}

			dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
			curg = dbg.cursor()
			curg.execute("SELECT setinstate(E'%(w)s', %(ts)d, %(tid)s )" % {"w":w.lower(), "ts":0, "tid":tid}
);
			dbg.close();
		except: 
			print "PGsql setinstate failed", exc_info()[0]
			


if __name__ == "__main__":
	splitter = "\t";
	TwiSpli = "T#S%\r\n";
	f = open("pubT.txt", 'a');
	#for i in range(0,10):
	while (True):
		try:
			pub_tw = tweepy.api.public_timeline();
			print "Got %d tweets" % pub_tw.__len__()
			for t in pub_tw:
				#time.sleep(0.3);
				#try:
				#	try:
				#		tlang = guess_language.guessLanguage(unicode(sanitize(t.text)))
				#		if (tlang == "UNKNOWN"): #| (tlang == "en")):
				#			tlang = detect_language_v2(sanitize(t.text), api_key='AIzaSyDAjurAKFjvi_pTgnzJ6HU0bMeHxhQMnrQ')
				#	except: 
				#		tlang = detect_language_v2(sanitize(t.text), api_key='AIzaSyDAjurAKFjvi_pTgnzJ6HU0bMeHxhQMnrQ')
				#except:
				#	tlang = "x";
				tlang = " "				
				if tlang not in ('ja', 'ca', 'ar', 'ru', 'pt', 'af', 'bg', 'fr', 'de', 'zh', 'tr', 'nb','es','sk', 'ko', 'it', 'id','la','lv','mk','nl','et','cs','so','da','uk', 'sv','th','ro','tn','tl','ha','sr','el','ceb'):
					s = '';
					s += t.id.__str__() + splitter;
					s += t.user.id.__str__() + splitter;
					s += t.author.id.__str__() + splitter;
					s += t.created_at.__str__() + splitter;
					s += tlang[0] + splitter;
					if t.source_url==None :
						s += splitter;
					else:				
						s += sanitize(t.source_url) + splitter;						
					if t.place==None :
						s += splitter;
					else:				
						s += t.place['country'] + splitter;						
					#s += t. + splitter;						
					s += sanitize(t.text) + splitter;
					f.write(s.encode('utf-8'));
					f.write(TwiSpli);	
		
					for w in word_tokenize(t.text):
						try:
							sw = sanitize(w)					
							CheckinWord(sw)
							SetinStatus(sw, 0, 0, t.id.__str__())
						except:
							print "Failed", exc_info()[0], tlang, sw



		finally:
			print time.time()
		time.sleep(30);

	f.close();
