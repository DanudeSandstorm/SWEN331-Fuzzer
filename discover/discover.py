import os
import sys
import mechanize

from discover.form_params import form_params
from guess import Guess
from crawl import Crawl
from parse_url import ParseURL

class Discover(object):

    browser = None

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
        self.browser = mechanize.Browser()
        try:
            self.browser.open(base_url)
            self.browser.select_form(nr=0)
            self.browser.form['username'] = username
            self.browser.form['password'] = password
            self.browser.submit()
        except mechanize.FormNotFoundError:
            pass
        except:
            print 'Website not found. Check to see if url is valid.'
            sys.exit()

        print 'Collecting cookies...'
        cookies = self.fillCookieJar(self.browser)

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
        self.browser.open(url)
        forms = []
        for f in self.browser.forms():
            form = form_params(f)
            forms.append(form)
        return forms

    def fillCookieJar(self, self.browser):
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
            for param in urlInputMap[url]:
                if param != "":
                    sexyString += "\tInput: " + param + '\n'
            #comment out the next 4 lines to run w/o the forms printoutCom
            sexyString += "\n"
            sexyString += "       Form(s): "
            for form in self.findFormParams(url):
                sexyString += "\t\t" + form.toString()
            count += 1
        return sexyString
