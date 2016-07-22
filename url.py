# This class repersents URLs
class url(object):
    def __init__(self , path):
        self.url = path
        self.http = False
        self.https = False
        self.i2p = False
        self.onion = False
        self.freenet = False
        self.page = False
        self.valid = False
        self.up = False # TODO change the way we test if up or not? Just a single head and check the status code?
        self.classify()
        self.domain = self.getDomain()
        self.relative_path = self.getRelativePath()

    def classify(self):
        if "http://" in self.url:
            self.http = True
        elif "https://" in self.url:
            self.https = True
        else:
            self.valid = False
        if ".i2p/" in self.url:
            self.i2p = True
        elif ".onion/" in self.url:
            self.onion = True
        elif ".freenet/" in self.url:
            self.freenet = True
        else:
            self.valid = False
        if not self.url[-1] == "/": # Might not work?
            self.page = True

    def getDomain(self):
        if self.http:
            return self.url.replace("http://" , "").split("/")[0] + "/"
        if self.https:
            return self.url.replace("https://" , "").split("/")[0] + "/"

    def getRelativePath(self):
        return self.url.replace(self.domain,"")
