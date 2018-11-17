"""Support for getting the used server daemon."""
def server(headers):
	for key in headers.keys():
		if key.lower() == 'server':
			return headers[key]
	return 
