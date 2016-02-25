import os
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
        browser = mechanize.Browser()
        browser.open(base_url)
        browser.select_form(nr=0)
        browser.form['username'] = username
        browser.form['password'] = password
        browser.submit()

        crawler = Crawl(browser, base_url)
        crawled_urls = crawler.crawl()
        print crawled_urls

        


        # guesser = Guess(browser, common_words)
        # guessed_urls = guesser.guess(crawled_urls)
        # print guessed_urls

        # found_urls = crawled_urls + guessed_urls

        #TODO
        # Return map url to its paramaters
        # parser = ParseURL()
        # url_params = parser.parse(found_urls)
        # print url_params
