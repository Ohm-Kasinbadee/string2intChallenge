#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python version 3.6 ++

def checkInt(input):
	list_INT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	strInt = ''

	#loop string input 
	for x in input:
		#check number string.
		for y in list_INT:
			if x == y:
				strInt += x

	return int(strInt)


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

