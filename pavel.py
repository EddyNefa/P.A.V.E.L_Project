#!/bin/python3

from concurrent.futures import ThreadPoolExecutor
from Wappalyzer import Wappalyzer, WebPage
from termcolor import colored
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

	banner = '           _............              ..-------.......\n'
	banner +='         :              \....-------..\                `\n'
	banner +='        :                                                :.\n'
	banner +='      .:`            ...-----....--..........--:.         .:\n'
	banner +='      /      .--...`````                          `..-/+   .-\n'
	banner +='     :` ::-.`                                          `:. `\n'
	banner +='     / .+`                       .                       /` /\n'
	banner +='    :` /`                       . -                      `/ +\n'
	banner +='    + :`                       /`   \                     + +\n'
	banner +='   -- /                  .......    `......               + +\n'
	banner +='   + --                  \                /               + /\n'
	banner +='  .: /`                   -.           .-                 /`/`\n'
	banner +='  .- /                      `/         :                  .:/`\n'
	banner +='  -- :                       :         `-                 `//\n'
	banner +='  ./ :                       :  .-``... /                 `:/\n'
	banner +='   :-+                       :-``      ``                 :+-\n'
	banner +='    `/- V 1.0                                 By EddyNefa -o`\n'
	banner +='      ``..                                        -------.`\n'
	banner +='          `````.....--------------.............```\n'
	banner +='\tFor help: https://github.com/EddyNefa/P.A.V.E.L_Project '

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
		cm = input('#]> ')

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

			if(len(words) != 6):
				print(colored('Wrong syntaxis','red'))
				continue

			if (words[2].upper() != 'TO'):
				print(colored('Wrong syntaxis','red'))
				continue

			if (words[4].upper() != 'AT'):
				print(colored('Wrong syntaxis','red'))
				continue

			try:
				port = int(words[5])

			except:
				print(colored('Sir, the port must be a number','yellow'))

			if not (os.path.isfile(words[1])):
				print(colored('File '+ words[1]+ " doesn't exist","red"))
				continue

			file = open(words[1],'r')
			lines = file.readlines()
			ext = 0
			t = 90
			if (len(lines) < 90):
				t = len(lines)

			executor = ThreadPoolExecutor(max_workers=t)
			for l in lines:
				ok = executor.submit(send.send,l,words[3],words[5])
				if (not ok):
					ext = 1
					break
			if (ext == 1):
				continue



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


			print(words[1]+' '+str(m)+' '+params+' '+str(encode)+' '+enc+' '+out)
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
				print('\tGen\n\tSend\n\tFuzz\n\tHead\n\tOptions\n\tWappalyze\n\tSet\n\tList\n\tHelp\n\tExit\n')
			else:
				print(colored("Couldn't find anything to list with "+chr(39)+words[1]+chr(39),"yellow"))



		elif(words[0].upper() == 'OPTIONS' or words[0].upper() == 'HEAD'):

			if(len(words) < 3 or len(words) > 5):
				print(colored('Wrong sintaxis','red'))
				continue

			if(words[1].upper() != 'TO'):
				print(colored('Sir, you must include the '+chr(39)+'TO'+chr(39)+' keyword','yellow'))
				continue

			method = ''
			if(words[0].upper() == 'OPTIONS'):
				method = 'OPTIONS'

			else:
				method = 'HEAD'

			out = ''
			bool = False
			if (' AS ' in cm.upper()):
				out = words[4]
				bool = True

			req.req(method,bool,out,words[2])


		elif (words[0].upper() == 'WAPPALYZE'):

			if (len(words) < 2):
				print(colored('Sir, please supply a target','red'))
				continue

			target = words[1]
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

		elif (words[0].upper() == 'HELP'):
			help()

		elif (words[0].upper() == 'EXIT'):
			exit()

		else:
			err = 1
			com = ['cat','ls','echo','rm','clear','cp','wc','searchsploit','gobuster']
			for c in com:
				if (words[0] == c):
					err = 0
					break

			if (words[0] == ''):
				continue

			if (err != 0):
				print(colored('Unknown command: '+words[0],'red'))
				continue

			else:
				err = 1
				badThings = [';','&','\'','|','`','$','@']
				for bad in badThings:
					if (bad in cm):
						err = 0
						break

				if (err != 1):
					print(colored("Sorry sir, you can't do that","red"))
					continue
				else:
					os.system('/usr/bin/'+cm)


def help():
	print('You can use an option betwen:')
	print('\n\tGen: Generate numbers from a given range')
	print('\t\tExample: gen 1-10 as numbers.txt\n')
	print('\t\tYou can modify increase between the numbers with the increase keyword')
	print('\t\tExample: gen 2-8 as numbers.txt increase=2')
	print('\n\tSend: Send a get request with a file given to a proxy like: http://foo.com/<file>')
	print('\t\tExample: send file.txt to https://github.com/EddyNefa at 8080')
	print('\t\tNote that you must enter the entire url with the http(s)\n')
	print('\tFuzz: An excelent way for making custom fuzzer files')
	print('\t\t\nSyntaxis: fuzz <FILE(S)> with <MODE> PARAMS: <PARAM1>,<PARAM2>, ENCODE: (OPTIONAL) <ALGORITM> AS <OUTPUT>')
	print('\t\tMode:\n\t\t\tBattery: same file in all params (<PARAM1>=FILE,<PARAM2>=FILE)')
	print('\t\t\tPitchfork: each param needs a different file (<PARM1>=FILE1<PARAM2>=FILE2)')
	print('\t\t\tEncode: only encode')
	print('\n\t\tEncode: encode each file with only one algoritm (Encode: MD5,SHA1 SHA256,B64,etc)')
	print('\t\t\tNote: You can use 0 if you dont want to encode a param like: PARAMS: usr,pass ENCODE: 0,MD5\n')
	print('\tHead: makes a head request to the target you supply')
	print('\t\tExample: head to https://github.com/EddyNefa')
	print('\t\tNote: You can use the AS keyword to save it\n\t\t      You must supply the target with http://[...]')
	print('\n\tOptios: Same as head but with an options request')
	print('\n\tWappalyze: Grab the technologies used by the target with Wappalyzer')
	print('\t\tNote: Use -v to also grab versions and categories')
	print('\t\tExample: wappalyze https://github.com/EddyNefa [-v]')
	print('\n\tSet: Set a variable to use instead a tedious value')
	print('\t\tNote: Only one is permited (for now)')
	print('\t\tExample: set target=https://github.com/EddyNefa')
	print('\n\tList: List available things:')
	print('\n\t\t\t-Modes\n\t\t\t-Algs/Algoritms\n\t\t\t-Commands')
	print('\n\t\tExample: List Modes')
	print('\n\tHelp: Show this help menu')
	print('\n\tExit: Exit the program\n')

def locate(words,word):
	foo = word
	for f in words:
		if (f.upper() == foo):
			foo = f
			break


	bar = words.index(foo)
	return bar


if __name__ == '__main__':
	main()
