import mechanize
import sys

class Guess(object):
    browser = None
    guesses = []
    extentions = ['/', '.php', '.jsp', '.html']

    def __init__(self, browser, file_name):
        self.browser = browser
        try:
            with open(file_name) as file:
                for word in file:
                    self.guesses.append(word.replace(' ','')[:-1])
        except:
            print 'No such file:' + file_name
            sys.exit()

    def guess(self, urls):
        goodGuess = []
        for base_url in urls:
            if not base_url.endswith('/'):
                continue      
            for guess in self.guesses:
                for ext in self.extentions:
                    url_guess = base_url + guess + ext
                    try:
                        self.browser.open(url_guess).read()
                        goodGuess.append(url_guess)
                    except mechanize.HTTPError as e:
                        pass
        return goodGuess
