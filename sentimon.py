#!/usr/bin/python

#Based on https://github.com/taskulu/tweelead

from aylienapiclient import textapi
from TwitterAPI import TwitterAPI, TwitterRestPager
#import sys ##If default encoding is set to ASCII
#reload(sys)
#sys.setdefaultencoding('UTF8')

c = textapi.Client("AYLIEN_API_ID_HERE", "AYLIEN_API_KEY_HERE")

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

pager = TwitterRestPager(api, 'search/tweets', {'q': 'keywords,comma,separated'})

for item in pager.get_iterator():
	tweet = item['text']
	name = item['user']['screen_name']
	s = c.Sentiment({'text' : tweet})
	print ("Username: {0} | Tweet: {1} | Polarity: {2} | Confidence: {3} | Subjectivity: {4} | Confidence: {5}".format(name, tweet, s['polarity'], s['polarity_confidence'], s['subjectivity'], s['subjectivity_confidence'])) 


	
	



	
