from bs4 import BeautifulSoup

class Sanitize(object):

    browser = None

    def __init__(self, browser):
        self.browser = browser

    def isURLSanitized(self, url_vector):
        response = self.browser.open(url_vector)
        if ('chipotle' in response.read()):
            return False
        return True

    def isFormSanitized(self, url, form, vector):
        return True
