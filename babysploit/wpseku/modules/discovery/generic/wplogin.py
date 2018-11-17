"""Support for discovering Wordpress logins."""
from lib.request import *


class wplogin(Request):
	def __init__(self,url,data,kwargs):
		self.url = url 
		self.data = data
		self.kwargs = kwargs
		Request.__init__(self,kwargs)

	def run(self):
		if self.kwargs['verbose'] is True:
			info('Checking wp-loging protection...')
		url = Path(self.url,'wp-login.php')
		resp = self.send(url=url,method="GET")
		if resp.status_code not in range(200,299):
			plus('WordPress login is protected by WAF')
