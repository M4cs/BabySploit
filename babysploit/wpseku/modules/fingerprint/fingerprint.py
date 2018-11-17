"""Support for fingerprint Wordpress."""
from lib.request import *
from modules.fingerprint.cms import *
from modules.fingerprint.headers import *
from modules.fingerprint.server import *
from modules.fingerprint.waf import *


class fingerprint(Request):
	def __init__(self,url,data,kwargs):
		self.url = url
		self.data = data
		Request.__init__(self,kwargs)

	def run(self):
		req = self.send(url=self.url)
		_cms_ = cms(req.headers,req.content)
		if 'wordpress' not in _cms_:exit(warn('That site not running WordPress'))
		_server_ = server(req.headers)
		if _server_:plus('Server: %s'%_server_)
		_waf_ = waf(req.content)
		for w in _waf_:
			if w != None: plus('WAF: %s'%w)
		headers(req.headers)
