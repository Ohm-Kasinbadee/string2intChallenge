#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python version 3.6 ++

def checkInt(input):
	list_strInt = []
	dict_str2int = {'0': 0,
					'1': 1,
					'2': 2,
					'3': 3,
					'4': 4,
					'5': 5,
					'6': 6,
					'7': 7,
					'8': 8,
					'9': 9
					}
	for x in range(0,len(input)):
		for k, v in dict_str2int.items():
			#check digit str to int from list
			if input[x] == k:
				list_strInt.append(v)

	#set output type int 
	output = 0

	for x in range(0,len(list_strInt)):
		#set cost start -> 10
		set_int = 10

		#calculate loop position number
		for y in range(0,len(list_strInt)-x-2):
			set_int *= 10

		#check last position number calculator set cost 10 to 1
		if x+1 == len(list_strInt):
			set_int = 1

		output += list_strInt[x] * set_int
		
	return output


#Start Program
str_input_A = "abc573"
str_input_B = "a5b7c3"

output_A = checkInt(str_input_A)
output_B = checkInt(str_input_B)

print(f'INTPUT : {str_input_A} -->> OUTPUT : {output_A} -->> TYPE : {type(output_A)}' )
print(f'INTPUT : {str_input_B} -->> OUTPUT : {output_B} -->> TYPE : {type(output_B)}' )


#by: kasinbadee wongthongluea 
#mail: kasinbadee.w@gmail.com
#INTPUT : abc573 -->> OUTPUT : 573 -->> TYPE : <class 'int'>
#INTPUT : a5b7c3 -->> OUTPUT : 573 -->> TYPE : <class 'int'>

