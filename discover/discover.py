import os
from guess import Guess
from crawl import Crawl

class Discover(object):

    def __init__(self, args):
        #base_url = args.url
        #common_words = args.common_words
        #temp variables
        base_url = "http://127.0.0.1/"
        common_words = "\\discover\\common_words.txt"
        path = os.getcwd()

        newGuess = Guess(base_url, path+common_words)
        newCrawl = Crawl(base_url)

        guess = newGuess.startToGuess()
        crawl = newCrawl.findUrl(base_url)
        print guess
        print crawl

