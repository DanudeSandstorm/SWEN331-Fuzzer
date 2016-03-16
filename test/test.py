import os
from response import Response
from sanitize import Sanitize
from leakage import Leakage

class Test(object):

	def __init__(self, args, browser):
		base_url = args.url
		path = os.getcwd()
		sensitive = os.path.join(path, args.sensitive)

		#TODO Sanitize
		sanitize = Sanitize()

		leakage = Leakage(browser, sensitive)
		resObj = Response(browser, args.slow)

		url = 'http://127.0.0.1/dvwa/'
		print url
		print leakage.findLeaks(url)
		print(resObj.responseTimer(url))
		print(resObj.responseType(url))
