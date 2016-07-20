#This containst the eepsite class and the makeURL method used in "spider.py"
import threading
import requests
import os
import params
import utils
#TODO Consider making an URL class
    #TODO Non-i2p domains and sub-domains and pages and ...
#TODO PAGES
class eepsite (threading.Thread):
    def __init__ ( self , url ):
        threading.Thread.__init__(self)
        self.url = url
        self.isKnown = False
        self.isUp = False
        self.isBlacklisted = False
        #TODO expand the crawler to make use of these fields and be "smarter" and do things like check which known sites are still up ...
    def run ( self ):
        if self.isKnown :
            return
            #Former todo: program in an "update" mode - SOLVED THROUGH "UPDATE FLAG" IN "spider.py"
        res = requests.get ( self.url , proxies = params.proxy )
        if ( res.status_code == 200 ):  #then eepsite does exist and is up
            self.isKnown = True
            self.isUp = True
            utils.logDate ( params.path_to_up )
            with open ( params.path_to_up , "a" ) as upSites:
                upSites.write ( self.url + "\n" )
            #This records that this url is in fact an eepsite and is currently online
            #page = open ( "./eepsites/" + unMakeURL ( self.url ) , "w" ) #TODO sub-directories and other pages?
            #page.write ( res.text )
            #page.close()
            #Creates a directory to hold the pages and sub-directories of this eepsite
            #TODO populate with content
            directory = "./eepsites/" + utils.unMakeUrl ( self.url ) + ".d"
            if not os.path.exists ( directory ):
                os.makedirs ( directory )
            path_to_page = directory + utils.unMakeURL ( self.url ) + ".main"
            with open ( path_to_page , "w" ) as page:
                page.write ( res.text )
        elif "<h3>Website Unreachable</h3>" in res.text:
            #This most likely means the website is down
            utils.logDate ( params.path_to_down )
            with open ( params.path_to_down , "a" ) as down:
                down.write ( self.url + "\n" )
            self.isKnown = True
            #FormerTODO possibly purge it from the Addressbook if it has been down more than a month? - NO, bad idea, just mark it as down and don't check it until "update mode" is run
        else:
            #Unknown event occured
            with open ( utils.unMakeURL ( self.url ) + ".weird" , "w") as weird:
                weird.write ( res.text + "\n" )
                weird.write ( res.status_code )
            weird = open ( params.path_to_weird , "a" )
            weird.write ( self.url + "\n" )
            weird.close ()
    def loadOldSites ( self ):
        with open( params.path_to_down ) as down:
            for line in down:
                if self.url == line.strip()
                    self.isKnown = True
                    return
        with open( params.path_to_up ) as up:
            for line in up:
                if self.url == line.strip():
                    self.isUp = True
                    self.isKnown = True
                    return
                #TODO the other fields?
        with open ( params.path_to_blacklist ) as black:
            for line in black:
                if self.url == line.strip():
                    self.isBlacklisted = True
                    self.isKnown = True
                    return
