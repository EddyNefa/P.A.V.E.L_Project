#!/bin/python3

import requests
import os
from termcolor import colored

def req(method,bool,out,to):

	try:
		requests.packages.urllib3.disable_warnings()
		s = requests.session()


		if(method == 'HEAD'):
			r = s.head(to)
			dic = r.headers

			foo = ''
			print('')
			for header,content in dic.items():
				foo += header+': '+content + '\n'
				print(header+': '+content)
			print('')

		else:
			r = s.options(to)
			foo = r.headers['Allow']
			print(foo)

		if(bool):
			os.system('/usr/bin/echo  > '+out)
			with  open(out,'w') as f:
				f.write(foo)

	except:
		print(colored('Invalid host or noting interesting to show','yellow'))





if '__main__' == __name__:
	req()
