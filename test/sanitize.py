import re

class Sanitize(object):

    def __init__(self):
        pass

    def sanitized(self, input):
        badData = ['<', '>', '"', "'", "/"]  # add more to this
        while '&' in input:
            pattern = re.compile('&([#]\w+|\w+);')
            if pattern.search(input):
                if len(pattern.search(input).group()) < 4:
                    return False
                input = input[(input.find(pattern.search(input).group())+len(pattern.search(input).group())):]
                print input
            else:
                return False
        if any(substring in input for substring in badData):
            return False
        return True


    def toString(self, input):
        returnMe = "Input: " + input + "\n"
        returnMe += "Sanitized: " + str(self.sanitized(input))
        return returnMe

if __name__ == '__main__':
    input = '&#888;&#455;'
    sanitizer = Sanitize()
    print(sanitizer.toString(input))
