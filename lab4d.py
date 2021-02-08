#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s1):
    # Place code here - refer to function specifics in section below
	return(s1[:5])
def last_seven(s2):
    # Place code here - refer to function specifics in section below
	return(s2[-7:])
def middle_number(n1):
    # Place code here - refer to function specifics in section below
	return(str(n1)[1]+str(n1)[2])
def first_three_last_three(s3, s4):
    # Place code here - refer to function specifics in section below
	return(s3[0:3] + s4[-3:])

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
