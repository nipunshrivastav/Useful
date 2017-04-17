"""
author::nipun.shrivastav
input::
output::
description::Function to read a file delimited by any delimiter into array
"""
import re

def readContents(filename):
	with open(filename) as f:
	    content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	delimiters = " ", ",", ":", "{", "}"
	
	regexPattern = '|'.join(map(re.escape, delimiters))
	content = [re.split(regexPattern, x.strip()) for x in content]
	content = [filter(None, x) for x in content]
	f.close()
	return content


if __name__ == "__main__":
	theos = readContents("/home/trader/Desktop/repos/trade_list_merge/theos.txt")
	trades = readContents("/home/trader/Desktop/repos/trade_list_merge/trades.csv")
