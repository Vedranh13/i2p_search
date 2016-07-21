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
import utils
# Write date on each file
# Former todo: Clean this up with a "logDate" function -SOLVED
try:
  opts, args = getopt.getopt( sys.argv[1:] , "Up:" , longopts = [ "update" , "port=", "proxy_ip="] )
except getopt.GetoptError:
   exit(1)
for flag, arg in opts:
    if flag in ( "-U" , "--update" ):
        print ( "Updating" )
        params.update = True
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
sites = 0
    #Loop through adr_book and retrive data
with open ( params.path_to_adr_book ) as adr_book:
    for adr in adr_book:
        sites = sites + 1
        print ( sites )
        site = eepsite_spider.eepsite ( utils.makeURL ( "".join(adr) ) )
        # site = eepsite_spider.eepsite("http://zzz.i2p/")
        if not params.update:
            site.loadOldSites()
        site.start()
        while ( active_count() >= params.MAX_THREADS ):
            print ( "Sleeping" )
            sleep(1)
