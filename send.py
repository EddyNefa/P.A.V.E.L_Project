#!/bin/python3

import requests

def send(param,url,port):

	requests.packages.urllib3.disable_warnings()

	proxies = {
 	'http': 'http://127.0.0.1:' + port,
	'https': 'https://127.0.0.1:' + port,
}
	try:
		s = requests.session()
		s.proxies = proxies
		r = s.get(url+'/'+param, proxies=proxies, verify=False)
		return True

	except:
		print('Invalid host or proxy')
		return False

