"""Support for fingerprinting CMS."""
from re import I, search

from lib.printer import *


def wordpress(headers,content):
	_cms_ = False
	_cms_ |= search(decode('<meta name="generator" content="WordPress'),content) is not None
	_cms_ |= search(decode('<a href="http://www.wordpress.com">Powered by WordPress</a>'),content) is not None
	_cms_ |= search(decode('<link rel=\'https://api.w.org/\''),content) is not None
	_cms_ |= search(decode('\\?\/wp-content\\?\/plugins\/|\\?\/wp-admin\\?\/admin-ajax.php'),content) is not None
	if _cms_:
		return "wordpress"

def joomla(headers,content):
	_cms_  = False
	if 'Set-Cookie' in headers.keys():
		_cms_ |= search("mosvisitor=",headers["Set-Cookie"],I) is not None
	_cms_ |= search(decode("<meta name=\"Generator\" content=\"Joomla! - Copyright (C) 200[0-9] - 200[0-9] Open Source Matters. All rights reserved.\" />"),content) is not None
	_cms_ |= search(decode("<meta name=\"generator\" content=\"Joomla! (\d\.\d) - Open Source Content Management\" />"),content) is not None
	_cms_ |= search(decode("Powered by <a href=\"http://www.joomla.org\">Joomla!</a>."),content) is not None
	if _cms_ :
		return "joomla"

def drupal(headers,content):
	_cms_ = False
	if 'Set-Cookie' in headers.keys():
		_cms_ |= search("SESS[a-z0-9]{32}=[a-z0-9]{32}",headers["Set-Cookie"],I) is not None
	if 'X-Drupal-Cache' in headers.keys(): _cms_ |= True
	_cms_ |= search(decode("<script type=\"text/javascript\" src=\"[^\"]*/misc/drupal.js[^\"]*\"></script>"),content) is not None
	_cms_ |= search(decode("<[^>]+alt=\"Powered by Drupal, an open source content management system\""),content) is not None
	_cms_ |= search(decode("@import \"[^\"]*/misc/drupal.css\""),content) is not None
	_cms_ |= search(decode("jQuery.extend\(drupal\.S*"),content) is not None
	_cms_ |= search(decode("Drupal.extend\(\S*"),content) is not None
	if _cms_ :
		return "drupal"

def cms(headers,content):
	return (
			wordpress(headers,content),
			joomla(headers,content),
			drupal(headers,content)
			)
