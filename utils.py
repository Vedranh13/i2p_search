# Commonly used methods
from time import strftime
import os
def logDate ( path , perm = "a" ):
    myFile = open ( path , perm )
    myFile.write ( "# " + strftime ( "%c" ) + "\n" )
    myFile.close()
    #TODO fix race-condition / lock
def unMakeURL ( url ):
    url = url.replace("http://" , "")
    url = url.rstrip(".i2p/").replace(".i2p" , "")
    return url
    # return url.replace( "http://" , "" ).replace( ".i2p/" , "" )
def makeURL ( domain , isI2P = True , isHttp = True , isOnion = False ) -> str:
    url = domain.strip()
    if ( isHttp ):
        url = "http://" + url
    if ( isI2P ):
        url = url + ".i2p/"
    if ( isOnion ):
        pass
        #TODO crawl TOR too
    print (url.strip())
    return url.strip()

def createFile(path):
    os.makedirs(os.path.dirname(path) , exist_ok=True)
    myFile = open(path , "x")
    myFile.close()
