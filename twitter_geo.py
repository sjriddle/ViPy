import json
import urllib
import optparse
from anonBrowser import *

def get_tweets(handle):
    query = urllib.quote_plus(f'from: {handle} since:2009-01-01 include:retweets')
    tweets = []
    browser = anonBrowser()
    browser.anonymize()
    response = browser.open(f'http://search.twitter.com/search.json?q={query}')

    for result in json.load(response)['results']:
        tweets.append({'from_user': result['from_user_name'], 'geo': result['geo'], 'tweet': result['text']})

    return tweets

def load_cities(city_file):
    cities = []
    for line in open(city_file).readlines():
        cities.append(line.strip('\n').strip('\r').lower())
    return cities


def twitter_locate(tweets, cities):
    locations = []
    loc_cnt = 0
    city_cnt = 0
    tweets_text = ""

    for tweets in tweets:
        if tweet['geo']:
            locations.append(tweet['geo'])
            loc_cnt += 1
        tweets_text += tweet['tweet'].lower()

    for city in cities:
        if city in tweets_text:
            locations.append(city)
            city_cnt += 1

    print(f'[+] Found {loc_cnt} {locations} via Twitter API and {city_cnt} locations from text search.')
    return locations


def main():
    parser = optparse.OptionParser('usage %prog -u <twitter handle> [-c <list of cities>]')
    parser.add_options('-u', dest='handle', type='string', help='specify twitter handle')
    parser.add_options('-c', dest='city_file', type='string', help='specify file containing cities to search')

    (options, args) = parser.parse_args()
    handle = options.handle
    city_file = options.city_file

    if not handle:
        print(parser.usage)
        exit(0)

    print(f'[+] Locations: {twitter_locate(get_tweets(handle), load_cities(city_file) if city_file else [])}')

    
if __name__ == '__main__':
    main()
