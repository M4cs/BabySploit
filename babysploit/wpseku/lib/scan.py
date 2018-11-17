#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# WPSeku - Wordpress Security Scanner
# by Momo Outaadi (m4ll0k) and Filippo Conti (b4dnewz)

import fnmatch
import glob
import json
import os
import re
import sys
import time

from humanfriendly.tables import format_pretty_table

from lib.printer import *
from lib.readfile import *


class Scan:
	"""
	Scanning PHP Code
	https://github.com/ethicalhack3r/wordpress_plugin_security_testing_cheat_sheet
	"""
	table = ['Line','Possibile Vuln.','String']
	vuln = {
			'csrf' : 'Cross-Site Request Forgery',
			'xss'  : 'Cross-Site Scripting',
			'sql'  : 'SQL Injection',
			'op'   : 'Open Redirect',
			'pce'  : 'PHP Code Execution',
			'com'  : 'Command Execution',
			'auth' : 'Authorization Hole',
			'php'  : 'PHP Object Injection',
			'fi'   : 'File Inclusion',
			'fd'   : 'File Download',
			}
	def check(self,filename):
		if not filename.endswith('.php'):
			exit(warn('Not found file with php extension'))
		else:
			return filename

	def recursive(self,rootdir,pattern):
		matchs = []
		for root,dirnames,filenames in os.walk(rootdir):
			for filename in fnmatch.filter(filenames,pattern):
				matchs.append(os.path.join(root,filename))
		return matchs

	def run(self,source):
		plus('Checking PHP code...')
		if os.path.isdir(source):
			plus('Scanning directory...')
			files = self.recursive(source,'*.php')
			for file in files:
				try:
					with open(file, 'tr') as check_file:  # Try open file in text mode
						check_file.read()
						info('Scanning %s file'%file)
						self.testFile(file)
				except:  # If check_file.read fails, then file is non-text (possibly binary)
					warn("Skipping %s"%file)
					pass

		else:
			plus('Scanning file...')
			file = self.check(source)
			self.testFile(file)

	def testFile(self,file):
		res = []
		code = readfile(file)
		res += self.csrf(code)
		res += self.ope(code)
		res += self.pce(code)
		res += self.com(code)
		res += self.auth(code)
		res += self.php(code)
		res += self.fin(code)
		res += self.fid(code)
		res += self.sql(code)
		res += self.xss(code)
		if res != []:
			print(format_pretty_table(res,self.table))
		else: plus('Not found vulnerabilities')

	def csrf(self,code):
		# check cross-site request forgery
		vuln = []
		blacklist = [
		             '^wp_nonce_field\(\S*\)','^wp_nonce_url\(\S*\)',
		             '^wp_verify_nonce\(\S*\)','^check_admin_referer\(\S*\)'
		             ]
		for b in blacklist:
			b = decode(b)
			for line,cd in enumerate(code):
				pattern = re.findall(b.decode("utf-8"),cd.decode("utf-8"),re.I)
				if pattern != []:
					vuln.append([line,self.vuln['csrf'],pattern[0]])
		return vuln
	
	def ope(self,code):
		# check open redirect
		vuln = []
		blacklist = [
					 '^wp_redirect\(\S*\)'
					 ]
		for b in blacklist:
			b = decode(b)
			for line,cd in enumerate(code):
				pattern = re.findall(b.decode("utf-8"),cd.decode("utf-8"),re.I)
				if pattern != []:
					vuln.append([line,self.vuln['op'],pattern[0]])
		return vuln

	def pce(self,code):
		# check php code execution
		vuln = []
		blacklist = [
					  '^eval\(\S*\)', '^assert\(\S*\)', '^preg_replace\(\S*\)'
					  ]
		for b in blacklist:
			b = decode(b)
			for line,cd in enumerate(code):
				pattern = re.findall(b.decode("utf-8"),cd.decode("utf-8"),re.I)
				if pattern != []:
					vuln.append([line,self.vuln['pce'],pattern[0]])
		return vuln
	
	def com(self,code):
		# check command execution
		vuln = []
		blacklist = [
					 '^system\(\S*\)', '^exec\(\S*\)','^passthru\(\S*\)','^shell_exec\(\S*\)'
					 ]
		for b in blacklist:
			b = decode(b)
			for line,cd in enumerate(code):
				pattern = re.findall(b.decode("utf-8"),cd.decode("utf-8"),re.I)
				if pattern != []:
					vuln.append([line,self.vuln['com'],pattern[0]])
		return vuln

	def auth(self,code):
		# check authorization hole
		vuln = []
		blacklist = [
					 '^is_admin\(\S*\)', '^is_user_admin\(\S*\)'
					 ]
		for b in blacklist:
			b = decode(b)
			for line,cd in enumerate(code):
				pattern = re.findall(b.decode("utf-8"),cd.decode("utf-8"),re.I)
				if pattern != []:
					vuln.append([line,self.vuln['auth'],pattern[0]])
		return vuln

	def php(self,code):
		# check php object injection
		vuln = []
		blacklist = [
					 '^unserialize\(\S*\)'
					 ]
		for b in blacklist:
			b = decode(b)
			for line,cd in enumerate(code):
				pattern = re.findall(b.decode("utf-8"),cd.decode("utf-8"),re.I)
				if pattern != []:
					vuln.append([line,self.vuln['php'],pattern[0]])
		return vuln

	def fin(self,code):
		# check file inclusion
		vuln = []
		blacklist = [
					 '^include\(\S*\)','^require\(\S*\)',
					 '^include_once\(\S*\)','^require_once\(\S*\)','^fread\(\S*\)'
					 ]
		for b in blacklist:
			b = decode(b)
			for line,cd in enumerate(code):
				pattern = re.findall(b.decode("utf-8"),cd.decode("utf-8"),re.I)
				if pattern != []:
					vuln.append([line,self.vuln['fi'],pattern[0]])
		return vuln

	def fid(self,code):
		# check file download
		vuln = []
		blacklist = [
					 '^file\(\S*\)', '^readfile\(\S*\)','^file_get_contents\(\S*\)'
					 ]
		for b in blacklist:
			b = decode(b)
			for line,cd in enumerate(code):
				pattern = re.findall(b.decode("utf-8"),cd.decode("utf-8"),re.I)
				if pattern != []:
					vuln.append([line,self.vuln['fd'],pattern[0]])
		return vuln
	
	def sql(self,code):
		# check sql injection
		vuln = []
		blacklist = [
					 '?\$wpdb->query\(\S*\)','^\$wpdb->get_var\(\S*\)','^\$wpdb->get_row\(\S*\)','^\$wpdb->get_col\(\S*\)',
					 '?\$wpdb->get_results\(\S*\)','^\$wpdb->replace\(\S*\)','^esc_sql\(\S*\)','^escape\(\S*\)','^esc_like\(\S*\)',
					 '^like_escape\(\S*\)'
					 ]
		for b in blacklist:
			b = decode(b)
			for line,cd in enumerate(code):
				pattern = re.findall(str(b),str(cd),re.I)
				if pattern != []:
					vuln.append([line,self.vuln['sql'],pattern[0]])
		return vuln

	def xss(self,code):
		# check cross-site scripting
		vuln = []
		blacklist = [
					 '^\$_GET\[\S*\]','^\$_POST\[\S*\]','^\$_REQUEST\[\S*\]','^\$_SERVER\[\S*\]','^\$_COOKIE\[\S*\]',
					 '^add_query_arg\(\S*\)','^remove_query_arg\(\S*\)'
					 ]
		for b in blacklist:
			b = decode(b)
			for line,cd in enumerate(code):
				pattern = re.findall(b.decode("utf-8"),cd.decode("utf-8"),re.I)
				if pattern != []:
					vuln.append([line,self.vuln['xss'],pattern[0]])
		return vuln
