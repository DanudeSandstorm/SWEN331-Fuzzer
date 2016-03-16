class ParseURL(object):

    def __init__(self):
        pass

    def parse(self, urls):
        urlInputMap = {}
        for url in urls:
            input = url.partition('?')[-1].rpartition('=')[0]
            urlInputMap[url] = []
            if ';' in input:
                isInput = True
                newInput = ''
                for char in input:
                    if char == '=':
                        isInput = False
                        urlInputMap[url].append(newInput)
                        newinput = ''
                    if isInput:
                        newInput += char
                    if char == ';':
                        isInput = True
        return urlInputMap
