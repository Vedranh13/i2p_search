#This is an i2p crawler writen in python 3.5.2
#TODO Make A verbose mode / status updates
#Former todo: Clean this up - SOLVED BY MOVING THE EEPSITE CLASS AND URL METHODS TO "eepsite_spider.py"
from threading import active_count
from itertools import product
from string import ascii_lowercase, digits
import sys, getopt
import eepsite_spider
import params
from time import sleep
#Write date on each file
#Former todo: Clean this up with a "logDate" function -SOLVED
try:
  opts, args = getopt.getopt( sys.argv[1:] , "Ubp:" , longopts = [ "update" , "b32" , "port=", "proxy_ip="] )
except getopt.GetoptError:
   exit(1)
for flag, arg in opts:
    if flag in ( "-U" , "--update" ):
        print ( "Updating" )
        params.update = True
    if flag in ( "-b" , "--b32" ):
        print ( "Generating all .b32.i2p addresses" )
        params.b32 = True
    if flag in ( "-p" , "--port" ):
        params.port = arg
        params.proxy = {
        'http' : 'http://' + params.proxy_ip + ':' + params.port
        }
    if flag in ( "" , "--proxy_ip"):
        params.proxy_ip = arg
        params.proxy = {
        'http' : 'http://' + params.proxy_ip + ':' + params.port
        }
        #TODO various help and error messages
#logDate ( "./non_eepsites.search" , mode )
#logDate ( "./somethingWeirdHappened.search" , mode )
#logDate ( "./down_eepsites.search" , mode )
#logDate ( "./known_eepsites.search" , mode ) Now that this is just the Addressbook, write method to update it
#logDate ( "./up_eepsites.search" , mode )
#This generates possible URLs and then tests them, recording the results
sites = 0
if ( params.b32 ):
    #Generate .b32.i2p URLs and test them
    for i in product(ascii_lowercase + digits, repeat = 32):
        sites = sites + 1
        if ( sites % 5 == 0 ):
            print ( "Checked" , sites , "sites" )
            #TODO make a utils.py file
            site = eepsite_spider.eepsite ( eepsite_spider.makeURL ( "".join(i) ,  isB32 = True ) )
            if not params.update:
                site.loadOldSites()
            site.start()
#This stops it from having to many active threads and/or active connections
        while ( active_count() >= params.MAX_THREADS ):
            print ( "Sleeping" )
            sleep(1)
else:
    #Loop through adr_book and retrive data
    with open ( params.path_to_adr_book ) as adr_book:
        for adr in adr_book:
            sites = sites + 1
            print ( sites )
            site = eepsite_spider.eepsite ( eepsite_spider.makeURL ( "".join(adr) ) )
            if not params.update:
                site.loadOldSites()
            site.start()
            while ( active_count() >= params.MAX_THREADS ):
                print ( "Sleeping" )
                sleep(1)

#Former todo: Back this up to the rasp-pi - SOLVED WITH GITHUB
