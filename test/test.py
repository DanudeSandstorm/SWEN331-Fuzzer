import os
from response import Response

class Test(object):

	def __init__(self, args, browser):
		base_url = args.url
		path = os.getcwd()
		common_words = os.path.join(path, args.common_words)
		
		print 'TODO'
		resObj = Response(browser, 500)
		print(resObj.responseTimer(args.url))
		print(resObj.responseType(args.url))
