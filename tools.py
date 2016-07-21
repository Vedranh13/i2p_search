import sys, getopt
from adr_book import updateAndClean
import params
def createAllFiles ():
    with open ( params.path_to_raw , "x" ) as temp:
        pass
    with open ( params.path_to_up , "x" ) as temp:
        pass
    with open ( params.path_to_down , "x" ) as temp:
        pass
    with open ( params.path_to_known , "x" ) as temp:
        pass
    with open ( params.path_to_non , "x" ) as temp:
        pass
    with open ( params.path_to_weird , "x" ) as temp:
        pass
    with open ( params.path_to_adr_book , "x" ) as temp:
        pass
def removeDupsFromFile ( path ):
    file = open ( path , "r" )
    all_lines = file.readlines()
    file.close()
    file = open ( path , "w" )
    writen_lines = []
    for line in all_lines:
        if ( writen_lines.count( line ) == 0 ):
            file.write ( line )
            writen_lines.append ( line )
#TODO Download more RAM?
def generateCleanDotSearches ():
    """myFile = open ( params.path_to_up , "w" )
    myFile.close()
    myFile2 = open ( params.path_to_non , "w" )
    myFile2.close()
    myFile3 = open ( params.path_to_down , "w" )
    myFile3.close()
    myFile4 = open ( params.path_to_known , "w" )
    myFile4.close()
    myFile5 = open ( params.path_to_weird , "w" )
    myFile5.close()
    """
    updateAndClean ()
def main( argv ):
    try:
      opts, args = getopt.getopt( argv , "hD:CG" )
    except getopt.GetoptError:
       print ( "tools.py -hD:G" )
       exit(1)
    for flag, arg in opts:
        if flag in ( "-D" , "" ):
            removeDupsFromFile ( arg ) #TODO Should probably check this is a valid path
        if flag in ( "-C" , "" ):
            createAllFiles()
        if flag in ( "-G" , "" ):
            generateCleanDotSearches()
main ( sys.argv[1:] )
