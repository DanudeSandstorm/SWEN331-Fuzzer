class ParseURL(object):

    def __init__(self):
        pass

    def parse(self, urls):
        #TODO map the urls to params
        urlInputMap = {}
        for url in urls:
            input = url.partition('?')[-1].rpartition('=')[0]
            urlInputMap[url] = input
        return urlInputMap
