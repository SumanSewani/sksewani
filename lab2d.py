#!/usr/bin/env python3
import sys
arguments = sys.argv

if len(sys.argv) != 3:
	print('Usage: ' + sys.argv[0] + ' name age')
	sys.exit()

Name = sys.argv[1]
age = sys.argv[2]
print('Hi ' + Name + ', you are '+ str(age) + ' years old.')
