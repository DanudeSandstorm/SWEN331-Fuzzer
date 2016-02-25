import mechanize
from bs4 import BeautifulSoup

class Crawl(object):
    substring = 'href="'
    base_url = ''
    browser = None
    url_list = []
    keeper_list = []

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.url_list.append(base_url)

    def crawl(self):
        if len(self.url_list) <= 0:
            return self.keeper_list

        url = self.url_list.pop()
        if (
            url not in self.keeper_list and
            not url.endswith('logout.php')
        ):
            self.keeper_list.append(url)
            try:
                url_content = self.browser.open(url).read()
                soup = BeautifulSoup(url_content, 'html.parser')

                for link in soup.find_all('a'):
                    urlExt = link.get('href')

                    if (
                        urlExt != None and
                        'http' not in urlExt and
                        not urlExt.startswith('../')
                    ):
                        #Formatting
                        urlExt = urlExt.encode('ascii', 'ignore')
                        urlExt = urlExt.split('%22', 1)[0]
                        if urlExt.startswith('/'):
                            urlExt = urlExt[1:]
                        if urlExt.endswith('.'):
                            urlExt = urlExt[:-1]

                        if '/' in urlExt:
                            moreExt = urlExt.split('/')[:-1]
                            moreExt = [s + '/' for s in moreExt]
                            for i in xrange(len(moreExt)):
                                self.url_list.append(self.base_url + ''.join(moreExt[0:i]))

                        self.url_list.append(self.base_url + urlExt)
            except mechanize.HTTPError as e:
                pass

        return self.crawl()
        

