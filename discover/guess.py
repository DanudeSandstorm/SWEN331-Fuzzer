import mechanize

class Guess(object):
    browser = None
    base_url = None
    bad_url =  "http://127.0.0.1/adfdsfdasfjsdakfjqjeijfodjaoijfdoaijfiascnisdniqj/"
    guessThis = []
    goodGuess = []

    def __init__(self, browser, base_url, file_name):
        self.browser = browser
        self.base_url = base_url
        with open(file_name) as file:
            for word in file:
                self.guessThis.append(word.replace(' ','')[:-1])

    def startToGuess(self):
        for g in self.guessThis:
            url_guess = self.base_url + g
            if self.browser.open(url_guess).read() != self.browser.open(self.bad_url).read():
                self.goodGuess.append(g)
            php_guess = self.base_url + g + ".php"
            if self.browser.open(php_guess).read() != self.browser.open(self.bad_url).read():
                self.goodGuess.append(g+".php")
            jsp_guess = self.base_url + g + ".jsp"
            if self.browser.open(jsp_guess).read() != self.browser.open(self.bad_url).read():
                self.goodGuess.append(g+".jsp")
            html_guess = self.base_url + g + ".html"
            if self.browser.open(html_guess).read() != self.browser.open(self.bad_url).read():
                self.goodGuess.append(g+".html")
        return self.goodGuess
