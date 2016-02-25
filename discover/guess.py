import mechanize
import sys

class Guess(object):
    browser = None
    base_url = None
    guesses = []
    extentions = ['/', '.php', '.jsp', '.html']

    def __init__(self, browser, base_url, file_name):
        self.browser = browser
        self.base_url = base_url
        try:
            with open(file_name) as file:
                for word in file:
                    self.guesses.append(word.replace(' ','')[:-1])
        except:
            print 'No such file:' + file_name
            sys.exit()

    def guess(self, urls):
        goodGuess = []
        for g in self.guesses:
            for ext in self.extentions:
                url_guess = self.base_url + g + ext
                try:
                    self.browser.open(url_guess).read()
                    goodGuess.append(url_guess)
                except mechanize.HTTPError as e:
                    pass
        return goodGuess
