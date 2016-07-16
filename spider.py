#This is an i2p crawler writen in python 3.5.2
#TODO Make A verbose mode / status updates
#Former todo: Clean this up - SOLVED BY MOVING THE EEPSITE CLASS AND URL METHODS TO "eepsite_spider.py"
import eepsite_spider
from threading import active_count
from itertools import product
from string import ascii_lowercase, digits
from time import gmtime, strftime, sleep
import sys, getopt
#Write date on each file
#TODO Clean this up with a "logDate" function
MAX_THREADS = 50
sites = 0
update = False
try:
  opts, args = getopt.getopt( sys.argv[1:] , "U" , longopts = [ "update" ] )
except getopt.GetoptError:
   exit(1)
for flag, arg in opts:
    if ( flag in ( "-U" , "--update" ) ):
        update = True
nonExistant = open ( "./non_eepsites.search" , "a" )
somethingWeirdHappened = open ( "./somethingWeirdHappened.search" , "a" )
knownSites = open ( "./known_eepsites.search" , "a" )
nonExistant.write ( "# " + strftime ( "%c" ) + "\n" )
somethingWeirdHappened.write ( "# " + strftime ( "%c" ) + "\n" )
knownSites.write ( "# " + strftime ( "%c" ) + "\n" )
nonExistant.close()
somethingWeirdHappened.close()
knownSites.close()
#This generates possible URLs and then tests them, recording the results
for i in product(" " + ascii_lowercase + digits, repeat = 15):
    print ( sites )
    sites = sites + 1
    site = eepsite_spider.eepsite ( eepsite_spider.makeURL ( "".join(i) ) )
    if not update:
        site.loadOldSites()
    site.start()
#This stops it from having to many active threads and/or active connections
    if ( active_count() >= MAX_THREADS ):
        print ( "Sleeping" )
        sleep(1) #TODO Figure out why there are duplicates on all lists, possibly something to do with sleeping?
#Former todo: Back this up to the rasp-pi - SOLVED WITH GITHUB
