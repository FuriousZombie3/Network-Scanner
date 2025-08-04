print("Made my Jonathan Summers 9/11/2024\nThis program searches the network for computers that people may have access to.\nEstimated 3 hours and 50 minutes for 70,000 computers based on a smaller test of 2,500.\n")

import os
import time
"""
print("\nSearching Active Directory for all computers...")
query = "dsquery computer -gc -limit 0 > \"%cd%\\AD.txt\""
os.system(query)
"""
inputfile = open('AD.txt', 'r')
Lines = inputfile.readlines()

starter1 = open('starter1.bat','w')
starter1.write("@echo off\nlist1 > \"%cd%\\input1.txt\"")
starter1.close()
list1 = open('list1.bat','w')

starter2 = open('starter2.bat','w')
starter2.write("@echo off\nlist2 > \"%cd%\\input2.txt\"")
starter2.close()
list2 = open('list2.bat','w')

starter3 = open('starter3.bat','w')
starter3.write("@echo off\nlist3 > \"%cd%\\input3.txt\"")
starter3.close()
list3 = open('list3.bat','w')

starter4 = open('starter4.bat','w')
starter4.write("@echo off\nlist4 > \"%cd%\\input4.txt\"")
starter4.close()
list4 = open('list4.bat','w')

starter5 = open('starter5.bat','w')
starter5.write("@echo off\nlist5 > \"%cd%\\input5.txt\"")
starter5.close()
list5 = open('list5.bat','w')

starter6 = open('starter6.bat','w')
starter6.write("@echo off\nlist6 > \"%cd%\\input6.txt\"")
starter6.close()
list6 = open('list6.bat','w')

starter7 = open('starter7.bat','w')
starter7.write("@echo off\nlist7 > \"%cd%\\input7.txt\"")
starter7.close()
list7 = open('list7.bat','w')

starter8 = open('starter8.bat','w')
starter8.write("@echo off\nlist8 > \"%cd%\\input8.txt\"")
starter8.close()
list8 = open('list8.bat','w')

lists = (list1,list2,list3,list4,list5,list6,list7,list8)


Lines.sort()
i = 0
for line in Lines:
	temp = "ping " + line[4:line.find(",")] + " -n 1 -l 1 -w 2\n"
	lists[i % len(lists)].write(temp)
	i = i + 1
for i in range(len(lists)):
	lists[i].write("exit")
	lists[i].close()

print("\nPinging computers for IPs...\n")
for i in range(len(lists)):
	temp = "start /MIN /REALTIME starter" + str(i + 1)
	os.system(temp)


temp = "WMIC Process WHERE \"Name='cmd.exe'\" GET Priority"
i = 1
while(i):
	line = os.popen(temp).read()
	if (line.find("13") <= 0):
		i = 0
	time.sleep(1)

log = "copy /b "
for i in range(len(lists)):
	if(i != (len(lists) - 1)): log = log + "input" + str(i + 1) + ".txt + "
	else: log = log + "input" + str(i + 1) + ".txt log.txt"
print(log)
os.system(log)
time.sleep(1)

print("\nCleaning up...\n")
for i in range(len(lists)):
	temp = "Del starter" + str(i + 1) + ".bat"
	os.system(temp)
for i in range(len(lists)):
	temp = "Del list" + str(i + 1) + ".bat"
	os.system(temp)
for i in range(len(lists)):
	temp = "Del input" + str(i + 1) + ".txt"
	os.system(temp)

print("\nLogging computers that responded\n")
inputfile = open('log.txt', 'r')
f = open('output.txt', 'w')
Lines = inputfile.readlines()
for line in Lines:
	if line.find("Reply from ") >= 0:
		newline = "\\" + line[11:line.find(":")]
		f.write("\\" + newline + "\n")
