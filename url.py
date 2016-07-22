# This class repersents URLs
import params
import utils
class url(object):
    def __init__(self , link):
        self.proto = ""
        self.url = link
        self.full_url = link
        self.http = False
        self.https = False
        self.i2p = False
        self.onion = False
        self.freenet = False
        self.page = False
        self.internal = False
        self.valid = True
        self.up = False # TODO change the way we test if up or not? Just a single head and check the status code?
        self.domain = ""
        self.classify()
        self.relative_path = self.getRelativePath()
        self.file_path = self.getFilePath()

    def __repr__(self):
        return self.url

    def classify(self):
        if "http://" in self.url:
            self.http = True
            self.proto = "http://"
        elif "https://" in self.url:
            self.https = True
            self.proto = "https://"
        else:
            self.internal = True
            return
        self.domain = self.getDomain()
        if (self.proto + self.domain) in self.url:
            self.internal = True
            return
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
            return self.url.replace("http://" , "").split("/")[0]
        if self.https:
            return self.url.replace("https://" , "").split("/")[0]

    def getRelativePath(self):
        return self.url.replace(self.domain,"").replace(self.proto , "")

        """
    def unMakeURL ( url ):
        url = url.replace("http://" , "")
        url = url.replace(".i2p/" , "").replace(".i2p" , "")
        return url
        # return url.replace( "http://" , "" ).replace( ".i2p/" , "" )
        """

    def getFilePath(self):
        path = params.path_to_eepsites
        path = path + self.domain + self.relative_path + ".index"
        # utils.createFile(path)
        return path

    def URLFromPath (cls, domain , isI2P = True , isHttp = True , isOnion = False ):
        url = domain.strip()
        if not "http://" in url and isHttp:
            url = "http://" + url
        #TODO implement other variants
        return cls(url)

    URLFromPath = classmethod(URLFromPath)
