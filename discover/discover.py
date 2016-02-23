import os
import mechanize
from guess import Guess
from crawl import Crawl

class Discover(object):

    def __init__(self, args):
        #base_url = args.url
        #common_words = args.common_words
        #temp variables
        base_url = "http://127.0.0.1/dvwa/"
        common_words = "\\discover\\common_words.txt"
        path = os.getcwd()

        #Login
        browser = mechanize.Browser()
        browser.open(base_url)
        browser.select_form(nr=0)
        browser.form['username'] = 'admin'
        browser.form['password'] = 'password'
        browser.submit()

        # s = requests.session()
        # r = s.get(base_url, verify = False)
        # print r.cookies
        # matchme = 'meta content="(.*)" name="csrf-token" /'
        # csrf = re.search(matchme, str(r.text))
        # print csrf

        # payload = {
        #     'username': 'admin',
        #     'password': 'password',
        #     'authenticity_token' : csrf.group(1),
        #     '_portal_session' : r.cookies["_portal_session"]
        # }

        # r = s.post(url,data=payload,verify = False)
        # print r.text

        # payload = {
        #     'username': 'admin',
        #     'password': 'pssword',
        # }

        # with requests.session() as c:
        #     print c.post(base_url + 'login.php', headers=user_agent, data=payload)
        #     response = c.get(base_url + 'index.php', headers=user_agent)
        #     print(response.text)

        #guess = Guess(browser, base_url, path+common_words)
        crawl = Crawl(browser, base_url)

        #print newGuess.startToGuess()
        crawled_urls = crawl.find_urls()
        print crawled_urls

