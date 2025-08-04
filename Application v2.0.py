print("Made my Jonathan Summers 9/11/2024\nThis program searches the network for computers that people may have access to.\nEstimated 3 hours and 50 minutes for 70,000 computers based on a smaller test of 2,500.\n")

import os
import time

print("\nSearching Active Directory for all computers...")
query = "dsquery computer -gc -limit 0 > \"%cd%\\input.txt\""
os.system(query)

inputfile = open('input.txt', 'r')
Lines = inputfile.readlines()

starter1 = open('starter1.bat','w')
starter1.write("list1 > \"%cd%\\input1.txt\"")
starter1.close()
list1 = open('list1.bat','w')

starter2 = open('starter2.bat','w')
starter2.write("list2 > \"%cd%\\input2.txt\"")
starter2.close()
list2 = open('list2.bat','w')

starter3 = open('starter3.bat','w')
starter3.write("list3 > \"%cd%\\input3.txt\"")
starter3.close()
list3 = open('list3.bat','w')

starter4 = open('starter4.bat','w')
starter4.write("list4 > \"%cd%\\input4.txt\"")
starter4.close()
list4 = open('list4.bat','w')

starter5 = open('starter5.bat','w')
starter5.write("list5 > \"%cd%\\input5.txt\"")
starter5.close()
list5 = open('list5.bat','w')
"""
starter6 = open('starter6.bat','w')
starter6.write("list6 > \"%cd%\\input6.txt\"")
starter6.close()
list6 = open('list6.bat','w')

starter7 = open('starter7.bat','w')
starter7.write("list7 > \"%cd%\\input7.txt\"")
starter7.close()
list7 = open('list7.bat','w')

starter8 = open('starter8.bat','w')
starter8.write("list8 > \"%cd%\\input8.txt\"")
starter8.close()
list8 = open('list8.bat','w')

starter9 = open('starter9.bat','w')
starter9.write("list9 > \"%cd%\\input9.txt\"")
starter9.close()
list9 = open('list9.bat','w')

starter10 = open('starter10.bat','w')
starter10.write("list10 > \"%cd%\\input10.txt\"")
starter10.close()
list10 = open('list10.bat','w')

starter11 = open('starter11.bat','w')
starter11.write("list11 > \"%cd%\\input11.txt\"")
starter11.close()
list11 = open('list11.bat','w')

starter12 = open('starter12.bat','w')
starter12.write("list12 > \"%cd%\\input12.txt\"")
starter12.close()
list12 = open('list12.bat','w')

starter13 = open('starter13.bat','w')
starter13.write("list13 > \"%cd%\\input13.txt\"")
starter13.close()
list13 = open('list13.bat','w')

starter14 = open('starter14.bat','w')
starter14.write("list14 > \"%cd%\\input14.txt\"")
starter14.close()
list14 = open('list14.bat','w')

starter15 = open('starter15.bat','w')
starter15.write("list15 > \"%cd%\\input15.txt\"")
starter15.close()
list15 = open('list15.bat','w')

starter16 = open('starter16.bat','w')
starter16.write("list16 > \"%cd%\\input16.txt\"")
starter16.close()
list16 = open('list16.bat','w')

starter17 = open('starter17.bat','w')
starter17.write("list17 > \"%cd%\\input17.txt\"")
starter17.close()
list17 = open('list17.bat','w')

starter18 = open('starter18.bat','w')
starter18.write("list18 > \"%cd%\\input18.txt\"")
starter18.close()
list18 = open('list18.bat','w')

starter19 = open('starter19.bat','w')
starter19.write("list19 > \"%cd%\\input19.txt\"")
starter19.close()
list19 = open('list19.bat','w')

starter20 = open('starter20.bat','w')
starter20.write("list20 > \"%cd%\\input20.txt\"")
starter20.close()
list20 = open('list20.bat','w')
"""
lists = (list1,list2,list3,list4,list5)#,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16,list17,list18,list19,list20)

current = 0
i = 0
for line in Lines:
	if (i == int((len(Lines)/len(lists) + 1))):
		lists[current].write("\n")
		lists[current].close()
		current = current + 1
		i = 0
	i = i + 1
	newline = "ping " + line[4:line.find(",")] + " -n 1 -l 1 -w 2\n"
	lists[current].write(newline)
lists[current].write("\n")
lists[current].close()

for i in range(len(lists)):
	temp = "start starter" + str(i + 1)
	os.system(temp)
"""
temp = "copy \b list1.txt + list2.txt complete_list.txt"
os.system(temp)

print("\nLogging computers that responded\n")
inputfile = open('complete_list.txt', 'r')
f = open('output.txt', 'w')
Lines = inputfile.readlines()
for line in Lines:
	if line.find("Reply from ") >= 0:
		newline = "\\" + line[11:line.find(":")]
		f.write("\\" + newline + "\n")
"""