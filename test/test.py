import os
from response import Response
from sanitize import Sanitize
from leakage import Leakage
import random


class Test(object):
    printer = ''

    def __init__(self, args, browser, urlMap):
        base_url = args.url
        path = os.getcwd()
        sensitive = os.path.join(path, args.sensitive)
        vectors = os.path.join(path, args.vectors)

        rando = args.random

        sanitize = Sanitize(browser)
        leakage = Leakage(browser, sensitive)
        resObj = Response(browser, args.slow)

        printMe = ''

        if rando == False:
            for url in urlMap:
                printMe += "Information regarding " + url + ":\n"
                printMe += leakage.findLeaks(url) + "\n"
                printMe += resObj.responseType(url) + "\n"
                printMe += resObj.responseTimer(url) + "\n"
                for v in vectors:

                    for form in urlMap[url][1]:
                        printMe += "Form Inputs Sanitized: " + str(sanitize.isFormSanitized(url, form, v)) + "\n"

                    for input in urlMap[url][0]:
                        urlAndInput = url + input + "="
                        urlAndVector = urlAndInput + v
                        printMe += "URL Inputs Sanitized: " + str(sanitize.isURLSanitized(urlAndVector)) + "\n"
                        printMe += "Information regarding " + url + ":\n"
                        printMe += leakage.findLeaks(urlAndVector) + "\n"
                        printMe += resObj.responseType(urlAndVector) + "\n"
                        printMe += resObj.responseTimer(urlAndVector) + "\n"

        elif rando == True:
            input = None
            form = None

            key = random.sample(urlMap,1)[0]

            printMe += "Information regarding " + key + ":\n"
            printMe += leakage.findLeaks(key) + "\n"
            printMe += resObj.responseType(key) + "\n"
            printMe += resObj.responseTimer(key) + "\n"

            vector = random.sample(vectors, 1)[0]

            if len(urlMap[key][0]) >= 1:
                input = random.choice(urlMap[key][0])
                urlAndVector = key+input+"="+vector
                printMe += "URL Inputs Sanitized: " + str(sanitize.isURLSanitized(urlAndVector)) + "\n"
                printMe += "Information regarding " + urlAndVector + ":\n"
                printMe += leakage.findLeaks(urlAndVector) + "\n"
                printMe += resObj.responseType(urlAndVector) + "\n"
                printMe += resObj.responseTimer(urlAndVector) + "\n"

            if len(urlMap[key][1]) >= 1:    
                form = random.choice(urlMap[key][1])
                printMe += "Form Inputs Sanitized: " + str(sanitize.isFormSanitized(key, form, vector)) + "\n"

        else:
            print "What is random? It isn't true and it isn't false... uh oh..."

        self.printer = printMe

    def toString(self):
        return self.printer
