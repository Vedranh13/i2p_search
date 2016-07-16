import sys, getopt
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
    myFile = open ( "./up_eepsites.search" , "w" )
    myFile.close()
    myFile2 = open ( "./down_eepsites.search" , "w" )
    myFile2.close()
    myFile3 = open ( "./somethingWeirdHappened.search" , "w" )
    myFile3.close()
    myFile4 = open ( "./known_eepsites.search" , "w" )
    myFile4.close()
    myFile5 = open ( "./non_eepsites.search" , "w" )
    myFile5.close()
def main( argv ):
    try:
      opts, args = getopt.getopt( argv , "hD:G" )
    except getopt.GetoptError:
       print ( "tools.py -hD:G" )
       exit(1)
    for flag, arg in opts:
        if flag in ( "-D" , "" ):
            removeDupsFromFile ( arg ) #TODO Should probably check this is a valid path
        if flag in ( "-G" , "" ):
            generateCleanDotSearches()
main ( sys.argv[1:] )
