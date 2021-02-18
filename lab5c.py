#!/usr/bin/env python3
# Author ID: sksewani

def add(number1, number2):
# Add two numbers together, return the result, if error return string['error: could not add numbers']
	number1=str(number1)
	number2=str(number2)
	if number1.isnumeric() and number2.isnumeric():
		number1=int(number1)
		number2=int(number2)
	else:
		if number1.isnumeric():
			number1=int(number1)
		if number2.isnumeric():
			number2=int(number2)
	try:
		return(number1 + number2)
	except TypeError:
		return('error: could not add numbers')

def read_file(filename):
    # Read a file, return a list of all lines, if error return string string['error: could not read file'
	try:
		f=open(filename,'r')
		output = f.readlines()
		f.close()
		return(output)
	except (FileNotFoundError, PermissionError, IsADirectoryError):
		return('error: could not read file')

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
