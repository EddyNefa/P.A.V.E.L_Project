#!/bin/python3

import sys
import os
import batteringRam
import pitchfork
import encoded

def fuzz(file,mode,param,encode,alg,out):

	while (True):
		if(mode != 0 and param == None):
			print('You must supply at least 2 params if you are not using encode mode')
			break

		if(param != None):
			params = param.replace(',',' ')

		fileList = file.replace(',',' ')
		files = fileList.split(' ')
		cFiles = len(files)

		if(mode == 0 and encode == False):
			print('You must supply an encode algoritm if you are using mode 0')
			break

		if ' ' in fileList:
			for f in files:
				if not (os.path.isfile(f)):
					print('File '+f+ " doesn't exist")
				break


	        #Encode
		if (encode):
			algs = alg.split(',')
			cAlgs = len(algs)
			if(cAlgs != cFiles):
				print('You must supply the same number of files than algoritms')
				break

			elif(',' in alg):
				bar = 0
				for a in algs:
					if (a != "0"):
						bar +=1
				if (bar == 0):
					print("If you don't want to encode don't use encode 0")
					break



			if ',' not in alg:

				if (mode == 2):
					for f in files:
						encoded.encoded(f,alg)
				else:
					encoded.encoded(fileList,alg)

				if (mode == 0):
					os.system('/usr/bin/mv '+ fileList +'.encoded '+out )
					break
			else:
				for a in range(0,cFiles):
					encoded.encoded(files[a],algs[a])


		#Mode
		if (mode < 0 or mode > 2):
			print('Invalid mode!')
			break

		if (mode == 1):

			if ' ' in fileList:
				print('Whops\t this mode can only accept one file')
				break
			else:
				batteringRam.battery(fileList,params,out,encode)

		if (mode == 2):
			if ' ' not in fileList:
				print('Whops\t this mode requires at least two files')
				break

			else:
				pitchfork.pitchfork(fileList,params,out,encode)


		break



if __name__ == '__main__':
	fuzz()
