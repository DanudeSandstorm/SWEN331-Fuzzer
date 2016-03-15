class Sanitize(object):

	def __init__(self, args):
		print 'TODO'

	def sanitized(self, inputs):
		badData = ['<','>','"',"'"] #add more to this
		for i in inputs:
			for c in i:
				if c in badData:
					return False
		return True
