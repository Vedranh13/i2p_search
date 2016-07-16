"""This is an i2p crawler writen in python 3.5.2"""
#TODO Make A verbose mode / status updates
#TODO Clean this up and make it not shite
import requests
proxy = {
'http' : 'http://127.0.0.1:4444'
}
from itertools import product
from string import ascii_lowercase, digits
def unMakeURL ( url ) -> str:
    return url.replace( "http://" , "" ).replace( ".i2p/" , "" )
def makeURL ( domain , isI2P = True ) -> str:
    if ( isI2P ):
        return ("http://" + domain + ".i2p/").replace( " " , "")
    #TODO Non-i2p domains and sub-domains and pages and ...
import threading
#TODO PAGES!!!!!!!!!!!!!!!!!!!!!
class eepsite (threading.Thread):
    def __init__ ( self , url ):
        threading.Thread.__init__(self)
        self.url = url
        self.isKnown = False
        self.isUp = False
        self.isEepsite = True
        self.isDown = False #TODO expand the crawler to make use of these fields and be "smarter" and do things like check which known sites are still up ...
    def run ( self ):
        if ( self.isKnown or not self.isEepsite ):
            return
            #TODO program in an "update" mode
        res = requests.get ( self.url , proxies = proxy )
        #print ( res.text )
        #print ( res.status_code )
        if "<h3>Website Not Found in Addressbook</h3>" in res.text: #then eepsite does not exist
            nonExistant = open ( "./non_eepsites.search" , "a" )
            nonExistant.write ( self.url + "\n" )
            nonExistant.close()
            #This records that this eepsite does not currently exist
        elif ( res.status_code == 200 ):  #then eepsite does exist and is up
            self.isKnown = True
            self.isUp = True
            knownSites = open ( "./known_eepsites.search" , "a" )
            knownSites.write ( self.url + "\n" )
            knownSites.close()
            upSites = open ( "./up_eepsites.search" , "a" )
            upSites.write ( self.url + "\n" )
            upSites.close()
            #This records that this url is in fact an eepsite and is currently online
            page = open ( "./eepsites/" + unMakeURL ( self.url ) , "w" ) #TODO sub-directories and other pages?
            page.write ( res.text )
            page.close
        else:
            #This means something unknown happened, possibly site exists but is not in Addressbook so i2p was sugessting a jump link?
            #TODO make something intelligent happen here
            somethingWeirdHappened = open ( "./somethingWeirdHappened.search" , "a" )
            somethingWeirdHappened.write ( self.url + "\n" )
            somethingWeirdHappened.close()
    def loadOldSites( self ):
        nonExistant = open ( "./non_eepsites.search" , "r" )
        for line in nonExistant:
            if self.url == line.strip():
                self.isEepsite = False
                #TODO Is it nessesary to close nonExistant here?
                return
        nonExistant.close()
        known = open ( "./known_eepsites.search" , "r" )
        for line in known:
            if self.url == line.strip():
                self.isKnown = True
                return
                #TODO the other fields?
        known.close()
sites = 0
from time import gmtime, strftime, sleep
#Write date on each file
#TODO Clean this up with a "logDate" function
nonExistant = open ( "./non_eepsites.search" , "a" )
somethingWeirdHappened = open ( "./somethingWeirdHappened.search" , "a" )
knownSites = open ( "./known_eepsites.search" , "a" )
nonExistant.write ( "# " + strftime ( "%c" ) + "\n" )
somethingWeirdHappened.write ( "# " + strftime ( "%c" ) + "\n" )
knownSites.write ( "# " + strftime ( "%c" ) + "\n" )
nonExistant.close()
somethingWeirdHappened.close()
knownSites.close()
for i in product(" " + ascii_lowercase + digits, repeat = 15):
    print ( sites )
    sites = sites + 1
    site = eepsite ( makeURL ( "".join(i) ) )
    site.loadOldSites()
    site.start()
    if ( threading.active_count() >= 30 ):
        print ( "Sleeping" )
        sleep(1) #TODO Figure out why there are duplicates on all lists, possibly something to do with sleeping?
#TODO Back this up to the rasp-pi
#TODO Make the rasp-pi a Bitcoin full node
