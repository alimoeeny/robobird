
import time
from googlelangdetect import detect_language_v2
#import guess_language

# exc_info is used for getting exceptions info
from sys import exc_info

#import MySQLdb
#from nltk import pos_tag, word_tokenize

servername = 'localhost'
username = 'ali'
userpass = 'testpassword' 
databasename = 'robobird'
import bpgsql
pguser="postgres"
pgpass="testpassword"


if __name__ == "__main__":
	db =  bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)
	cur = db.cursor()
	cur.execute('SELECT "Word" FROM "Words" WHERE "Lang" = \'\'');
	c = 0;
	for w in cur:
		c += 1
		time.sleep(1);
		try:
			tlang = detect_language_v2(w, api_key='AIzaSyDAjurAKFjvi_pTgnzJ6HU0bMeHxhQMnrQ')
		except:
			tlang = "x";				

		print c, w , tlang
		if tlang <> "":
			dbg = bpgsql.Connection(host=servername, username= pguser, password=pgpass, dbname=databasename)			
			curg = dbg.cursor()
			# THIS IS TO BE FIXED POSSIBLE SQL INJECTION PROBLEM HERE
			#print 'UPDATE "Words" SET "Lang" = E\'%(lang)s\' WHERE "Word" = E\'%(w)s\';'  % {"w":w[0], "lang":tlang[0]}
			curg.execute('UPDATE "Words" SET "Lang" = E\'%(lang)s\' WHERE "Word" = E\'%(w)s\';'  % {"w":w[0], "lang":tlang[0]});
			dbg.close();


	db.close();
	





