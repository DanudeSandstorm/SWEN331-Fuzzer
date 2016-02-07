import requests

class guess(object):
    base_url = "http://127.0.0.1/"
    bad_url =  "http://127.0.0.1/adfdsfdasfjsdakfjqjeijfodjaoijfdoaijfiascnisdniqj/"
    guessThis = []
    goodGuess = []

    def __init__(self):
        self.guessThis = ["admin","employee","private","dashboard","secure","profile",
                          "users","user","password","applications","phpinfo"]

    def startToGuess(self):
        boolTest = False
        for g in self.guessThis:
            url_guess = self.base_url + g
            if requests.get(url_guess).content != requests.get(self.bad_url).content:
                self.goodGuess.append(g)
            php_guess = self.base_url + g + ".php"
            if requests.get(php_guess).content != requests.get(self.bad_url).content:
                self.goodGuess.append(g+".php")
            jsp_guess = self.base_url + g + ".jsp"
            if requests.get(jsp_guess).content != requests.get(self.bad_url).content:
                self.goodGuess.append(g+".jsp")
            html_guess = self.base_url + g + ".html"
            if requests.get(html_guess).content != requests.get(self.bad_url).content:
                self.goodGuess.append(g+".html")
        print(self.goodGuess)


if __name__ == "__main__":
    newGuess = guess()
    newGuess.startToGuess()





