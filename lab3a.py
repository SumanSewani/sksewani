#!/usr/bin/env python3
# return_text_value() function

def return_text_value():
	name = "Terry"
	greeting = 'Good Morning ' + name
	return greeting

# return_number_value() function

def return_number_value():
	num1 = 10
	num2 = 5
	num3 = num1 + num2
	return num3




# Main program


if __name__ == '__main__':
	print ('Python Code')
	txt = return_text_value()
	print(txt)
	number = return_number_value()
	print(str(number))
