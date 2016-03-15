import os

from guess import Guess
from crawl import Crawl
from parse_url import ParseURL
from form import Form

class Discover(object):

    def __init__(self, args, browser):
        base_url = args.url
        path = os.getcwd()
        common_words = os.path.join(path, args.common_words)

        print 'Throwing up cookies...'
        cookies = self.fillCookieJar(browser)

        crawler = Crawl(browser, base_url)
        print 'Crawling for urls...'
        crawled_urls = crawler.crawl()

        guesser = Guess(browser, common_words)
        print 'Guessing urls...'
        guessed_urls = guesser.guess(crawled_urls)

        found_urls = list(set(crawled_urls) - set(guessed_urls))

        urlParser = ParseURL()
        print 'Parsing urls for inputs...'
        urlInputMap = urlParser.parse(found_urls)

        print cookies
        print self.makeAString(browser, urlInputMap)

    def fillCookieJar(self, browser):
        cookieJar =  "\nCookies:\n"
        count = 1
        for cookie in browser._ua_handlers['_cookies'].cookiejar:
            cookieJar += str(count) + '. ' + str(cookie) + '\n'
            count += 1
        return cookieJar

    def makeAString(self, browser, urlInputMap):
        count = 1
        sexyString = ""
        for url in urlInputMap:
            sexyString += str(count) + '. ' + url + '\n'
            if urlInputMap[url] != "":
                sexyString += "\tInput: " + urlInputMap[url] + '\n'
            for form in self.findFormParams(browser, url):
                sexyString += form.toString() + '\n'
            count += 1
        return sexyString

    def findFormParams(self, browser, url):
        forms = []
        browser.open(url)
        for f in browser.forms():
            form = Form(f)
            forms.append(form)
        return forms
