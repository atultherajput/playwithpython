#!/usr/bin/env python3
def OneAway(string1, string2):
	'''Check if there is any edit in strings'''
	if len(string1)==len(string2) or len(string1)==len(string2)+1 or len(string1)==len(string2)-1:
		edited = False
		i = j = 0
		while i<len(string1) and j<len(string2):
			if string1[i]!=string2[j]: 	#Compare each element of same index from both string
				if edited is True:
					return False 	#If already one element is edited return False
				if len(string1)!=len(string2):
					j+=1 		#If length of string is not same i.e. in case of insertion or deletetion
				edited = True 		#If first time edit found
			i+=1
			j+=1
		return True
	return False


print(OneAway('pale', 'ple')) 	#True
print(OneAway('pales', 'pale'))	#True
print(OneAway('pale', 'bale'))	#True
print(OneAway('pale', 'bake'))	#False
