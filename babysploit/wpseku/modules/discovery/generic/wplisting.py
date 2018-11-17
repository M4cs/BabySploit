"""Support for discovering Wordpress listings."""
from os.path import realpath
from re import I, search

from lib.readfile import *
from lib.request import *


class wplisting(Request):
	def __init__(self,url,data,kwargs):
		self.url = url 
		self.data = data
		self.kwargs = kwargs
		Request.__init__(self,kwargs)

	def run(self):
		if self.kwargs['verbose'] is True:
			info('Checking directory listing...')
		path  = realpath(__file__).split('modules')[0]
		path += "db/dirlisting.wpseku"
		for dir_ in readfile(path):
			url = Path(self.url,dir_.decode('utf-8'))
			resp = self.send(url=url,method="GET")
			if search(decode('<title>Index of /'),resp.content,I):
				plus('Dir "%s" listing enable at: %s'%(dir_.decode('utf-8'),resp.url))
