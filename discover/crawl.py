import requests

class crawl(object):
    base_url = ""
    curr_url = ""
    url_content = ""
    url_list = []
    keeper_list = []

    def __init__(self, base_url):
        self.base_url = base_url
        self.url_content = requests.get(base_url).content


    def findHref(self, url):
        url_content = requests.get(url).content
        indexList = []
        substring = 'href="/'
        currIndex = 0
        while currIndex != -1:
            currIndex = self.url_content.find(substring,currIndex+1)
            indexList.append(currIndex)
        return indexList

    def findUrls(self, url):
        if url in self.keeper_list:
            newUrl = self.base_url + self.url_list.pop()
            self.findUrls(newUrl)
        else:
            self.keeper_list.append(url)
            indexList = self.findHref(url)
            print(indexList)
            for index in indexList[:-1]:
                urlExt = ""
                charIndex = index+6
                char = self.url_content[charIndex]
                while char != '"':
                    urlExt += char
                    charIndex += 1
                    char = self.url_content[charIndex]
                self.url_list.append(url+urlExt)
            newUrl = self.base_url + self.url_list.pop()
            print(newUrl)
            #print(self.url_list[:-1])
            self.findUrls(newUrl)


if __name__ == "__main__":
    newGuess = crawl("http://127.0.0.1/")
    #print(newGuess.findHref())
    newGuess.findUrls(newGuess.base_url)