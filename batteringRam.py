#!/bin/python3

import os
import codecs
import isascii
from concurrent.futures import ThreadPoolExecutor


def battery(F,param,fileName,encoded):

	payloadF = str(F)
	if (encoded):
		payloadF += '.encoded'

	file = codecs.open(payloadF, 'r', encoding='utf-8', errors='replace')
	fileLines = file.readlines()
	file.close()

	os.system('/usr/bin/echo "" > '+fileName)

	params = param.split()
	c = 1
	payload = ''
	foo = ''
	overflow = 0
	file = open(fileName, 'a')

	for line in fileLines:
		if not (isascii.isascii(line)):
			continue
		for l in params:
			payload += l +'=' + line
			payload = payload.replace('\n','')
			if (c == len(params)):

				payload +=';'
			else:
				payload +='&'
			c+=1
		c = 1
		foo += payload + '\n'
		payload = ''
		overflow +=1

		if (overflow == 1000):
			file.write(foo)
			foo = ''
			overflow = 0

	#removing the line in blank
	file.write(foo)
	file.close()
	foo = ''
	file = open(fileName,'r')
	l = file.readlines()
	file.close()
	file = open(fileName,'w')
	del l[0]
	for f in l:
		foo += f
	file.write(foo)
	file.close()

if '__main__' == __name__:
	battery()
