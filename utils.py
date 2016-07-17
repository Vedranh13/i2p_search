#Commonly used methods
from time import strftime
def logDate ( path , perm = "a" ):
    myFile = open ( path , perm )
    myFile.write ( "# " + strftime ( "%c" ) + "\n" )
    myFile.close()
    #TODO fix race-condition
