# -*- coding: utf-8 -*-

### Move to TA
import bpgsql
import time

# exc_info is used for getting exceptions info
from sys import exc_info

def TA_tweetCountCache():
	r = [];
	try:
		dbg = bpgsql.Connection(host=config["servername"], username=config["pguser"], password=config["pgpass"], dbname=config["databasename"])			
		curg = dbg.cursor()
		curg.execute("SELECT tweetcount()");
		for c in curg.fetchall():
			r.append(c);
		dbg.close();
	except:
		print "PGsql tweetcount failed!", exc_info()[0]
	f = open("TA_tweetcount.Cache","w");
	for rs in r:
		for i in rs:
			f.write(i.__str__().encode('utf-8'));
		f.write(";");
	f.close()

def TA_topTweetingCountriesCache():
	r = [];
	try:
		dbg = bpgsql.Connection(host=config["servername"], username=config["pguser"], password=config["pgpass"], dbname=config["databasename"])			
		curg = dbg.cursor()
		curg.execute("SELECT toptweetingcountries2()");
		for c in curg.fetchall():
			r.append(c);
		dbg.close();
	except:
		print "PGsql topTweetingCountriesv2 failed!", exc_info()[0]
	f = open("TA_topTweetingCountries.Cache","w");
	for rs in r:
		for i in rs:
			f.write(i.encode('utf-8'));
		f.write(";");
	f.close()
	
def TA_whatArePeopleTweetingAboutCache():
	r = [];
	try:
		dbg = bpgsql.Connection(host=config["servername"], username=config["pguser"], password=config["pgpass"], dbname=config["databasename"])			
		curg = dbg.cursor()
		#curg.execute("SELECT whatArePeopleTweetingAbout()");
		curg.execute("SELECT whatsignificantthingsarepeopletweetingabout2()");
		for c in curg.fetchall():
			r.append(c);
		dbg.close();
	except:
		print "PGsql whatArePeopleTweetingAbout failed!", exc_info()[0]
	f = open("TA_whatArePeopleTweetingAbout.Cache","w");
	for rs in r:
		for i in rs:
			f.write(i.encode('utf-8'));
		f.write(";");
	f.close()
	


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

def main():
	global config;
	config = loadConfig();
	#print config
	print "Report Writer Here!"
	print "We are in %(env)s !" % {"env":config["environment"]}
	print "Database server is at %(env)s !" % {"env":config["servername"]}
	print "RoboBird db name is %(env)s !" % {"env":config["databasename"]}
	while 1:
		try:
			print "Starting to regenerate the reports"
			print "running TA_tweetCountCache()"
			TA_tweetCountCache()
			print "running TA_topTweetingCountriesCache()"
			TA_topTweetingCountriesCache()
			print "running TA_whatArePeopleTweetingAboutCache()"
			TA_whatArePeopleTweetingAboutCache()
		except:
			print "Can't DO IT", exc_info()[0]
		print "Just Sleeping!"
		time.sleep(3600)
		

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		quit()

