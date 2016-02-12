class parse_url(object):

    def parseThis(self, url):
        return url.partition('?')[-1].rpartition('=')[0]

