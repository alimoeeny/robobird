# LOAD DATA LOCAL INFILE '~/pubT.txt' INTO TABLE Drops COLUMNS TERMINATED BY '\t' LINES TERMINATED BY 'T#S%\r\n' (TID, UID, AuthorId, CreatedAt, tlang, SourceURL, tplace, Body);

import tweepy
import time
from googlelangdetect import detect_language_v2

def sanitize(s):
	r = s.replace("\t","");
	r = s.replace("\n","");
	r = s.replace("\r","");
	r = s.replace("\a","");
	r = s.replace("\b","");
	r = s.replace("\f","");
	r = s.replace("\v","");
	return r

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
