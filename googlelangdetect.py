# -*- coding: utf-8 -*-

import json
import urllib, urllib2

from operator import itemgetter

def detect_language_v2(chunks, api_key):
    """
    chunks: either string or sequence of strings

    Return list of corresponding language codes
    """
    if isinstance(chunks, basestring):
        chunks = [chunks] 

    url = 'https://www.googleapis.com/language/translate/v2'

    data = urllib.urlencode(dict(
        q=[t.encode('utf-8') if isinstance(t, unicode) else t 
           for t in chunks],
        key=api_key,
        target="en"), doseq=1)

    # the request length MUST be < 5000
    if len(data) > 5000:
        raise ValueError("request is too long, see "
            "http://code.google.com/apis/language/translate/terms.html")

    #NOTE: use POST to allow more than 2K characters
    request = urllib2.Request(url, data,
        headers={'X-HTTP-Method-Override': 'GET'})
    d = json.load(urllib2.urlopen(request))
    if u'error' in d:
        raise IOError(d)
    return map(itemgetter('detectedSourceLanguage'), d['data']['translations'])

# Usage sample
#print detect_language_v2(
#    ["Python - can I detect unicode string language code?",
#     u"матрёшка",
#     u"打水"], api_key=open('api_key.txt').read().strip())
