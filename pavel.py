#!/bin/python3

from subprocess import PIPE, run
from concurrent.futures import ThreadPoolExecutor
from Wappalyzer import Wappalyzer, WebPage
from termcolor import colored
import http.server
import socketserver
import socket
import subprocess
import threading
import warnings
import filecmp
import json
import requests
import readline
import os
import sys
import gen
import send
import fuzz
import req

warnings.filterwarnings("ignore", message="""Caught 'unbalanced parenthesis at position 119' compiling regex""", category=UserWarning)
readline.parse_and_bind('tab: complete')

def main():

	banner ='                             :o+-                           \n'
	banner+='                            hMhmN+                          \n'
	banner+='                           hMy  mM/                         \n'
	banner+='                          yMh    NN:                        \n'
	banner+='                         oMd`    :NN-                       \n'
	banner+='                        +Mm.      /Mm.                     \n'
	banner+='                      +sMm.        +Mm+            \n'
	banner+='           -syhddmNNmdhyo.          :shdmNNNmddhyo- \n'
	banner+='          -MMo                                 +yMd  \n'       
	banner+='          `hMd:  By EddyNefa          V  1. 0 `+NM+   \n'      
	banner+='            :dMh-                            +mMy.     \n'     
	banner+='              /mMy.                        /mMy.        \n'    
	banner+='               `+mMs.                    :dMh-           \n'   
	banner+='                 `oNN-                  oMd:              \n'  
	banner+='                  `NM-                  yMs                \n' 
	banner+='                  :MN                   :Mm                 \n'
	banner+='                  sMy                   `NM-                \n'
	banner+='                  mM:       -+ys/.       hMo                \n'
	banner+='                 -MN`   ./sdmdsymmdo-    /Mm                \n'
	banner+='                 oMh`-+hmmh+-`  `:odmmy/..MM.               \n'
	banner+='                 :mmdmds:`          ./ymmdNd`               \n'
	banner+='                  .::-                 `::-`'
	banner+='\n'
	banner+='For bugs https://github.com/EddyNefa/\n'

	name = []
	value = []
	b = 0
	if(len(sys.argv) > 1):
		if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
			help()
			exit()

		elif (sys.argv[1] == '-n' or sys.argv[1] == '--noBanner'):
			b = 1

	if(b == 0):
		print(colored(banner,'green'))


	while(True):
		try:
			cm = input('#]> ')
			cm = cm.strip()

		except EOFError:
			killDemon()
			exit()

		except KeyboardInterrupt:
			print(colored('Press Ctrl+D or exit to exit','yellow'))
			continue

		#repalcing variable with value
		if (len(name) == 1):
			if (name[0] != '' and name[0] in cm.upper()):
				if ((' '+ name[0] + ' ') in cm):
					foo = locate(words,name[0])
					words[foo] = value[0]

				else:
					foo = cm.upper().index(name[0])
					l = len(name[0])
					cm = cm[:foo] + value[0] + cm[(foo+l):]
		elif (len(name) > 1):
			for i in range(0,len(name)):
				if ((' '+ name[i] +' ') in cm):
					foo = locate(words,name[i])
					words[foo] = value[i]

				elif((name[i]) in cm.upper()):
					foo = cm.upper().index(name[i])
					l = len(name[i])
					cm = cm[:foo] + value[i] + cm[(foo+l):]

		words = cm.split(' ')

		if(words[0].upper() == 'GEN'):

			if(len(words) < 4 or len(words) > 5):
				print(colored('Wrong syntaxis','red'))
				continue

			if '-' in words[1]:
				nums = words[1].split('-')
			else:
				print(colored('Sir, you must supply the range for the numbers like 1-100','yellow'))
				continue

			if (len(nums) > 2):
				print(colored('Wrong syntaxis','red'))
				continue

			try:
				fro = int(nums[0])
				to = int(nums[1])
			except:
				print(colored('Sir, you must supply numbers as the range', 'yellow'))
				continue

			if ' AS ' not in cm.upper():
				print(colored('Sir, you must supply the AS keyword to indicate the output', 'yellow'))
				continue

			else:
				i = locate(words,'AS')
				out = words[i+1]

			if os.access(out,os.F_OK) and not os.access(out,os.W_OK):
				print(colored('sir, this file is forbiden','yellow'))
				continue

			increase = 1
			if ' INCREASE=' in cm.upper():

				foo = 'INCREASE='
				for f in words:
					if (foo in f.upper()):
						foo = f
						break

				bar = words.index(foo)
				increase = words[bar]
				increase = increase.upper()
				increase = int(increase.replace('INCREASE=',''))


			gen.gen(fro,to,out,increase)

		elif (words[0].upper() == 'SEND'):

			if(len(words) != 5):
				print(colored('Wrong syntaxis','red'))
				continue

			if (words[2].upper() != 'TO'):
				print(colored('Wrong syntaxis','red'))
				continue


			try:
				port = int(words[4])

			except:
				print(colored('Sir, the port must be a number','yellow'))
				continue

			if (port > 65535):
				print(colored('Port must be between 1 and 65535','yellow'))
				continue

			if not (os.path.isfile(words[1])):
				print(colored('File '+ words[1]+ " doesn't exist","red"))
				continue

			elif not os.access(words[1],os.R_OK):
				print(colored('Sir, this file is forbiden','yellow'))
				continue

			url = checkHTTP(words[3])
			file = open(words[1],'r')
			lines = file.readlines()
			ext = 0
			t = 90
			if (len(lines) < 1):
				print(colored('Sir, this file is empty','yellow'))
				continue

			if (len(lines) < 90):
				t = len(lines)

			executor = ThreadPoolExecutor(max_workers=t)
			requests.packages.urllib3.disable_warnings()

			proxies = {
			'http': 'http://127.0.0.1:' + str(port),
			'https': 'https://127.0.0.1:' + str(port),
			}

			try:

				s = requests.session()
				s.proxies = proxies
				r = s.get(url, proxies=proxies, verify=False)

			except:
				print(colored('Invalid  proxy','red'))
				continue

			for l in lines:
				ok = executor.submit(send.send,l,url,str(port))


		elif(words[0].upper() == 'FUZZ'):

			if (len(words) > 10):
				print(colored('Wrong syntaxis','red'))
				continue

			if (len(words) < 2):
				print(colored('Try typing something the next one sir...','yellow'))
				continue


			files = words[1].split(',')

			foo = 0
			for f in files:
				if not (os.path.isfile(f)):
					print(colored('File '+f+ " doesn't exist","red"))
					foo = 1

				elif not (os.access(f,os.R_OK)):
					print(colored('Sir, this file is forbiden','yellow'))
					foo = 1

				elif (os.path.getsize(f) == 0):
					print(colored('Sir, file '+f+' is empty ','yellow'))
					continue

			if(len(files) != len(set(files))):
				print(colored('Sir files need to be different. I recomend yo made a copy','yellow'))
				continue


			if (foo == 1):
				continue

			if (words[2].upper() != 'WITH'):
				print(colored('Wrong syntaxis','red'))
				continue

			m = 3
			if (words[3].upper() == 'PITCHFORK'):
				m = 2

			elif (words[3].upper() == 'BATTERY'):
				m = 1

			elif (words[3].upper() == 'ENCODE:'):
				m = 0

			else:
				print(colored("Sir, there is not mode named '"+ words[3] + chr(39),"yellow"))
				continue


			params = ''
			encode = False
			enc = ''
			out = ''

			if (m != 0 and ' PARAMS: ' in cm.upper()):

				i = locate(words,'PARAMS:')
				params = words[i+1]

				bar = params.split(',')
				if (len(bar) < 2):
					print(colored('Sir, you must use at least 2 params','yellow'))
					continue

				if (m == 2):
					if(len(bar) != len(files)):
						print(colored('Sir, you need to supply the same numbers of files and params with pitchfork mode', 'yellow'))
						continue
			elif(m != 0):
				print(colored("Sir, you must supply the'PARAMS:"+chr(39)+" keyword","yellow"))
				continue

			if ' ENCODE: ' in cm.upper():
				encode = True

				i = locate(words,'ENCODE:')
				enc = words[i+1]

				ceros = 0
				err = 0
				bar = 1
				algs = ['MD5','SHA1','SHA256','SHA512','B64','0']
				algoritms = enc.split(',')
				for i in algoritms:

					for a in algs:
						if (a == i.upper()):
							bar = 0
							continue

					if (i == "0"):
						ceros +=1

					if (bar == 1):
						print(colored('Invalid algoritm '+i, 'yellow'))
						err = 1

					bar = 1

				if (ceros == len(algoritms)):
					print(colored("Sir, please don't use encode if nothing will be encode","yellow"))
					continue

				if (err == 1):
					continue


			if ' AS ' in cm.upper():

				i = locate(words,'AS')
				out = words[i+1]

			else:
				print(colored('Sir, you must supply an output name','yellow'))
				continue


			foo = 0
			bar = cm.upper()
			onlyOne = [' WITH ',' AS ',' PARAMS: ',' FUZZ ',' ENCODE: ']
			for o in onlyOne:
				if (bar.count(o) > 1):
					print(colored('Sir, please type'+ o +'only once','red'))
					foo = 1
					break
			if (foo == 1):
				continue

			if os.access(out,os.F_OK) and not os.access(out,os.W_OK):
				print(colored('Sir, this file is forbiden','yellow'))
				continue


			print(colored('This could take a while...','yellow'))
			fuzz.fuzz(words[1],m,params,encode,enc,out)
			if(m == 2 and enc):
				for f in files:
					encoded = f + '.encoded'
					f1 = open(f,'r')
					l1 = f1.readlines()
					f2 = open(encoded,'r')
					l2 = f2.readlines()
					if (l1[1] == l2[1]):
						os.system('rm '+str(encoded))
					f1.close()
					f2.close()
					del l1,l2

		elif (words[0].upper() == 'LIST'):
			if (words[1].upper() == 'MODES'):
				print('\tEncode\n\tBattery\n\tPitchfork\n')

			elif(words[1].upper() == 'ALGS' or words[1].upper() == 'ALGORITMS'):
				print('\tMD5\n\tSHA1\n\tSHA256\n\tSHA512\n\tB64\n\t0 for none\n')

			elif(words[1].upper() == 'COMMANDS'):
				print('\tGen\n\tSend\n\tFuzz\n\tHead\n\tOptions\n\tWappalyze\n\tListen\n\tSet\n\tList\n\tHelp\n\tExit\n')
			else:
				print(colored("Couldn't find anything to list with "+chr(39)+words[1]+chr(39),"yellow"))



		elif(words[0].upper() == 'OPTIONS' or words[0].upper() == 'HEAD'):

			if(len(words) < 2 or len(words) > 4):
				print(colored('Wrong sintaxis','red'))
				continue

			method = ''
			if(words[0].upper() == 'OPTIONS'):
				method = 'OPTIONS'

			else:
				method = 'HEAD'

			out = ''
			bool = False
			if (' AS ' in cm.upper()):
				out = words[3]
				bool = True

			if not os.access(out,os.W_OK):
				print(colored('Sir, this file is forbiden','yellow'))
				continue

			url = checkHTTP(words[1])
			req.req(method,bool,out,url)


		elif (words[0].upper() == 'WAPPALYZE'):

			if (len(words) < 2):
				print(colored('Sir, please supply a target','red'))
				continue

			target = checkHTTP(words[1])
			verbose = False
			if (len(words) == 3):
				v =  words[2]
				if (v.upper() == '-V'):
					verbose = True

			try:
				wapp = Wappalyzer.latest()
				page = WebPage.new_from_url(str(target))

				if (verbose):
					f = wapp.analyze_with_versions_and_categories(page)

					for d, info  in f.items():
						ver = ''
						i = 1
						for v in info["versions"]:
							if (len(info["versions"]) == i):
								ver += v
							else:
								ver += v + ', '

							i +=1

						i = 1
						cat = ''
						for c in info["categories"]:
							if (len(info["categories"]) == i):
								cat += c
							else:
								cat += c + ', '

							i += 1

						print(f'{d} {ver} ({cat})')

				else:
					f = wapp.analyze(page)
					for d in f:
						print(d)

			except:
				print(colored('Whoops...Something went wrong','red'))
				continue


		elif (words[0].upper() == 'SET'):

			if (len(words) != 2):
				print(colored('Sir, you must to supply only one variable','yellow'))
				continue

			if ('=' not in words[1]):
				print(colored('Sir, give a variable like var=value please','yellow'))
				continue

			foo = words[1].split('=')
			repited = '$'+foo[0].upper()
			if (repited in name):
				bar = locate(name,repited)
				value[bar] = foo[1]
			else:
				name.append('$'+foo[0].upper())
				value.append(foo[1])

		elif (words[0].upper() == 'LISTEN'):

			port = 8000
			if (len(words) != 1):

				try:
					port = int(words[1])
				except:
					print(colored('Sir, the port must be a number','red'))
					continue

				if (port < 1 or port > 65535):
					print(colored('Sir, the port has to be between 1 and 65535','red'))
					continue

				elif(port < 1024):
					print(colored('Sir, I am not premited to use a port smaller than 1024','yellow'))
					continue

			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				t = ('127.0.0.1',port)
				isopen = s.connect_ex(t)
				if (isopen == 0):
					print(colored('Port already used','yellow'))
					continue

			except:
				print(colored('An unexpected error occurred','red'))
				continue

			path = '/home/nefa/scripts/python/fuzzerUpgrade/'
			os.system('python3.9 '+path+'listen.py '+str(port)+' &')


		elif (words[0].upper() == 'HELP'):
			help()

		elif (words[0].upper() == 'EXIT'):
			killDemon()
			exit()

		else:
			foo = cm
			foo = foo.replace(' ','')
			if (foo == ''):
				continue
			else:
				os.system(cm)


def help():
	print('You can use an option betwen:')
	print('\n\tGen: Generate numbers from a given range')
	print('\t\tExample: gen 1-10 as numbers.txt\n')
	print('\t\tYou can modify the increase between the numbers with the increase keyword')
	print('\t\tExample: gen 2-8 as numbers.txt increase=2')
	print('\n\tSend: Send a given file with discovered content in a host to your attack proxy')
	print('\t\tExample: send file.txt to https://github.com/EddyNefa 8080')
	print("\n\tFuzz: Prepare custom fuzzer files with different options (as burp intruder's modes)")
	print('\n\t\tSyntaxis: fuzz <FILE(S)> with <MODE> PARAMS: <PARAM1>,<PARAM2>,<PARAMx> ENCODE: (OPTIONAL) <ALGORITM> AS <OUTPUT>')
	print('\t\tMode:\n\t\t\tBattery: same file in all params (<PARAM1>=FILE,<PARAM2>=FILE)')
	print('\t\t\tPitchfork: each param uses a different file (<PARM1>=FILE1<PARAM2>=FILE2)')
	print('\t\t\tEncode: only encode')
	print('\n\t\tEncode: encode each file with only one algoritm (Encode: MD5,SHA1 SHA256,B64,etc)')
	print('\t\t\tNote: You can use 0 if you dont want to encode a param like: PARAMS: usr,pass ENCODE: 0,MD5\n')
	print('\tHead: makes a head request to the target you supplied')
	print('\t\tExample: head https://github.com/EddyNefa')
	print('\t\tNote: You can use the AS keyword to save it')
	print('\n\tOptions: Same as head but with an options request')
	print('\n\tWappalyze: Grab the technologies used by your target with Wappalyzer')
	print('\t\tNote: Use -v to also grab versions and categories')
	print('\t\tExample: wappalyze https://github.com/EddyNefa [-v]')
	print('\n\tListen: set a port listener in background for reciveing external connections ')
	print('\t\tExample: listen [port] (if none 8000)')
	print('\n\tSet: Set a variable to use it instead a tedious value')
	print('\t\tExample: set target=https://github.com/EddyNefa')
	print('\t\tNote: to call the variable use $ and the var name')
	print('\t\tExample: head $target')
	print('\n\tList: List available things:')
	print('\n\t\t\t-Modes\n\t\t\t-Algs/Algoritms\n\t\t\t-Commands')
	print('\n\t\tExample: List Modes')
	print('\n\tHelp: Show this menu')
	print('\n\tExit: Exit the program\n')

def locate(words,word):
	foo = word
	for f in words:
		if (f.upper() == foo):
			foo = f
			break


	bar = words.index(foo)
	return bar


def checkHTTP(url):
	if not(url.startswith('http://') or url.startswith('https://')):
		url = 'http://'+url

	return url

def killDemon():
	try:
		pid = str(subprocess.check_output(['pidof','python3.9']))
		pid = pid.replace('b','')
		pid = pid.replace('\\','')
		pid = pid.replace('n','')
		os.system('kill '+str(pid))

	except:
		pass


if __name__ == '__main__':
	main()
4
