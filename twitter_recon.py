import json
import urllib
from anonBrowser import *

class ReconPerson:
    def __init__(self, first_name: str, last_name: str, job: str='', social_media: dict={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def __repr__(self):
        return f'{self.first_name} {self.last_name} has job {self.job}'

    def get_social(self, media_name):
        if self.social_media.has_ley(media_name):
            return self.social_media[media_name]
        return None

    def query_twitter(self, query):
        query = urllib.quote_plus(query)
        results = []
        browser = anonBrowser()
        response = browser.open(f'http://search.twitter.com/search.json?q={query}')
        for result in json.load(response)['results']:
            results.append({'from_user': result['from_user_name'], 'geo': result['geo'], 'tweet': result['tweet']})
        return results

ap = ReconPerson('Boondock', 'Saint')
print(ap.query_twitter('from:th3j35t3r since:2010-01-01 include:retweets'))
