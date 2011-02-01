from googlelangdetect import detect_language_v2

if __name__ == "__main__":
	TwiSpli = "T#S%\r\n";
	f = open('pubT.txt');
	ts = f.read();
	tws= ts.split(TwiSpli);
	for t in tws:
		tspl = t.split("\t");
		#print tspl.__len__()		
		if tspl.__len__()>=7:
			#print detect_language_v2(tspl[6], api_key='AIzaSyDAjurAKFjvi_pTgnzJ6HU0bMeHxhQMnrQ');
			if tspl[5]<>'':
				print tspl[5];
		else:
			print "WWWWW TTTTT FFFFF", t

	f.close();
