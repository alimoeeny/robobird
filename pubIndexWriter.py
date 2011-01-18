import tweepy
import time

if __name__ == "__main__":
	f = open("pubT.txt", 'w');
	#for i in range(0,10):
	while (True):
		time.sleep(10);
		try:
			pub_tw = tweepy.api.public_timeline();
			for t in pub_tw:
				s = '';
				s += t.id.__str__() + '-';
				s += t.user.id.__str__() + '-';
				s += t.author.id.__str__() + '-';
				s += t.created_at.__str__() + '-';
				if t.source_url==None :
					s += '-';
				else:				
					s += t.source_url + '-';						
				if t.place==None :
					s += '-';
				else:				
					s += t.place['country'] + '-';						
				#s += t. + '-';						
				s += t.text;
				f.write(s.encode('utf-8'));
				f.write("\n");	
		finally:
			print time.time()

	f.close();
