print("Made my Jonathan Summers 9/11/2024\nThis program searches the network for computers that people may have access to\n")

import os

print("\nSearching Active Directory for all computers...")
query = "dsquery computer -gc -limit 0 > \"%cd%\\input.txt\""
os.system(query)

print("\nIsolating computer names and pinging them for their IP...\nThis is the long part...\n")
inputfile = open('input.txt', 'r')
Lines = inputfile.readlines()
for line in Lines:
	comma = line.find(",")
	newline = line[:comma]
	newline = newline [4:]
	newline = "ping " + newline + " -n 1 -l 1 >> \"%cd%\\list.txt\"\n"
	os.system(newline)

print("\nLogging computers that responded\n")
inputfile = open('list.txt', 'r')
f = open('output.txt', 'w')
Lines = inputfile.readlines()
for line in Lines:
	if line.find("Reply from ") >= 0:
		colon = line.find(":")
		newline = line[:colon]
		newline = "\\" + newline[11:]
		f.write("\\" + newline + "\n")