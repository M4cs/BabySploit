#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# WPSeku - Wordpress Security Scanner 
# by Momo Outaadi (m4ll0k)

from lib.colors import *


def decode(string):
	return string.encode('utf-8')

def plus(string):
	print("{}[ + ]{} {}{}{}".format(
		GREEN%1,RESET,GREEN%0,string,RESET))

def test(string):
	print("{}[ * ]{} {}{}{}".format(
		BLUE%1,RESET,WHITE%0,string,RESET))

def warn(string):
	print("{}[ ! ]{} {}{}{}".format(
		RED%1,RESET,RED%0,string,RESET))

def info(string):
	print("{}[ i ]{} {}{}{}".format(
		YELLOW%1,RESET,YELLOW%0,string,RESET))

def normal(string):
	print("{}{}{}".format(WHITE%1,string,RESET))

def more(string):
	print("  {}|{}   {}{}{}".format(
		WHITE%0,RESET,WHITE%1,string,RESET))
