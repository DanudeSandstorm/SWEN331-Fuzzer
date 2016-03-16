class ParseURL(object):

    def __init__(self):
        pass

    def parse(self, urls):
        urlInputMap = {}
        for url in urls:
            input = url.partition('?')[-1].rpartition('=')[0]
            if ';' in input:
                isInput = True
                urlInputMap[url] = []
                input = ''
                for char in input:
                    if char == '=':
                        isInput = False
                        urlInputMap[url].append(input)
                        input = ''
                    if isInput:
                        input += c
                    if char == ';':
                        isInput = True
        return urlInputMap
