import mechanize
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
		self.browser.open(url)
