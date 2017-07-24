#!/usr/bin/env python3

def IsUnique(string):
	"""Check weather string is unique or not"""
	arr =[False for x in range(128)] 		#Create a list of 128 elements and make them false ny default.
	for x in string:
		temp = ord(x)			#Convert each character with thier ASCII value.
		if arr[temp]:
			return False 		# Return false if their value is already true in list
		arr[temp] = True 		#Update list with true.
	return True

print("alul: ", IsUnique('alul'))
print("atul: ", IsUnique('atul'))
