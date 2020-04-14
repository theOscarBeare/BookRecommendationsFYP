"""
	This file has some useful functions
	Some inspiration is from web
	Thank you stackoverflow and python documentation
"""

import re

def norm_rsplit(text, n):
	'''split string into list'''
	return text.lower().rsplit(' ', n)[-n:]


def re_split(text):
	'''return all non-overlapping matches of pattern in string'''
	return re.findall('[a-z]+', text.lower())


def chunks(l, n):
	'''Function to split a list into evenly sized chunks'''
	for i in range(0, len(l) - n + 1):
		yield l[i:i+n]