
import time
from googlelangdetect import detect_language_v2
#import guess_language

# exc_info is used for getting exceptions info
from sys import exc_info

import MySQLdb
#from nltk import pos_tag, word_tokenize

servername = 'localhost'
username = 'ali'
userpass = 'testpassword' 
databasename = 'robobird'

###################
#import psycopg2
import bpgsql
pguser="postgres"
pgpass="testpassword"




def SetinStatus(w, tid):	
		try:
			dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
			curg = dbg.cursor()
			curg.execute("SELECT setinstate(E'%(w)s', %(ts)d, %(tid)s )" % {"w":w.lower(), "ts":0, "tid":tid});
			dbg.close();
		except: 
			print "PGsql setinstate failed", exc_info()[0]
			
def CheckinWord(w):
	try:
		dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
		curg = dbg.cursor()
		# THIS IS TO BE FIXED POSSIBLE SQL INJECTION PROBLEM HERE
		curg.execute("SELECT checkinword(E'%s')" % w.lower());
		dbg.close();
	except:
		print "PGsql checkinword failed!", exc_info()[0]


if __name__ == "__main__":
	db = MySQLdb.Connect(servername, username, userpass, databasename, use_unicode=True)
	cur = db.cursor()

#	cur.execute('SELECT Word FROM Words');
#	for w in cur:
#		print w[0]
#		CheckinWord(w[0])

	cur.execute('SELECT * FROM MindState');
	for w in cur:
		print w[1], w[3], w[5]
		#print 'E\'%(w)s\', %(d)s, %(tid)s )'  % {"w":w[1], "d":w[3], "tid":w[2]}
		dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
		curg = dbg.cursor()
		# THIS IS TO BE FIXED POSSIBLE SQL INJECTION PROBLEM HERE
		curg.execute('INSERT INTO "MindState" ("Word", "InsertDate","TweetID" ) VALUES(E\'%(w)s\', \'%(d)s\', %(tid)s )'  % {"w":w[1], "d":w[3], "tid":w[2]});
		dbg.close();



	db.close();
	





