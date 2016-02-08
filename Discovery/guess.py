import requests

class guess(object):
    base_url = "http://127.0.0.1/"
    bad_url =  "http://127.0.0.1/adfdsfdasfjsdakfjqjeijfodjaoijfdoaijfiascnisdniqj/"
    guessThis = []
    goodGuess = []

    def __init__(self, base_url, file_name):
        self.base_url = base_url
        #self.guessThis = ["about","admin","applications","archives","custom","dashboard",
         #                 "employee","group","groups","index","login","password","passwords","people",
          #                "photos","phpinfo","profile","private","register","secure","security","secret",
           #               "tags","unlinked","upload","uploads","users","user"]
        with open(file_name) as file:
            for word in file:
                self.guessThis.append(word.replace(' ','')[:-1])
            print(self.guessThis)

    def startToGuess(self):
        boolTest = False
        for g in self.guessThis:
            url_guess = self.base_url + g
            if requests.get(url_guess).content != requests.get(self.bad_url).content:
                self.goodGuess.append(g)
            php_guess = self.base_url + g + ".php"
            if requests.get(php_guess).content != requests.get(self.bad_url).content:
                self.goodGuess.append(g+".php")
                print(requests.get(php_guess).content)
            jsp_guess = self.base_url + g + ".jsp"
            if requests.get(jsp_guess).content != requests.get(self.bad_url).content:
                self.goodGuess.append(g+".jsp")
            html_guess = self.base_url + g + ".html"
            if requests.get(html_guess).content != requests.get(self.bad_url).content:
                self.goodGuess.append(g+".html")
        print(self.goodGuess)


if __name__ == "__main__":
    newGuess = guess("http://127.0.0.1/","common_words.txt")
    newGuess.startToGuess()





