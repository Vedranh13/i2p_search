# Commonly used methods
from time import strftime
import os
import url
def logDate ( path , perm = "a" ):
    myFile = open ( path , perm )
    myFile.write ( "# " + strftime ( "%c" ) + "\n" )
    myFile.close()
    #TODO fix race-condition / lock

def createFile(path):
    os.makedirs(os.path.dirname(path) , exist_ok=True)
    if not os.path.exists(path):
        myFile = open(path , "x")
        myFile.close()
