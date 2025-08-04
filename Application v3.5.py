import os, time, subprocess

os.system("TITLE Jonathan Summers' Network Scanner")
os.system("WMIC Process WHERE \"Name='python.exe'\" Call setpriority \"REALTIME\" > NUL")
os.system("%windir%\system32\rundll32.exe advapi32.dll,ProcessIdleTasks")
os.system("CLS")

temp = "IF EXIST settings.ini echo good"
line = os.popen(temp).read()
if (line.find("good") >= 0):
	settings = open('settings.ini','r')
	Lines = settings.readlines()
	for line in Lines:
		if(line.find("Staff") >= 0):
			if(line[-5:-1].lower() == "true"):
				ustaff = 1
			else:
				ustaff = 0
		if(line.find("Students") >= 0):
			if(line[-5:-1].lower() == "true"):
				ustudents = 1
			else:
				ustudents = 0
		if(line.find("Misc") >= 0):
			if(line[-5:-1].lower() == "true"):
				umisc = 1
			else:
				umisc = 0
		if(line.find("10.*.*.*") >= 0):
			if(line[-5:-1].lower() == "true"):
				u10 = 1
			else:
				u10 = 0
else:
	settings = open('settings.ini','w')
	settings.write("Staff = true\nStudents = false\nMisc = true\n10.*.*.* = true\n")
	ustaff = 1
	ustudents = 0
	umisc = 1
	u10 = 1
settings.close()

print("\nSearching Active Directory for all computers...")
temp = "dsquery computer -gc -limit 0 > \"%cd%\\AD.txt\""
os.system(temp)


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

starter9 = open('starter9.bat','w')
starter9.write("@echo off\nlist9 > \"%cd%\\input9.txt\"")
starter9.close()
list9 = open('list9.bat','w')

starter10 = open('starter10.bat','w')
starter10.write("@echo off\nlist10 > \"%cd%\\input10.txt\"")
starter10.close()
list10 = open('list10.bat','w')

starter11 = open('starter11.bat','w')
starter11.write("@echo off\nlist11 > \"%cd%\\input11.txt\"")
starter11.close()
list11 = open('list11.bat','w')

starter12 = open('starter12.bat','w')
starter12.write("@echo off\nlist12 > \"%cd%\\input12.txt\"")
starter12.close()
list12 = open('list12.bat','w')

starter13 = open('starter13.bat','w')
starter13.write("@echo off\nlist13 > \"%cd%\\input13.txt\"")
starter13.close()
list13 = open('list13.bat','w')

starter14 = open('starter14.bat','w')
starter14.write("@echo off\nlist14 > \"%cd%\\input14.txt\"")
starter14.close()
list14 = open('list14.bat','w')

starter15 = open('starter15.bat','w')
starter15.write("@echo off\nlist15 > \"%cd%\\input15.txt\"")
starter15.close()
list15 = open('list15.bat','w')

lists = (list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15)

inputfile = open('AD.txt', 'r')
Lines = inputfile.readlines()
Lines.sort()
staff = []
students = []
misc = []
for line in Lines:
	if(line.find("OU=Staff") >= 0 or line.find("OU=Administration") >= 0):
		staff.append(line)
	elif(line.find("OU=Students") >= 0):
		students.append(line)
	else:
		misc.append(line)
Computers = []
if(ustaff):
	Computers = Computers + staff
if(ustudents):
	Computers = Computers + students
if(umisc):
	Computers = Computers + misc

i = 0
for line in Computers:
	temp = "ping " + line[4:line.find(",")] + " -n 1 -l 1 -w 2\n"
	lists[i % len(lists)].write(temp)
	i = i + 1
for i in range(len(lists)):
	lists[i].write("exit")
	lists[i].close()

print("\nPinging computers for IPs...\n")
for i in range(len(lists) - 1):
	temp = "starter" + str(i + 2)
	subprocess.run(temp)
os.system("starter1")

temp = "WMIC Process WHERE \"Name='cmd.exe'\" GET Priority"
i = 1
while(i):
	process = subprocess.run(temp, capture_output=True, text=True)
	output = process.stdout
	if (output.find("13") <= 0):
		i = 0
	time.sleep(5)

temp = "copy /b "
for i in range(len(lists)):
	if(i != (len(lists) - 1)): temp = temp + "input" + str(i + 1) + ".txt + "
	else: temp = temp + "input" + str(i + 1) + ".txt log.txt"
os.system(temp)

os.system("CLS")
time.sleep(5)

print("\nCleaning up...\n")
for i in range(len(lists)):
	temp = "DEL starter" + str(i + 1) + ".bat"
	subprocess.run(temp)
for i in range(len(lists)):
	temp = "DEL list" + str(i + 1) + ".bat"
	subprocess.run(temp)
for i in range(len(lists)):
	temp = "DEL input" + str(i + 1) + ".txt"
	subprocess.run(temp)

print("\nSorting through log..\n")
list = []
list2 = []
inputfile = open('log.txt', 'r')
Lines = inputfile.readlines()
for i in range(len(Lines)):
	line = Lines[i]
	if line.find("Reply from ") >= 0:
		pline = Lines[i - 1]
		if line.find("165.111") >= 0:
			list.append(pline[8:pline.find(".")] + "\\" + line[11:line.find(":")] + "\n")
		else:
			list2.append(pline[8:pline.find(".")] + "\\" + line[11:line.find(":")] + "\n")
		i = i + 1
list.sort()
if(u10):
	list2.sort()
	for line in list2:
		list.append(line)

list = list[:1500]

temp = open('Killer.py','w')
temp.write("import os, time, subprocess\ntemp = \"TASKLIST /FI \\\"IMAGENAME eq powershell.exe\\\" /FO LIST\"\nlist2 = []\nwhile(1):\n\tlist = []\n\tif(len(list2) > 0):\n\t\ttemp2 = \"taskkill /f\"\n\t\tfor line in list2:\n\t\t\ttemp2 = temp2 + \" /pid \" + line\n\t\ttemp2 = temp2 + \"> NUL 2> NUL\"\n\t\tos.system(temp2)\n\tprocess = subprocess.run(temp, capture_output=True, text=True)\n\toutput = process.stdout\n\ti = 1\n\twhile(i):\n\t\tif output.find(\"PID:\") >= 0:\n\t\t\toutput = output[output.find(\"PID:\") + 14:]\n\t\t\tlist.append(output[:output.find(\"\\n\")])\n\t\telse:\n\t\t\ti = 0\n\ttime.sleep(.75)\n\tlist2 = []\n\tif(len(list) > 0):\n\t\ttemp2 = \"taskkill /f\"\n\t\tfor line in list:\n\t\t\ttemp2 = temp2 + \" /pid \" + line\n\t\ttemp2 = temp2 + \"> NUL 2> NUL\"\n\t\tos.system(temp2)\n\tprocess = subprocess.run(temp, capture_output=True, text=True)\n\toutput = process.stdout\n\ti = 1\n\twhile(i):\n\t\tif output.find(\"PID:\") >= 0:\n\t\t\toutput = output[output.find(\"PID:\") + 14:]\n\t\t\tlist2.append(output[:output.find(\"\\n\")])\n\t\telse:\n\t\t\ti = 0\n\ttime.sleep(.75)")
temp.close()
time.sleep(.25)
os.system("TASKKILL /FI \"USERNAME eq %userdomain%\\%username%\" /FI \"IMAGENAME ne svchost.exe\" /FI \"IMAGENAME ne explorer.exe\" /FI \"IMAGENAME ne cmd.exe\" /FI \"IMAGENAME ne tasklist.exe\" /FI \"IMAGENAME ne python.exe\" > NUL 2> NUL")
subprocess.Popen("python Killer.py", shell=True)
log = open('log','w')
print("\nTesting connections by creating shortcuts. This is the long part...\nEstimated " + str(int((len(list) / 2.935420)/3600)) + " hours and " + str(round((len(list) / 3.995433)/60,1)) + " minutes...")
for i in range(len(list)):
	temp = "powershell; $WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut(\"\"\"%cd%\\" + list[i][:list[i].find("\\")] + ".lnk\"\"\"); $Shortcut.TargetPath = \"\"\"\\" + list[i][list[i].find("\\"):-1] + "\"\"\"; $Shortcut.Save()"
	subprocess.Popen(temp, shell=True)
	time.sleep(.35)
log.write(".")
time.sleep(5)
os.system("TASKKILL /F cmd.exe")
killer.kill()
time.sleep(5)
os.system("DEL Killer.py; START /MIN /REALTIME cmd.exe /C TASKKILL /F /IM python.exe /IM powershell.exe")