import os
inputfile = open('input.txt', 'r')
f = open('output.txt', 'w')
Lines = inputfile.readlines()
for line in Lines:
	comma = line.find(",")
	newline = line[:comma]
	newline = "\\" + newline[4:]
	if os.path.exists("\\" + newline):
		f.write(newline + "\n")
	f.write("Not \\" + newline + "\n")
f.close()