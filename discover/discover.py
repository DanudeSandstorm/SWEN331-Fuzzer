import os
import sys
import mechanize
from guess import Guess
from crawl import Crawl
from parse_url import ParseURL

class Discover(object):

    def __init__(self, args):
        path = os.getcwd()
        username = 'admin'
        password = 'password'
        base_url = args.url
        common_words = os.path.join(path, args.common_words)

        if not base_url.endswith('/'):
            base_url = base_url + '/'

        #Login
        print 'Logging in...'
        browser = mechanize.Browser()
        try:
            browser.open(base_url)
            browser.select_form(nr=0)
            browser.form['username'] = username
            browser.form['password'] = password
            browser.submit()
        except:
            print 'Unable to log in. Try again'
            sys.exit()
        #how to find cookies....  browser._ua_handlers['_cookies'].cookiejar

        crawler = Crawl(browser, base_url)
        print 'Crawling for urls...'
        crawled_urls = crawler.crawl()

        guesser = Guess(browser, common_words)
        print 'Guessing urls...'
        guessed_urls = guesser.guess(crawled_urls)

        found_urls = list(set(crawled_urls) - set(guessed_urls))

        urlParser = ParseURL()
        urlInputMap = urlParser.parse(found_urls)
        print self.makeAString(urlInputMap)

    def makeAString(self, urlInputMap):
        count = 1
        sexyString = ""
        for url in urlInputMap:
            sexyString += str(count) + '. ' + url + " "
            if urlInputMap[url] != "":
                sexyString += "\n       Input: " + urlInputMap[url]
            sexyString += '\n'
            count += 1
        return sexyString
