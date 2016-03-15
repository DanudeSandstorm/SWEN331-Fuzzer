import re

class Sanitize(object):
    def __init__(self):
        print 'TODO'

    def sanitized(self, inputs):
        badData = ['<', '>', '"', ' ']  # add more to this
        for i in inputs:
            for c in i:
                if c in badData:
                    return False
                if c == '&':
                    self.isAndSanitized(i)
        return True

    def isAndSanitized(self, input):

        while '&' in input:
            pattern = re.compile('&\w+;')
            #matched = re.search(r'&\w+;', input)
            if pattern.search(input):
                print(pattern.search(input).group())
                input = input[(input.find(pattern.search(input).group())+len(pattern.search(input).group())):]
            else:
                return False
        return True


        # escaped = ["&quot;", "&amp;", "&nbsp;", "&lt;", "&gt;"]
        # tempInput = input
        # while tempInput[0] != '&':
        #     tempInput = tempInput[1:]
        # count = tempInput.count('&')
        # currCheck = 4   #the length of the shortest escaped character
        # finCheck = 6    #the length of the longest escaped character
        # while count > 0:
        #     while currCheck <= finCheck:    # <= length of the longest escaped character
        #         if len(tempInput) < 4:
        #             return False
        #         else:
        #             if tempInput[0:currCheck+1] in escaped & count == 1:
        #                 return True
        #             elif tempInput[0:currCheck] in escaped & count > 1:
        #                 tempInput = tempInput[currCheck:]
        #     count -= 1


if __name__ == '__main__':
    sanitizer = Sanitize()
    input = "&&&"
    sanitizer.isAndSanitized(input)