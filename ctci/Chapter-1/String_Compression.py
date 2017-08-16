#!/usr/bin/env python3
def StringCompression(string):
	'''Count repeated no. of characters'''
	count = 0
	temp = string[0]
	new_string = ''
	for x in string+' ':
		if temp == x:
			count +=1
			continue
		new_string = new_string+temp+str(count)
		temp = x
		count = 1
	print(new_string)

StringCompression("aabcccccaaa")
