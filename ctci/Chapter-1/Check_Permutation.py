#!/usr/bin/env python3

def CheckPermutation(string1, string2):
	"""Check permutation of two string"""
	from collections import Counter
	counter = Counter()
	if len(string1) != len(string2):
		return False
	for x in string1:
		counter[x] += 1
	for x in string2:
		counter[x] -= 1

	for x in counter:
		if counter[x]!=0:
			return False
	return True

print(CheckPermutation("atual", "ultaa"))
