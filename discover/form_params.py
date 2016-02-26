import mechanize

class form_params(object):
    index = None
    form = None
    name = None
    control = None

    def __init__(self, form):
        self.form = form
        self.index = form.index
        self.name = form.name
        self.control = form.controls

    def toString(self):
        iLookGood = self.index + ". "
        iLookGood += "Name: " + self.name + "\n     "
        iLookGood += "Control: " + self.control + "\n"

# if __name__ == "__main__":
#     browser = mechanize.Browser()
#     browser.open("http://127.0.0.1/dashboard/")
#     index = 0
#     print browser.forms()
#     for f in browser.forms():
#         form = form_params(browser, index)
#         print form.toString()
#         index += 1

