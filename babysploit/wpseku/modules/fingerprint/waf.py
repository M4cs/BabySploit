"""Support for detecting Web application firewalls."""
from re import search

from lib.printer import *


def wordfence_security(content):
	if search(decode('/wp-content/plugins/wordfence/'),content):
		return 'Wordfence Security'

def bulletproof_security(content):
	if search(decode('/wp-content/plugins/bulletproof-security/'),content):
		return 'BulletProof Security'

def better_wp_security(content):
	if search(decode('/wp-content/plugins/better-wp-security/'),content):
		return 'Better WP Security'

def sucuri_security(content):
	if search(decode('/wp-content/plugins/sucuri-scanner/'),content):
		return 'Sucuri Security'

def acunetix_wp_security_scan(content):
	if search(decode('/wp-content/plugins/wp-security-scan/'),content):
		return 'Acunetix WP Security'

def  all_in_one_wp_security_and_firewall(content):
	if search(decode('/wp-content/plugins/all-in-one-wp-security-and-firewall/'),content):
		return 'All In One WP Security & Firewall'

def _6_scan_security(content):
	if search(decode('/wp-content/plugins/6scan-protection/'),content):
		return '6Scan Security'

def waf(content):
	return (
		wordfence_security(content),
		bulletproof_security(content),
		better_wp_security(content),
		sucuri_security(content),
		acunetix_wp_security_scan(content),
		all_in_one_wp_security_and_firewall(content),
		_6_scan_security(content)
		)
