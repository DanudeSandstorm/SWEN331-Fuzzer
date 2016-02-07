import requests

class guess(object):
    base_url = "http://127.0.0.1/"
    bad_url =  "http://127.0.0.1/adfdsfdasfjsdakfjqjeijfodjaoijfdoaijfiascnisdniqj/"
    guessThis = []
    goodGuess = []

    def __init__(self):
        self.guessThis = ["admin","employee","private"]

    def startToGuess(self):
        for g in self.guessThis:
            url_guess = self.base_url + g
            if requests.get(url_guess)._content is not requests.get(self.bad_url)._content:
                self.goodGuess.append(self, g)





