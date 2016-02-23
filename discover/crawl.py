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

    def find_hrefs(self, url_content):
        indexList = []
        currIndex = 0
        while currIndex != -1:
            currIndex = url_content.find(self.substring, currIndex+1)
            indexList.append(currIndex)
        return indexList

    def find_urls(self):
        if len(self.url_list) <= 0:
            return self.keeper_list

        url = self.url_list.pop()
        if url not in self.keeper_list:
            self.keeper_list.append(url)

            url_content = self.browser.open(url).read()
            indexList = self.find_hrefs(url_content)
            
            for index in indexList[:-1]:
                urlExt = ""
                charIndex = index + len(self.substring)
                char = url_content[charIndex]
                
                while char != '"':
                    urlExt += char
                    charIndex += 1
                    char = url_content[charIndex]
                
                if 'http' not in urlExt:
                    self.url_list.append(self.base_url + urlExt)
            
        return self.find_urls()

