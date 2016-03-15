import re

class Sanitize(object):
    input = None
    def __init__(self, input):
        self.input = input

    def sanitized(self, input):
        badData = ['<', '>', '"', "'", "/"]  # add more to this
        while '&' in input:
            pattern = re.compile('&[#]\w+;|&\w+;')
            if pattern.search(input):
                if len(pattern.search(input).group()) < 4:
                    return False
                input = input[(input.find(pattern.search(input).group())+len(pattern.search(input).group())):]
            else:
                return False
        if any(substring in input for substring in badData):
            return False
        return True


    def toString(self):
        returnMe = "Input: " + self.input + "\n"
        returnMe += "Sanitized: " + str(self.sanitized(self.input))
        return returnMe

if __name__ == '__main__':
    input = '&#888;&#455;'
    sanitizer = Sanitize(input)
    print(sanitizer.toString())