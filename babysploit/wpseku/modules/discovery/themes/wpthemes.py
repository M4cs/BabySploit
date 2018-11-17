"""Support for discovering Wordpress themes."""
from os.path import exists, join, realpath
from json import loads
from re import I, findall, search

from lib.request import *


class wpthemes(Request):
	def __init__(self, url, data, kwargs):
		self.url = url
		self.data = data
		self.kwargs = kwargs

		root = realpath(__file__).split('modules')[0]
		files_path = join(root, 'db', 'files.json')

		if exists(files_path):
			with open(files_path, 'r') as fl:
				self.files = loads(fl.read())

		Request.__init__(self, kwargs)

	def changelog(self, theme):
		if self.kwargs['verbose'] is True:
			info('Checking themes changelog...')

		for file in self.files.get('changelogs', []):
			url = Path(self.url, '/wp-content/themes/%s/%s' % (theme, file))
			resp = self.send(url=url, method="GET")
			if resp.status_code == 200 and resp.content != ("" or None):
				if resp.url == url:
					more('Changelog: %s' % (resp.url))
					break

	def fpd(self, theme):
		if self.kwargs['verbose'] is True:
			info('Checking themes full path disclosure...')

		for file in self.files.get('fpd', []):
			url = Path(self.url, '/wp-content/themes/%s/%s' % (theme, file))
			resp = self.send(url=url, method="GET")
			if resp.status_code == 200 and resp.content != ("" or None):
				if resp.url == url:
					if search(decode('<b>Fatal error</b>:'), resp.content, I):
						path_d = findall(decode('<b>(/\S*)</b>'), resp.content)[0]
						more('FPD (Full Path Disclosure): %s' % (path_d.decode('utf-8')))
						break

	def license(self, theme):
		if self.kwargs['verbose'] is True:
			info('Checking themes license...')

		for file in self.files.get('license', []):
			url = Path(self.url, '/wp-content/themes/%s/%s' % (theme, file))
			resp = self.send(url=url, method="GET")
			if resp.status_code == 200 and resp.content != ("" or None):
				if resp.url == url:
					more('License: %s' % (resp.url))
					break

	def listing(self, theme):
		if self.kwargs['verbose'] is True:
			info('Checking themes directory listing...')

		for dir_ in self.files.get('dirs', []):
			url = Path(self.url, '/wp-content/themes/%s/%s' % (theme, dir_))
			resp = self.send(url=url, method="GET")
			if resp.status_code == 200 and resp.content != ("" or None):
				if search(decode('<title>Index of'), resp.content, I):
					more('Listing: %s' % (resp.url))

	def readme(self, theme):
		if self.kwargs['verbose'] is True:
			info('Checking themes readme...')

		for file in self.files.get('readme', []):
			url = Path(self.url, '/wp-content/themes/%s/%s' % (theme, file))
			resp = self.send(url=url, method="GET")
			if resp.status_code == 200 and resp.content != ("" or None):
				if resp.url == url:
					more('Readme: %s' % (resp.url))
					break

	def run(self):
		info('Passive enumeration themes...')
		themes = self.s_themes()
		if themes != []:
			for theme in themes:
				plus('Name: %s' % (theme.decode('utf-8')))
				self.changelog(theme)
				self.fpd(theme)
				self.license(theme)
				self.readme(theme)
				self.listing(theme)
				self.dbwpscan(theme)
		else:
			plus('Not found themes with passive enumeration')

	def s_themes(self):
		theme = []
		resp = self.send(url=self.url, method="GET")
		themes = findall(decode('/wp-content/themes/(.+?)/'), resp.content)
		for pl in themes:
			if pl not in theme:
				theme.append(pl)
		return theme

	def dbwpscan(self, theme):
		if self.kwargs['verbose'] is True:
			info('Checking theme vulnerabilities...')
		theme = theme.decode('utf-8')
		url = "https://www.wpvulndb.com/api/v2/themes/%s"%(theme)
		resp = self.send(url=url,method="GET")
		if resp.headers['Content-Type'] == 'application/json':
			json = loads(resp.content)
			if json[theme]:
				if json[theme]['vulnerabilities']:
					for x in range(len(json[theme]['vulnerabilities'])):
						more('Title: \033[1;31m%s'%(json[theme]['vulnerabilities'][x]['title']))
						if json[theme]['vulnerabilities'][x]['references'] != {}:
							if json[theme]['vulnerabilities'][x]['references']['url']:
								for y in range(len(json[theme]['vulnerabilities'][x]['references']['url'])):
									more('Reference: %s'%(json[theme]['vulnerabilities'][x]['references']['url'][y]))
						more('Fixed in: %s'%(json[theme]['vulnerabilities'][x]['fixed_in']))
				else: more('Not found vulnerabilities')
			else: more('Not found vulnerabilities')
		else: more('Not found vulnerabilities')
		normal('')
