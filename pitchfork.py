#!/bin/python3

import os
import codecs
import isascii

def pitchfork(F,param,fileName,encoded):

	payloadF = str(F).split(' ')
	if (encoded):
		for i in range(0,len(payloadF)):
			payloadF[i] += '.encoded'

	files = []
	l = 10000000000
	for f in payloadF:
		file = codecs.open(f,'r',encoding='utf-8',errors='ignore')
		fileLines = file.readlines()
		files.append(fileLines)
		if (len(fileLines) < l):
			l = len(fileLines)


	os.system('/usr/bin/echo "" > '+fileName)

	params = param.split()
	if (len(params) != len(files)):
		print('You need to supply the same number of files and params')
		exit()

	foo = ''
	bar = ''
	le = len(payloadF)
	out = open(fileName,'a')
	overflow = 0

	for i in range(0,l):
		for j in range(0,le):
			bar = gen(payloadF[j],params[j],i)
			if (j == le-1):
				bar += ';'

			else:
				bar += '&'

			if not(isascii.isascii(bar)):
				continue

			foo += bar.replace('\n','')

		foo += '\n'
		overflow +=1

		if (overflow == 1000):
			out.write(foo)
			foo = ''
			overflow = 0

	out.write(foo)
	out.close()


	f = open(fileName,'r')
	lin = f.readlines()
	f.close()
	f = open(fileName,'w')
	del lin[0]
	foo = ''
	for la in lin:
		foo += la
	f.write(foo)
	f.close

def gen(file,param,index):
	try:
		f = open(file,'r')
		lines = f.readlines()
		f.close()

		return param +'='+ lines[index]

	except:
		return None


if __name__ == '__main__':
	pitchfork()
