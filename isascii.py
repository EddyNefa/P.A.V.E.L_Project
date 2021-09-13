#!/bin/python3

def isascii(s):
	return len(s) == len(s.encode())

if "__main__" == __name__:
	isascii()
