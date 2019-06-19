#!/usr/bin/python

"""
This function takes a string as input, search through the content for email like strings. 
It returns these emails in form of a list.
"""

import re

def find_emails(text):


	regex = r"\b[A-Za-z0-9.#$%&~'*+-/=?|{}]+@[A-Za-z0-9.#$%&~'*+-/=?|{}_]+\.[A-Za-z]{1,4}\b"	
	match = [re.findall(regex, email) for email in text]
			
	return match

"""
find_urls() takes a string as input and searches trough the content for urls.

They can look like:

<a href="PROTOCOL://www.HOST.DOMAIN/PATH"></a>
<a href="PROTOCOL://HOST.DOMAIN/PATH"> </a>
<a href=’PROTOCOL://www.HOST.DOMAIN/PATH’></a>
<a href=’PROTOCOL://HOST.DOMAIN/PATH’></a>
"""

def find_urls(text):

	#PROTOCOL    = http https
	#HOST/DOMAIN = .-~
	#PATH        = /.-~

	regex = r"""<a href=("|')((?:http|https)://[a-zA-Z0-9.-~]+[a-zA-Z0-9/.-~]+)\1>"""

	# returns every match as a tuple with ( ("|') , url ), maybe not ideal
	matches = [re.findall(regex, section) for section in text]

	# post processing of the matches, removing the first uninteresting group of every match
	for i in range(len(matches)):
		if len(matches[i]) == 0:
			continue
		else:
			for j in range(len(matches[i])):
				matches[i][j] = matches[i][j][1]

	return matches

