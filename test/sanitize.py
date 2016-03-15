import re

class Sanitize(object):
    def __init__(self):
        print 'TODO'

    def sanitized(self, inputs):
        badData = ['<', '>', '"', "'"]  # add more to this
        while '&' in input:
            pattern = re.compile('&\w+;')
            #matched = re.search(r'&\w+;', input)
            if pattern.search(input):
                if len(pattern.search(input).group()) < 4:
                    return False
                input = input[(input.find(pattern.search(input).group())+len(pattern.search(input).group())):]
            else:
                return False
        if any(substring in input for substring in badData):
            return False
        return True

if __name__ == '__main__':
    sanitizer = Sanitize()
    input = '&#88;'
    print(sanitizer.sanitized(input))