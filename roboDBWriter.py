# LOAD DATA LOCAL INFILE '~/pubT.txt' INTO TABLE Drops COLUMNS TERMINATED BY '\t' LINES TERMINATED BY 'T#S%\r\n' (TID, UID, AuthorId, CreatedAt, tlang, SourceURL, tplace, Body);

import tweepy
import time
from googlelangdetect import detect_language_v2


import MySQLdb
from nltk import pos_tag, word_tokenize

servername = 'localhost'
username = 'ali'
userpass = 'testpassword' 
databasename = 'robobird'



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
		db = MySQLdb.Connect(servername, username, userpass, databasename)
		cur = db.cursor()
		cur.callproc('checkinword', [w.lower()]);
		db.close();

def SetinStatus(w, hnscore, inTitle, sURL):
	#print w, hnscore, inTitle, sURL
	if ((w<>"") & (w<>" ")):
		db = MySQLdb.Connect(servername, username, userpass, databasename)
		cur = db.cursor()
		cur.callproc('setinstate', [w.lower(), hnscore, inTitle, sURL]);
		db.close();


if __name__ == "__main__":
	splitter = "\t";
	TwiSpli = "T#S%\r\n";
	f = open("pubT.txt", 'a');
	#for i in range(0,10):
	while (True):
		time.sleep(30);
		try:
			pub_tw = tweepy.api.public_timeline();
			for t in pub_tw:
				time.sleep(0.3);
				try:
					tlang = detect_language_v2(sanitize(t.text), api_key='AIzaSyDAjurAKFjvi_pTgnzJ6HU0bMeHxhQMnrQ')
				except:
					tlang = "x";				
				if tlang not in ('ja', 'ar', 'ru'):			
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
		finally:
			print time.time()

	f.close();
