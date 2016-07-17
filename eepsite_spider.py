#This containst the eepsite class and the makeURL method used in "spider.py"
import threading
import requests
import os
import params
import utils
#TODO Consider making an URL class
def unMakeURL ( url ) -> str:
    return url.replace( "http://" , "" ).replace( ".i2p/" , "" )
def makeURL ( domain , isI2P = True , isB32 = False , isHttp = True , isOnion = False ) -> str:
    url = domain.strip()
    if ( isHttp ):
        url = "http://" + url
    if ( isB32 ):
        url = url + ".b32"
    if ( isI2P ):
        url = url + ".i2p/"
    if ( isOnion ):
        pass
        #TODO crawl TOR too
    print (url.strip())
    return url.strip()
    #TODO Non-i2p domains and sub-domains and pages and ...
#TODO PAGES
class eepsite (threading.Thread):
    def __init__ ( self , url ):
        threading.Thread.__init__(self)
        self.url = url
        self.isKnown = False
        self.isUp = False
        self.isEepsite = True
        #TODO expand the crawler to make use of these fields and be "smarter" and do things like check which known sites are still up ...
    def run ( self ):
        if ( self.isUp or not self.isEepsite ):
            return
            #Former todo: program in an "update" mode - SOLVED THROUGH "UPDATE FLAG" IN "spider.py"
        res = requests.get ( self.url , proxies = params.proxy )
        #print ( res.text )
        #print ( res.status_code )
        if "<h3>Website Not Found in Addressbook</h3>" in res.text: #then eepsite does not exist
            utils.logDate ( params.path_to_non )
            with open ( params.path_to_non , "a" ) as nonExistant:
                nonExistant.write ( self.url + "\n" )
            #This records that this eepsite does not currently exist
        elif ( res.status_code == 200 ):  #then eepsite does exist and is up
            self.isKnown = True
            self.isUp = True
            if ".b32" in self.url:
                utils.logDate ( params.path_to_known ) #TODO clean up all these write with "with open ..."
                with open ( params.path_to_known , "a" ) as knownSites:
                    knownSites.write ( self.url + "\n" )
            utils.logDate ( params.path_to_up )
            with open ( params.path_to_up , "a" ) as upSites:
                upSites.write ( self.url + "\n" )
            #This records that this url is in fact an eepsite and is currently online
            page = open ( "./eepsites/" + unMakeURL ( self.url ) , "w" ) #TODO sub-directories and other pages?
            page.write ( res.text )
            page.close()
            #Creates a directory to hold the pages and sub-directories of this eepsite
            #TODO populate with content
            directory = "./eepsites/" + unMakeURL ( self.url ) + ".d"
            if not os.path.exists ( directory ):
                os.makedirs ( directory )
        elif "<h3>Website Unreachable</h3>" in res.text:
            #This most likely means the website is down
            utils.logDate ( params.path_to_down )
            with open ( params.path_to_down , "a" ) as down:
                down.write ( self.url + "\n" )
            self.isKnown = True
            #TODO possibly purge it from the Addressbook if it has been down more than a month?
        else:
            #Unknown event occured
            with open ( unMakeURL ( self.url ) + ".weird" , "w") as weird:
                weird.write ( res.text + "\n" )
                weird.write ( res.status_code )
            weird = open ( params.path_to_weird , "a" )
            weird.write ( self.url + "\n" )
            weird.close ()
    def loadOldSites ( self ):
        nonExistant = open ( params.path_to_non )
        for line in nonExistant:
            if self.url == line.strip():
                self.isEepsite = False
                #TODO Is it nessesary to close nonExistant here?
                return
        nonExistant.close()
        up = open ( params.path_to_up )
        for line in up:
            if self.url == line.strip():
                self.isUp = True
                return
                #TODO the other fields?
        up.close()
