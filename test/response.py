import mechanize
import time

class Response(object):
    browser = None
    maxTime = None

    def __init__(self, browser, maxTime):
        self.browser = browser
        self.maxTime = maxTime

    def responseTimer(self, url):
        timeStart = lambda: int(round(time.time() * 1000))
        self.browser.open(url)
        timeEnd = lambda: int(round(time.time() * 1000))
        return timeEnd-timeStart

    def responseType(self, url):
        response = self.browser.open(url)
        return response.code
