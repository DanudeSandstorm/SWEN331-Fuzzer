import os

from guess import Guess
from crawl import Crawl
from parse_url import ParseURL
from form import Form

class Discover(object):
    urlMap = {} #Dictionary of urls with array of inputs and forms
    cookies = ''
    browser = None

    def __init__(self, args, browser):
        self.browser = browser
        base_url = args.url
        path = os.getcwd()
        common_words = os.path.join(path, args.common_words)

        print 'Throwing up cookies...'
        self.cookies = self.fillCookieJar()

        crawler = Crawl(browser, base_url)
        print 'Crawling for urls...'
        crawled_urls = crawler.crawl()

        # guesser = Guess(browser, common_words)
        # print 'Guessing urls...'
        # guessed_urls = guesser.guess(crawled_urls)

        # found_urls = list(set(crawled_urls) - set(guessed_urls))
        found_urls = crawled_urls

        urlParser = ParseURL()
        print 'Parsing urls for inputs...'
        urlInputMap = urlParser.parse(found_urls)
        print urlInputMap
        for url in urlInputMap:
            self.urlMap[url] = []
            self.urlMap[url].append(urlInputMap[url])

        print 'Finding forms...'
        for url in self.urlMap:
            self.urlMap[url].append(self.findFormParams(self.browser, url))


    def returnUrlMap(self):
        return self.urlMap

    def fillCookieJar(self):
        cookieJar =  "\nCookies:\n"
        count = 1
        for cookie in self.browser._ua_handlers['_cookies'].cookiejar:
            cookieJar += str(count) + '. ' + str(cookie) + '\n'
            count += 1
        return cookieJar

    def toString(self):
        count = 1
        sexyString = ""
        sexyString += self.cookies + '\n'
        for url in self.urlMap:
            sexyString += str(count) + '. ' + url + '\n'
            for i in self.urlMap[url][0]:
                sexyString += "\tInput: " + i + '\n'
            for f in self.urlMap[url][1]:
                form = Form(f)
                sexyString += form.toString() + '\n'
            count += 1
        return sexyString

    def findFormParams(self, browser, url):
        forms = []
        browser.open(url)
        for f in browser.forms():
            forms.append(form)
        return forms
