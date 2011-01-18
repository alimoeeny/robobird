import tweepy
import time

def sanitize(s):
	r = s.replace("\t","");
	r = s.replace("\n","");
	r = s.replace("\r","");
	return r

if __name__ == "__main__":
	splitter = "\t";
	f = open("pubT.txt", 'w');
	#for i in range(0,10):
	while (True):
		time.sleep(30);
		try:
			pub_tw = tweepy.api.public_timeline();
			for t in pub_tw:
				s = '';
				s += t.id.__str__() + splitter;
				s += t.user.id.__str__() + splitter;
				s += t.author.id.__str__() + splitter;
				s += t.created_at.__str__() + splitter;
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
				f.write("\n");	
		finally:
			print time.time()

	f.close();
