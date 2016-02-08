import argparse

def main():
	def str2bool(v):
	    #susendberg's function
		return v.lower() in ("yes", "true", "t", "1")
	def msg(name='[discover | test]'): 
		return 'fuzz ' + name + ' url OPTIONS [-h]'

	# command line parsing
	parser = argparse.ArgumentParser(prog='fuzz', usage=msg())
	subparsers = parser.add_subparsers()	

	# discover parser
	d_parser = subparsers.add_parser('discover', usage=msg('discover'), help='Outputs a comprehensive, human-readable list of all discovered inputs to the system.\nTechniques include both crawling and guessing.')
	d_parser._optionals.title = 'additional arguments'
	d_parser.add_argument('url')
	d_parser.add_argument('--custom-auth', type=str, required=False, metavar='', help='Signal that the fuzzer should use hard-coded authentication for a specific application (e.g. dvwa).')
	d_parser.add_argument('--common-word', type=file, required=True, metavar='', help='REQUIRED Newline-delimited file of common words to be used in page guessing and input guessing.')
	
	# test parser
	t_parser = subparsers.add_parser('test', usage=msg('test'), help='Discovers all inputs, then attempts a list of exploit vectors on those inputs.\nReports potential vulnerabilities.')
	t_parser._optionals.title = 'additional arguments'
	t_parser.add_argument('url')
	#t_parser.register('type' 'bool', str2bool)
	t_parser.add_argument('--custom-auth', type=str, required=False, metavar='', help='Signal that the fuzzer should use hard-coded authentication for a specific application (e.g. dvwa).')
	t_parser.add_argument('--vectors', type=file, required=True, metavar='', help='REQUIRED Newline-delimited file of common exploits to vulnerabilities.')
	t_parser.add_argument('--sensitive', type=file, required=True, metavar='', help='REQUIRED Newline-delimited file data that should never be leaked.\nIt\'s assumed that this data is in the application\'s database (e.g. test data), but is not reported in any response.')
	t_parser.add_argument('--random', type=str2bool, default=False, metavar='', help='When off, try each input to each page systematically.\nWhen on, choose a random page, then a random input field and test all vectors. Default: false.')
	t_parser.add_argument('--slow', type=int, default=500, metavar='', help='Number of milliseconds considered when a response is considered "slow". Default is 500 milliseconds.')
	
	args = parser.parse_args()

if __name__ == '__main__':
    main()
