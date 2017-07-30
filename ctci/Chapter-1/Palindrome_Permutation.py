#!/usr/bin/env python3
def palindromePermutation(str): 	#Here we just check that string should not contain more than one odd character.
	"""Return True if string is permutation of palindrome"""
	import string
	str = str.replace(' ', '').lower()
	d = dict.fromkeys(string.ascii_lowercase, False) 	#Hash Table from a to z.
	count = 0
	for char in str:
		d[char] = not d[char] 	#Here we switch value for each character
	for char in d:
		if d[char] == True:
			count += 1
			if count > 1:
				return False
	return True

print(palindromePermutation("Tact Coa"))

