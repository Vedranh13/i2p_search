import utils
import params
import requests
import bs4
from os import stat
class page(object):
    #REALLY NEED error handeling - TODO
    #TODO handle case when it is the ".main" file
    def __init__( self , eepsite , relative_path ):
        self.eepsite = eepsite #eepsite is the name of the eepsite this page is on
        self.relative_path = relative_path
        self.full_url = utils.makeURL( eepsite + relative_path )
        self.file_path = params.path_to_eepsites + self.eepsite + ".d/" + self.relative_path
        self.size = stat( self.file_path ) #TODO error handeling
    def pageFromFile( cls , path_to_file ):
        #alternate init for a page already downloaded before
        #assumes the path is gotten from the "eepsites directory"
        split_path = path_to_file.split( "/" , maxsplit = 1 )
        eepsite = split_path[0].rstrip( ".d" )
        relative_path = split_path[1]
        return cls( eepsite , relative_path )
    pageFromFile = classmethod( pageFromFile )
    def pageFromURL( cls , url ):
        path = utilis.unMakeURL( url )
        split_path = path_to_file.split( "/" , maxsplit = 1 )
        eepsite = split_path[0].rstrip( ".d" )
        relative_path = split_path[1]
        return cls( eepsite , relative_path )
    pageFromURL = classmethod( pageFromURL )
    def updatePage( self ):
        res = requests.head( self.full_url , params.proxy )
        newSize = res.headers['content-length']
        if newSize != self.size:
            res = requests.get ( self.full_url , params.proxy )
            with open( self.file_path , "w" ) as thisPage:
                thisPage.write( res.text )
    def getAllLinks( self ):
        soup = bs4.BeautifulSoup( open ( self.file_path ) )
        all_links = []
        for a_tag in soup.find_all( "a" ):
            all_links.append( a_tag.get( 'href' ) )
        return all_links
    def getAllLocalLinks( self ):
        local_links = []
        for link in self.getAllLinks():
            if link[0] == "/" or self.eepsite + ".i2p/" in link:
                # This means it is a link to another page on a domain
                local_links.append( link )
        return local_links
    def getAllExternalLinks( self ):
        local_links = self.getAllLocalLinks()
        external_links = []
        for link in self.getAllLinks():
            if link not in local_links:
                external_links.append( link )
        return external_links
