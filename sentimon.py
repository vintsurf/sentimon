#!/usr/bin/python

#Based on https://github.com/taskulu/tweelead

from aylienapiclient import textapi
from aylienapiclient.errors import HttpError
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

count = 0

pager = TwitterRestPager(api, 'search/tweets', {'q': 'keywords,comma,separated', 'count':100})

for item in pager.get_iterator(wait=7):
	tweet = item['text']
	name = item['user']['screen_name']
	date = item['created_at']
	try:
		s = c.Sentiment({'text' : tweet})
	except HttpError:
		pass
	if 'text' in item:
		count += 1
	elif 'message' in item['code'] == 88:
		print(item['message'])
		break
	print ("{0} | {1} | User: {2} | Tweet: {3} | Polarity: {4} | Confidence: {5} | Subjectivity: {6} | Confidence: {7}".format(count, , date, name, tweet, s['polarity'], s['polarity_confidence'], s['subjectivity'], s['subjectivity_confidence'])) 


	
	



	
