
import time
from googlelangdetect import detect_language_v2

# exc_info is used for getting exceptions info
from sys import exc_info

import bpgsql

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
	print "Language Updater here!"
	print "We are in %(env)s !" % {"env":config["environment"]}
	print "Database server is at %(env)s !" % {"env":config["servername"]}
	print "RoboBird db name is %(env)s !" % {"env":config["databasename"]}

	db =  bpgsql.Connection(host=config["servername"], username= config["pguser"], password=config["pgpass"], dbname=config["databasename"])
	cur = db.cursor()
	cur.execute('SELECT "Word" FROM "Words" WHERE "Lang" = \'\'');
	c = 0;
	dbg =  bpgsql.Connection(host=config["servername"], username= config["pguser"], password=config["pgpass"], dbname=config["databasename"])
	for w in cur:
		c += 1
		time.sleep(1);
		try:
			tlang = detect_language_v2(w, api_key=config["googletranslateapikey"])
		except:
			tlang = "x";				

		print c, w , tlang
		if tlang <> "":
			curg = dbg.cursor()
			# THIS IS TO BE FIXED POSSIBLE SQL INJECTION PROBLEM HERE
			#print 'UPDATE "Words" SET "Lang" = E\'%(lang)s\' WHERE "Word" = E\'%(w)s\';'  % {"w":w[0], "lang":tlang[0]}
			curg.execute('UPDATE "Words" SET "Lang" = E\'%(lang)s\' WHERE "Word" = E\'%(w)s\';'  % {"w":w[0], "lang":tlang[0]});

	dbg.close();
	db.close();



		

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		quit()



