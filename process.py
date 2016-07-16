#This is a script to process the raw HTML downloaded by the crawler
from spider import makeURL
import bs4
class eepsite(object):
    def __init__ ( self , name = "" ):
        self.name = name
        self.url = makeURL ( self.name )
