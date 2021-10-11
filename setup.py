#!/bin/python3

from subprocess import PIPE, run
import os

file = open('pavel.py','r')
fileLines = file.readlines()

location = run('/usr/bin/pwd', stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=False)
location = location.stdout.replace('\n','')
location += '/'

fileLines[519] = "\t\t\tpath = "+ chr(39) + location + chr(39) + "\n"

file = open('pavel.py', 'w')
file.writelines(fileLines)
file.close

#creating an executable file
os.system('echo > pavel')
file = open('pavel', 'w')
foo = f'#!/bin/bash\n\n{location}pavel.py $1\n\n'
file.write(foo)
file.close

#giving exec permissions
os.system('chmod +x pavel pavel.py')
os.system('mv pavel /usr/bin')
print('Everything ready!')
