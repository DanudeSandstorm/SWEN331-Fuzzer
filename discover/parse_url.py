class ParseURL(object):

    def __init__(self):
        pass

    def parse(self, urls):
        #TODO map the urls to params
        urlInputMap = {}
        for url in urls:
            input = url.partition('?')[-1].rpartition('=')[0]
            if ';' in input:
                isInput = True
                newInput = ""
                for c in input:
                    if c == '=':
                        isInput = False
                    if isInput:
                        newInput += c
                    if c == ';':
                        isInput = True
                        newInput += " and "
                input = newInput
            urlInputMap[url] = input
        return urlInputMap
