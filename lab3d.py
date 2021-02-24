#!/usr/bin/env python3
#Author ID: sksewani
import os
import subprocess 

P = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
P_contents = P.communicate()

#result = P.read()
#P.close()

def free_space():
	output = P_contents[0].decode('utf-8').strip()
	return output
if __name__=='__main__':
	print(free_space())





