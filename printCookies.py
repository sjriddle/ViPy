#!/usr/bin/python
import mechanize
import cookielib

def printCookies(url):
    browser = mechanize.Browser()
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)

    for cookie in cookie_jar:
        print(cookie)

url = 'https://{INSERT URL}'
printCookies(url)
