"""The WPSeku main part."""
import getopt

from lib.scan import *
from lib.usage import *
from modules.bruteforce.wpxmlrpc import *
from modules.discovery.generic.generic import *
from modules.discovery.plugins.wpplugins import *
from modules.discovery.themes.wpthemes import *
from modules.discovery.users.wpusers import *
from modules.fingerprint.fingerprint import *


class wpseku(object):
	"""WPSeku main object"""
	kwargs = {
			 'agent':ragent(),'ragent':False,'redirect':True,
			  'cookie':None,'proxy':None,'timeout':None,'verbose':False,'headers':{}
			  }
	def main(self):
		# default value
		self.brute = False
		self.user = "admin"
		self.wordlist = "db/wordlist.txt"
		self.url = None
		self.user = None
		self.scan = None
		#
		if len(sys.argv) < 2:
			usage(True)
		try:
			opts,args = getopt.getopt(sys.argv[1:],'u:U:s:p:c:a:t:w:Rrhvb:',['url=',
				'brute','user=','scan=','proxy=','cookie=','agent=','wordlist=','timeout=',
				'redirect','ragent','help','verbose'])
		except getopt.GetoptError as e:
			usage(True)
		for opt,arg in opts:
			if opt in ('-u','--url'):self.url=urlCheck(arg)
			if opt in ('-b','--brute'):self.brute=True
			if opt in ('-U','--user'):self.user=arg
			if opt in ('-s','--scan'):self.scan=arg
			if opt in ('-p','--proxy'):self.kwargs['proxy']=arg
			if opt in ('-c','--cookie'):self.kwargs['cookie']=arg
			if opt in ('-a','--agent'):self.kwargs['agent']=arg
			if opt in ('-t','--timeout'):self.kwargs['timeout']=arg
			if opt in ('-R','--redirect'):self.kwargs['redirect']=True
			if opt in ('-r','--ragent'):self.kwargs['ragent']=True
			if opt in ('-v','--verbose'):self.kwargs['verbose']=True
			if opt in ('-h','--help'):usage(True)
		# start
		try:
			if self.scan != None:
				banner()
				Scan().run(self.scan)
			elif self.brute is True:
				ptime(self.url)
				XMLRPCBrute(self.url,None,self.user,
					self.wordlist,self.kwargs).run()
			elif self.url:
				ptime(self.url)
				fingerprint(self.url,None,self.kwargs).run()
				generic(self.url,None,self.kwargs)
				wpthemes(self.url,None,self.kwargs).run()
				wpplugins(self.url,None,self.kwargs).run()
				wpusers(self.url,None,self.kwargs).run()
		except UnboundLocalError as e:
			pass

if __name__ == "__main__":
	try:
		wpseku().main()
	except KeyboardInterrupt:
		exit(warn('CTRL+C...'))
