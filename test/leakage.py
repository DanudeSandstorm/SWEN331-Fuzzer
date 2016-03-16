import sys

class Leakage(object):
    browser = None
    techWords = []

    def __init__(self, browser, file_name):
        self.browser = browser
        try:
            with open(file_name) as file:
                for word in file:
                    self.techWords.append(word.replace(' ','')[:-1])
        except:
            print 'No such file:' + file_name
            sys.exit()

    def findLeaks(self, url):
        foundTW = []
        response = self.browser.open(url)
        book = response.read()
        for tw in self.techWords:
            if tw in book:
                foundTW.append(tw)

        if len(foundTW) >= 1:
            returnMe = "List of technical words:\n"
            for tw in foundTW:
                returnMe += tw + "\n"
            return returnMe

        return "No technical words were found "
