import mechanize

class Form(object):
    form = None
    name = None

    def __init__(self, form):
        self.form = form
        if hasattr(form, 'name'):
            self.name = form.name if form.name != None else "<NO NAME>"
        else:
            self.name = "<NO NAME>"

    def toString(self):
        iLookGood = "\tForm Name: " + self.name + "\n"
        if hasattr(self.form, 'controls'):
            iLookGood += '\tForm Control:\n'
            for control in self.form.controls:
                iLookGood += '\t\t' + str(control) + '\n'
                if control.type == "select":
                    for item in control.items:
                        print " name=%s values=%s" % (item.name, str([label.text  for label in item.get_labels()]))
        return iLookGood
