#!/usr/bin/python

import re

"""
This code takes Markdown text and converts it to html. 

The parse_downmark takes a string of text and replace different markdown code language
with html code language. 

Type   - Markdown - html:

bold   - %        - <b>this</b>
italic - *        - <i>this</i>
"""

def parse_downmark(text):
		
	#Blockquote
	text = re.sub(r">>(.+)\n", r"<blockquote>\1</blockquote>\n", text)	

	#Bold	
	text = re.sub(r"(?:([^\\])\%(.*[^\\])\%)", r"\1<b>\2</b>", text)
	

	# Seems like the regex does not find the shortest match, fits better with 
	# replacing dot-star (.*) with a more spesific group, but looses generality
	# 
	# r"(?:([^\\])\%([\w\ \.\,\!\?\%\*]*[^\\])\%)"

	
	#Italic
	text = re.sub(r"(?:([^\\])\*(.*[^\\])\*)", r"\1<i>\2</i>", text)
	
	#Uncomment star
	text = re.sub(r"\\\*", r"*", text)

	#Uncomment percentage
	text = re.sub(r"\\\%", r"%", text)

	#Hyperlink and add http://
	text = re.sub(r"\[([\w\s,\.]+)\]\((?:http://|https://)?([a-z0-9\.\-\:\/$\|\?]+)\)", r"<a href='http://\2'>\1</a>", text)
	
	#Image link
	text = re.sub(r"(?:\<([a-z\.\-\:\/]+)\>\(w=(\d+),h=(\d+)\))", r'<img src="\1" style="width:\2px;height:\3px;">', text)	

	#Wikipedia search
	text = re.sub(r"\[wp:(.+)\]", r'<a href="www.wikipedia.org/wiki/\1">Search Wikipedia for \1</a>', text)	
	
	return text

