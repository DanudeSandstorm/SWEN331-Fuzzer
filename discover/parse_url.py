class ParseURL(object):

    def __init__(self):
        pass

    def parse(self, urls):
        urlInputMap = {}
        for url in urls:
            param = url.partition('?')[-1].rpartition('=')[0]
            urlInputMap.setdefault(url, param)
        return urlInputMap
