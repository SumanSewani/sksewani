#!/usr/bin/env python3
# Author ID: sksewani

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
	f = open(file_name, 'r')
	read = f.read()
	f.close()
	return(read)
	
def read_file_list(file_name):
	f = open(file_name,'r')
	read_data = f.read()
	read1 = read_data.splitlines()
	f.close()
	return(read1)
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
	f=open(file_name,'a')
	write= f.write(string_of_lines)
	f.close()
	
	
def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
	f=open(file_name,'w')
	for num in list_of_lines:
		f.write(str(num) + '\n')
	f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
	f=open(file_name_read,'r')
	read_data=f.read()
	data= read_data.splitlines()
	g=open(file_name_write,'w')
	i=1
	for list in data:
		g.write(str(i) + ":" + list + '\n')
		i=i+1
	f.close()
	g.close()
	
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))




