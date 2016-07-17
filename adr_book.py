#Code to update and clean adr_book.search
import requests
import params
import os
def readOneAdr ( raw_text = "" ):
    entry = raw_text.split ( sep = ".i2p=" )
    return entry[0].split ( sep = "#T")[0]
def cleanAdr_book ():
    cleaned_book = []
    with open ( params.path_to_raw ) as raw:
        for line in raw:
            cleaned_book.append ( readOneAdr ( raw_text = line ) )
    with open ( params.path_to_adr_book , "w" ) as adr_book:
        for adr in cleaned_book:
            adr_book.write ( adr + "\n" )
def updateAdr_book ():
    res = requests.head ( "http://i2host.i2p/cgi-bin/i2hostetag" , proxies = params.proxy )
    if ( int ( res.headers['content-length'] ) !=  os.stat ( params.path_to_raw ).st_size ):
        print ( "Attempting to fetch Addressbook from i2host.i2p" )
        res = requests.get ( "http://i2host.i2p/cgi-bin/i2hostetag" , proxies = params.proxy )
        #TODO progress bar?
        if ( res.status_code == 200 ):
            with open ( params.path_to_raw , "w" ) as raw:
                raw.write ( res.text )
        else:
            pass
        #TODO error handeling
    else:
        print ( "Addressbook up to date" )
        cleanAdr_book ()
def updateAndClean ():
    updateAdr_book ()
    cleanAdr_book ()
