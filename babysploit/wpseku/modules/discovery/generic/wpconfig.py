"""Support for discovering Wordpress configuration."""
from os.path import realpath

from lib.readfile import *
from lib.request import *


class wpconfig(Request):
	def __init__(self,url,data,kwargs):
		self.url = url 
		self.data = data
		self.kwargs = kwargs
		Request.__init__(self,kwargs)

	def run(self):
		if self.kwargs['verbose'] is True:
			info('Checking wp-config backup file...')
		url = Path(self.url,'wp-config.php')
		resp = self.send(url=url,method="GET")
		if resp.status_code == 200 and resp.content != ("" or None):
			if resp.url == url:
				plus('wp-config.php available at: %s'%resp.url)
		self.wpconfig_backup()

	def wpconfig_backup(self):
		path  = realpath(__file__).split('modules')[0]
		path += "db/backupfile.wpseku"
		for ext in readfile(path):
			url = Path(self.url,"wp-config.php"+ext.decode('utf-8'))
			resp = self.send(url=url,method="GET")
			if resp.status_code == 200 and resp.content != ("" or None):
				if resp.url == url:
					plus('wp-config.php backup was found at: %s'%(resp.url))
