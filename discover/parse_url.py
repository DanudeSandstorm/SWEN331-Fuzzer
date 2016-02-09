class parse_url(object):

    def parseThis(self, url):
        input = ""
        index = url.find('?',0)
        char = url[index+1]
        if index == -1:
            return
        else:
            while char != '=':
                input += char
                index += 1
                char = url[index+1]
            return input
