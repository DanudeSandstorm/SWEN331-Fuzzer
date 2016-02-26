import os
import sys
import mechanize

from guess import Guess
from crawl import Crawl
from parse_url import ParseURL
from form import Form

class Discover(object):

    browser = None

    def __init__(self, args):
        path = os.getcwd()
        base_url = args.url
        common_words = os.path.join(path, args.common_words)

        if not base_url.endswith('/'):
            base_url = base_url + '/'

        #Instantiate browser session
        self.browser = mechanize.Browser()

        #Login
        if args.custom_auth != None:
            print 'Attempting to log in...'
        if args.custom_auth.lower() == 'dvwa':
            try:
                self.browser.open(base_url)
                self.browser.select_form(nr=0)
                self.browser.form['username'] = 'admin'
                self.browser.form['password'] = 'password'
                self.browser.submit()
            except mechanize.FormNotFoundError:
                pass
            except:
                print 'Website not found. Check to see if url is valid.'
                sys.exit()
        elif args.custom_auth.lower() == 'bwapp':
            try:
                self.browser.open(base_url)
                self.browser.select_form(nr=0)
                self.browser.form['login'] = 'bee'
                self.browser.form['password'] = 'bug'
                self.browser.submit()
            except mechanize.FormNotFoundError:
                pass
            except:
                print 'Website not found. Check to see if url is valid.'
                sys.exit()

        print 'Throwing up cookies...'
        cookies = self.fillCookieJar()

        crawler = Crawl(self.browser, base_url)
        print 'Crawling for urls...'
        crawled_urls = crawler.crawl()

        guesser = Guess(self.browser, common_words)
        print 'Guessing urls...'
        guessed_urls = guesser.guess(crawled_urls)

        found_urls = list(set(crawled_urls) - set(guessed_urls))

        urlParser = ParseURL()
        print 'Parsing urls for inputs...'
        urlInputMap = urlParser.parse(found_urls)

        print cookies
        print self.makeAString(urlInputMap)

    def findFormParams(self, url):
        forms = []
        self.browser.open(url)
        for f in self.browser.forms():
            form = Form(f)
            forms.append(form)
        return forms

    def fillCookieJar(self):
        cookieJar =  "\nCookies:\n"
        count = 1
        for cookie in self.browser._ua_handlers['_cookies'].cookiejar:
            cookieJar += str(count) + '. ' + str(cookie) + '\n'
            count += 1
        return cookieJar

    def makeAString(self, urlInputMap):
        count = 1
        sexyString = ""
        for url in urlInputMap:
            sexyString += str(count) + '. ' + url + '\n'
            if urlInputMap[url] != "":
                sexyString += "\tInput: " + urlInputMap[url] + '\n'
            for form in self.findFormParams(url):
                sexyString += form.toString() + '\n'
            count += 1
        return sexyString
