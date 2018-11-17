"""Support for discovering Wordpress users."""
from json import loads
from re import I, findall

from humanfriendly.tables import format_pretty_table

from lib.request import *


class wpusers(Request):
	def __init__(self, url, data, kwargs):
		self.url = url
		self.data = data
		self.kwargs = kwargs
		Request.__init__(self, kwargs)

	def run(self):
		info('Enumerating users...')
		users = []
		users = self.wpjson()
		users += self.wpjson2()
		users += self.wpfeed()
		users += self.wpauthor()
		text_table = ['ID', 'Username', 'Login']
		print(format_pretty_table(self.r_user(users), text_table))

	def r_user(self, users):
		_user_ = []
		__users__ = []
		if users != []:
			for user in users:
				if user not in __users__:
					__users__.append(user)
		else:
			plus('Not found usernames...')
		for x in range(len(__users__)):
			u, l = __users__[x]
			if isinstance(u, bytes):
				u = u.decode('utf-8')
			if isinstance(l, bytes):
				l = l.decode('utf-8')
			_user_.append((x, u, l))
		return _user_

	def wpjson(self):
		users = []
		url = Path(self.url, '/wp-json/wp/v2/users')
		resp = self.send(url=url, method="GET")
		if resp.status_code == 200:
			json = loads(resp.content, encoding="utf-8")
			for x in range(len(json)):
				users.append((json[x]['name'], json[x]['slug']))
		return users

	def wpjson2(self):
		users = []
		url = Path(self.url, '/?rest_route=/wp/v2/users')
		resp = self.send(url=url, method="GET")
		if resp.status_code == 200:
			try:
				json = loads(resp.content, encoding="utf-8")
				for x in range(len(json)):
					users.append((json[x]['name'], json[x]['slug']))
			except json.decoder.JSONDecodeError:
				pass
		return users

	def wpfeed(self):
		users = []
		url = Path(self.url, '/?feed=rss2')
		resp = self.send(url=url, method="GET")
		if resp.status_code == 200:
			_users_ = findall(
				decode('<dc:creator><!\[CDATA\[(.+?)\]\]></dc:creator>'),
				resp.content, I
			)
			for user in _users_:
				if user not in users:
					if user != []:
						if user != '':
							users.append((user.decode('utf-8'),'None'))
		return users

	def wpauthor(self):
		users = []
		for x in range(15):
			url = Path(self.url, '/?author=%s' % x)
			resp = self.send(url=url, method="GET")
			if resp.status_code == 200:
				user = findall(
					decode('author author-(.+?)|author/(.+?)/feed/'),
					resp.content, I
				)
				if user not in users:
					if user != []:
						if user != '':
							users.append(user[0])
			else: break
		return users
