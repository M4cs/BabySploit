"""Support for getting the HTTP headers."""
from lib.printer import *


def headers(headers):
	common_headers = (
		'Accept','Accept-Charset','Accept-Encoding','Accept-Language',
		'Accept-Datetime','Authorization','Connection','Cookie','Content-Length','Content-MD5','Content-Type',
		'Expect','From','Host','If-Match','If-Modified-Since','If-None-Match','If-Range','If-Unmodified-Since',
		'Max-Forwards','Origin','Pragma','Proxy-Authorization','Range','Referer','User-Agent','Upgrade','Via','Warning',
		'X-Requested-With','X-Forwarded-For','X-Forwarded-Host','X-Forwarded-Proto','Front-End-Https','X-Http-Method-Override',
		'X-ATT-DeviceId','X-Wap-Profile','Proxy-Connection','Accept-Ranges','Age','Allow','Cache-Control','Content-Encoding',
		'Content-Language','Content-Length','Content-Location','Content-MD5','Content-Disposition','Content-Range','Content-Type',
		'Date','ETag','Expires','Last-Modified','Link','Location','Proxy-Authenticate','Refresh','Retry-After','Server','Set-Cookie',
		'Status','Strict-Transport-Security','Trailer','Transfer-Encoding','Vary','WWW-Authenticate','X-Frame-Options',
		'Public-Key-Pins','X-XSS-Protection','Content-Security-Policy','X-Content-Security-Policy','X-WebKit-CSP',
		'X-Content-Type-Options','X-Powered-By','Keep-Alive','Content-language','X-UA-Compatible'
		)
	for key in headers.keys():
		if key not in common_headers:
			plus('Uncommon header "%s" found, with contents: %s'%(key,headers[key]))
