import mechanize
import time

class Response(object):
    browser = None
    maxTime = None

    def __init__(self, browser, maxTime):
        self.browser = browser
        self.maxTime = maxTime

    def responseTimer(self, url):
        timeStart = lambda: int(round(time.time() * 1000))
        self.browser.open(url)
        timeEnd = lambda: int(round(time.time() * 1000))
        return timeEnd()-timeStart()

    def responseType(self, url):
        codes = {100:"Informational: Continue", 101:"Informational: Switching Protocols",
                 200:"Success: OK", 201:"Success: Created",202:"Success: Accepted",
                 203:"Success: Non-Authoritative Information", 204:"Success: No Content",
                 205:"Success: Reset Content", 206:"Success: Partial Content", 300: "Redirection: Multiple Choices",
                 301:"Redirection: Moved Permanently", 302:"Redirection: Found", 303:"Redirection: See Other",
                 304:"Redirection: Not Modified", 305:"Redirection: Use Proxy", 307:"Redirection: Temporary Redirect",
                 400:"Client Error: Bad Request", 401:"Client Error: Unauthorized", 402:"Client Error: Payment Required",
                 403:"Client Error: Forbidden", 404:"Client Error: Not Found", 405:"Client Error: Method Not Allowed",
                 406:"Client Error: Not Acceptable", 407:"Client Error: Proxy Authentication Required",
                 408:"Client Error: Request Timeout", 409:"Client Error: Conflict", 410:"Client Error: Gone",
                 411:"Client Error: Length Required", 412:"Client Error: Precondiction Failed", 413:"Client Error: Request Entity Too Large",
                 414:"Client Error: Request-URI Too Long",415:"Client Error: Unsupported Media Type",416:"Client Error: Requested Range Not Satisfiable",
                 417:"Client Error: Expectation Failed", 500:"Expectation Failed: Internal Server Error", 501:"Expectation Failed: Not Implemented",
                 502:"Expectation Failed: Bad Gateway", 503:"Expectation Failed: Service Unavailable",
                 504:"Expectation Failed: Gateway Timeout", 505:"Expectation Failed: HTTP Version Not Supported"}

        try:
            code = self.browser.open(url).code
            return str(code) + " - " + codes[code]
        except mechanize.HTTPError as e:
            return str(e)
