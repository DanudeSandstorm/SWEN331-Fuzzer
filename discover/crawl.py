import requests

class Crawl(object):
    base_url = ""
    curr_url = ""
    url_content = ""
    url_list = []
    keeper_list = []

    def __init__(self, base_url):
        self.base_url = base_url
        self.url_content = requests.get(base_url).content


    def findHref(self, url):
        self.url_content = requests.get(url).content
        indexList = []
        substring = 'href="/'
        currIndex = 0
        while currIndex != -1:
            currIndex = self.url_content.find(substring,currIndex+1)
            indexList.append(currIndex)
        return indexList

    def findUrls(self, url):
        if url in self.keeper_list:
            if len(self.url_list) > 0:
                newUrl = self.url_list.pop(0)
                self.findUrls(newUrl)
            else:
                return self.keeper_list
        else:
            self.keeper_list.append(url)
            indexList = self.findHref(url)
            for index in indexList[:-1]:
                urlExt = ""
                charIndex = index+7
                char = self.url_content[charIndex]
                while char != '"':
                    urlExt += char
                    charIndex += 1
                    char = self.url_content[charIndex]
                self.url_list.append(self.base_url + urlExt)
            if len(self.url_list) > 0:
                newUrl = self.url_list.pop(0)
                self.findUrls(newUrl)
            else:
                return self.keeper_list

