import requests

class cookies(object):

    def findCookies(self, url):
        return requests.get(url).cookies