#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# WPSeku - Wordpress Security Scanner
# by Momo Outaadi (m4ll0k)

import sys
from time import strftime

from lib.printer import *


def ptime(url):
	banner()
	plus('Target: %s'%url)
	plus('Starting: %s'%(strftime('%H:%M:%S')))
	normal('')

def banner():
	print("-"*40)
	print(" _ _ _ ___ ___ ___| |_ _ _ ")
	print("| | | | . |_ -| -_| '_| | |")
	print("|_____|  _|___|___|_,_|___|")
	print("      |_|             v0.4.0\n")
	print("WPSeku - Wordpress Security Scanner")
	print("by Momo Outaadi (m4ll0k)")
	print("-"*40+"\n")
	
def usage(e=False):
	banner()
	print("Usage: %s [options]\n"%(sys.argv[0]))
	print("\t-u --url\tTarget URL (e.g: http://site.com)")
	print("\t-b --brute\tBruteforce login via xmlrpc")
	print("\t-U --user\tSet username for bruteforce, default \"admin\"")
	print("\t-s --scan\tChecking wordpress plugin code")
	print("\t-p --proxy\tUse a proxy, (host:port)")
	print("\t-c --cookie\tSet HTTP Cookie header value")
	print("\t-a --agent\tSet HTTP User-agent header value")
	print("\t-r --ragent\tUse random User-agent header value")
	print("\t-R --redirect\tSet redirect target URL False")
	print("\t-t --timeout\tSeconds to wait before timeout connection")
	print("\t-w --wordlist\tSet wordlist, default \"db/wordlist.txt\"")
	print("\t-v --verbose\tPrint more informations")
	print("\t-h --help\tShow this help and exit\n")
	print("Example:")
	print("\t %s --url http://site.com/"%(sys.argv[0]))
	print("\t %s --url http://site.com --brute --user test"%(sys.argv[0]))
	print("\t %s --url http://site.com/ --brute --user admin --wordlist wordlist.txt\n"%(sys.argv[0]))
	if e: exit()
