import sys, os, time, subprocess
os.system("TITLE Jonathan Summers' Network Scanner")
os.system("WMIC Process WHERE 'Name='python.exe'' Call setpriority 'REALTIME' > NUL")
os.system("CLS")

temp = "IF EXIST settings.ini echo good"
line = os.popen(temp).read()
ustaff = 1
ustudents = 0
umisc = 1
if (line.find("good") >= 0):
	settings = open('settings.ini','r')
	Lines = settings.readlines()
	for line in Lines:
		if(line.find("Staff") >= 0):
			if(line[-6:-1].lower() == "false"):
				ustaff = 0
		if(line.find("Students") >= 0):
			if(line[-5:-1].lower() == "true"):
				ustudents = 1
		if(line.find("Misc") >= 0):
			if(line[-6:-1].lower() == "false"):
				umisc = 0
else:
	settings = open('settings.ini','w')
	settings.write("Staff = true\nStudents = false\nMisc = true\n")
	sys.exit()
settings.close()

print("\nSearching Active Directory for all Computers...")
temp = "dsquery computer -gc -limit 0 > \"%cd%\\AD.txt\""
os.system(temp)

ad = open('AD.txt', 'r')
Lines = ad.readlines()
staff = []
students = []
misc = []
#gets the name of the computers
for line in Lines:
	temp = line[4:line.find(",")]	
	#checks if the computer name contains a ' so that I can prevent a syntax error later when running the powershell portion
	if(temp.find("'") >= 0):
		temp = temp[:temp.find("'")] + "'" + temp[temp.find("'"):]
	if(line.find("OU=Staff") >= 0 or line.find("OU=Admin") >= 0):
		if(ustaff):
			staff.append(temp)
	elif(line.find("OU=Students") >= 0):
		if(ustudents):
			students.append(temp)
	else:
		if(umisc):
			misc.append(temp)
ad.close()


print("\nScanning shares and creating shortcuts...\n")
tot = len(misc) + len(staff) + len(students)
#get each instance to have around to same amount of misc, staff, and student computers so they'll have more similar run times
compp = 450
miscp = int(compp * (len(misc) / tot) + 1)
staffp = int(compp * (len(staff) / tot) + 1)
studentsp = int(compp * (len(students) / tot) + 1)
m = 0
sta = 0
stu = 0
while((m + sta + stu) < tot):
	temp = "Powershell;$Array="
	if(umisc):
		if(m + miscp < len(misc)):
			for i in range(miscp):
				temp = temp + "'" + misc[m] + "',"
				m = m + 1
		else:
			for i in range(len(misc) - m):
				temp = temp + "'" + misc[m] + "',"
				m = m + 1
	if(ustaff):
		if(sta + staffp < len(staff)):
			for i in range(staffp):
				temp = temp + "'" + staff[sta] + "',"
				sta = sta + 1
		else:
			for i in range(len(staff) - sta):
				temp = temp + "'" + staff[sta] + "',"
				sta = sta + 1
	if(ustudents):
		if(stu + studentsp < len(students)):
			for i in range(studentsp):
				temp = temp + "'" + students[stu] + "',"
				stu = stu + 1
		else:
			for i in range(len(students) - stu):
				temp = temp + "'" + students[stu] + "',"
				stu = stu + 1
	#uses powershell through cmd to test the computers and creates shortcuts
	temp = temp[:-1] + ";$WshShell=New-Object -ComObject WScript.Shell;foreach($computer in $Array){$output=(net view $computer /all);for($i=7;$i-lt($output.Length - 2);$i++){if($output[$i].contains('$')-and!($output[$i].contains('ADMIN$')-or$output[$i].contains('print$')-or!$output[$i].contains('Disk')-or$output[$i].contains('Default share'))){$share=$output[$i].Substring(0,$output[$i].IndexOf('$'))+'$';$temp=$computer+';'+$share+'.lnk';$Shortcut=$WshShell.CreateShortcut($temp);$Shortcut.TargetPath='\\\\\\\\\\\\\\\\'+$computer+'.DOMAIN\\\\\\\\'+$share;$Shortcut.Save();$null=[System.Runtime.Interopservices.Marshal]::ReleaseComObject($Shortcut);}elseif($output[$i].contains('Disk')-and!$output[$i].contains('$')){$public=1;$temp=$computer+'.lnk';$Shortcut=$WshShell.CreateShortcut($temp);$Shortcut.TargetPath='\\\\\\\\\\\\\\\\'+$computer+'.DOMAIN\\\\\\\\';$Shortcut.Save();$null=[System.Runtime.Interopservices.Marshal]::ReleaseComObject($Shortcut);}}}$null=[System.Runtime.Interopservices.Marshal]::ReleaseComObject($WshShell) > NUL 2>NUL"
	if(8000 - len(temp) > 50):	
		m = m - miscp
		sta = sta - staffp
		stu = stu - studentsp
		#these if statements are to prevent pontential crashes if it fails of first instance
		if(m < 0): m = 0
		if(sta < 0): sta = 0
		if(stu < 0): stu = 0
		#these are to increase command length
		if ustaff and ustudents:
			staffp = staffp + 4
			studentsp = students + 4
		elif(ustaff): staffp = staffp + 8
		elif(ustudents): studentsp = studentsp + 8
	elif(8000 - len(temp) > 0):
		subprocess.Popen(temp, shell=True)
	else:
		m = m - miscp
		sta = sta - staffp
		stu = stu - studentsp
		#these if statements are to prevent pontential crashes if it fails of first instance
		if(m < 0): m = 0
		if(sta < 0): sta = 0
		if(stu < 0): stu = 0
		#these are to decrease the command length
		if(ustaff): staffp = staffp - 1
		if(ustudents): studentsp = studentsp - 1
		if(staffp < 1): sta = 1
		if(studentsp < 1): stu = 1
os.system("DEL AD.txt")