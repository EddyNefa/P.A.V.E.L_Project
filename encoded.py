#!/bin/python3

import hashlib
import base64
import os
import codecs
import isascii

def encoded(out,alg):

	os.system('/usr/bin/echo ""   > '+ out +'.encoded ')
	foo = ''
	bar = ''
	overflow = 0
	fi = codecs.open(out, 'r', encoding='utf-8', errors='ignore')
	f = fi.readlines()
	fi.close()
	out += '.encoded'
	with open(out,'a') as file:
		file.seek(0)
		for line in f:
			if not (isascii.isascii(line)):
				continue

			try:
				if (alg.upper() == "MD5"):
					foo += md5(line) + '\n'

				elif (alg.upper() == "SHA1"):
					foo += sha1(line) + '\n'

				elif (alg.upper() == "SHA256"):
					foo += sha256(line) + '\n'


				elif (alg.upper() == "SHA512"):
					foo += sha512(line) + '\n'

				elif (alg.upper() == "B64"):
					bar = b64(line) + '\n'
					bar = bar.replace('=','')
					foo += bar

				elif (alg == '0'):
					foo += line
				else:
					print('Invalid algoritm!')
					exit()

				overflow += 1

				if (overflow == 1000):
					file.write(foo)
					foo = ''
					overflow = 0
			except:
				foo += line

		file.write(foo)

	f = open(out,'r')
	lin = f.readlines()
	del lin[0]
	f.close()
	foo = ''
	f = open(out,'w')
	for l in lin:
		foo += l
	f.write(foo)
	f.close()

def md5(line, encoding='utf-8'):
	hash = hashlib.md5()
	hash.update(line.encode(encoding))
	return hash.hexdigest()

def sha1(line, encoding='utf-8'):
	hash = hashlib.sha1()
	hash.update(line.encode(encoding))
	return hash.hexdigest()

def sha256(line, encoding='utf-8'):
	hash = hashlib.sha256()
	hash.update(line.encode(encoding))
	return hash.hexdigest()

def sha512(line, encoding='utf-8'):
	hash = hashlib.sha512()
	hash.update(line.encode(encoding))
	return hash.hexdigest()

def b64(line, encoding='ascii'):
	planeStr = line
	planeBytes = planeStr.encode(encoding)
	b64Bytes = base64.b64encode(planeBytes)
	b64Str = b64Bytes.decode("ascii")
	return b64Str



if __name__ == '__main__':
	encoded()


