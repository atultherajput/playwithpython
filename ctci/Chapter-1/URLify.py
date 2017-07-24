#!/usr/bin/env python3
def URLify(string, length=0):
	"""Convert space int %20 i string."""
	arr=list(string)
	count = 0
	new_string = ''
	for x in arr:
		if x==' ':
			arr[count] = "%20"
		count +=1

	#If we donot have length of true string. We can do following:-

	# count = len(arr) - 1
	# for x in arr[-1::-1]:
	# 	if x == "%20":
	# 		del arr[count]
	# 	if x != "%20":
	# 		break
	# 	count -= 1

	#Another way if we have length of true string. Then we can do following:-

	count = length
	for x in arr[length:len(arr)]:
		del arr[length]
		count += 1
	for x in arr:
		new_string = new_string+ ''.join(x)
	print("Orginal String: "+"'"+ string+ "'")
	print("Updated String: "+"'"+new_string+"'")

URLify("Atul Krishna Patna Bihar India     ",30)
