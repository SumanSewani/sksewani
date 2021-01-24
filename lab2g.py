#!/usr/bin/env python3
#Author: Suman Sewani
#Author ID: sksewani
#Date Created: 2021/01/24
import sys
if len(sys.argv) == 1:
	timer = 3
else:
	timer = int(sys.argv[1])

while timer != 0:
	print(timer)
	timer = timer - 1

print('blast off!')


