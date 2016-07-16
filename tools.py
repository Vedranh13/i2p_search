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
def main( argv ):
    try:
      opts, args = getopt.getopt( argv , "hD:" )
    except getopt.GetoptError:
       print ( "tools.py -hd:D:" )
       exit(1)
    for flag, arg in opts:
        if ( flag in ( "-D" , "" ) or flag in ( "-d" , "" ) ):
            removeDupsFromFile ( arg ) #TODO Should probably check this is a valid path
main ( sys.argv[1:] )
