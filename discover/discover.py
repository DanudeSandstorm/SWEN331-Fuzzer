import os
import mechanize
from guess import Guess
from crawl import Crawl

class Discover(object):

    def __init__(self, args):
        #base_url = args.url
        #common_words = args.common_words
        #temp variables
        base_url = "http://127.0.0.1/dvwa/"
        common_words = "\\discover\\common_words.txt"
        path = os.getcwd()

        #Login
        browser = mechanize.Browser()
        browser.open(base_url)
        browser.select_form(nr=0)
        browser.form['username'] = 'admin'
        browser.form['password'] = 'password'
        browser.submit()

        guess = Guess(browser, base_url, path + common_words)
        guessed_urls = guess.startToGuess()
        print guessed_urls

        crawl = Crawl(browser, base_url)
        crawled_urls = crawl.find_urls()
        print crawled_urls

