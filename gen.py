#!/bin/python3

import os

def gen(fro,to,out,increase):

	os.system("/usr/bin/echo '' > "+out)
	file = open(out,'w')
	to = int(to)

	if (increase == 1):
		if (fro <= to):
			to +=1

			for n in range(fro,to):
				os.system('/usr/bin/echo '+str(n)+ ' >> '+out)

		else:
			i = fro
			while(i >= to):
				os.system('/usr/bin/echo '+str(i)+ ' >> '+out)
				i -=1

	elif (increase > 1):
		i = fro
		while(i <= to):
			os.system('/usr/bin/echo '+str(i)+ ' >> '+out)
			i += increase


	else:
		print("Increase can't be less than 1")

if __name__ == '__main__':
	gen()
