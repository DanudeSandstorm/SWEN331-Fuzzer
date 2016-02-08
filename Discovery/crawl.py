import requests

class crawl(object):
    base_url = ""
    base_url_content = ""
    url_list = []

    def __init__(self, base_url):
        self.base_url = base_url
        self.base_url_content = requests.get(base_url).content


    def findHref(self):
        indexList = []
        substring = 'href="/'
        currIndex = 0
        while currIndex != -1:
            currIndex = self.base_url_content.find(substring,currIndex+1)
            indexList.append(currIndex)
        return indexList

    def findUrls(self):
        indexList = self.findHref()
        print(indexList)
        for index in indexList[:-1]:
            url = ""
            charIndex = index+6
            char = self.base_url_content[charIndex]
            while char != '"':
                url += char
                charIndex += 1
                char = self.base_url_content[charIndex]
            self.url_list.append(url)
        print(self.url_list)


if __name__ == "__main__":
    newGuess = crawl("http://127.0.0.1/")
    #print(newGuess.findHref())
    newGuess.findUrls()


