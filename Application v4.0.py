import os, time, subprocess

os.system("TITLE Jonathan Summers' Network Scanner")
os.system("WMIC Process WHERE \"Name='python.exe'\" Call setpriority \"REALTIME\" > NUL")
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
else:
	settings = open('settings.ini','w')
	settings.write("Staff = true\nStudents = false\nMisc = true\n")
	ustaff = 1
	ustudents = 0
	umisc = 1
settings.close()

print("\nSearching Active Directory for all Computers...")
temp = "dsquery computer -gc -limit 0 > \"%cd%\\AD.txt\""
os.system(temp)

inputfile = open('AD.txt', 'r')
Lines = inputfile.readlines()
staff = []
students = []
misc = []
for line in Lines:
	if(line.find("OU=Staff") >= 0 or line.find("OU=Admin") >= 0):
		staff.append(line[4:line.find(",")])
	elif(line.find("OU=Students") >= 0):
		students.append(line[4:line.find(",")])
	else:
		misc.append(line[4:line.find(",")])
Computers = []
if(ustaff):
	Computers = Computers + staff
if(ustudents):
	Computers = Computers + students
if(umisc):
	Computers = Computers + misc

print("\nTesting port 445 and creating shortcuts...\n")
i = 0
while(i < len(Computers)):
	temp = "powershell;$Array="
	while(len(temp) < 7400 and i < len(Computers)):
		temp = temp + "\"\"\"" + Computers[i] + "\"\"\","
		i = i + 1
	temp = temp[:-1] + ";$WshShell=New-Object -ComObject WScript.Shell;$tcp=[System.Net.Sockets.TcpClient]::new();$tcp.Client.ReceiveTimeout=100;foreach($computername in $Array){$computer=$computername+\"\"\".DOMAIN\"\"\";try{$result=$tcp.BeginConnect($computer,445,$null,$null);$tcp.EndConnect($result)}catch{};if($tcp.connected){$tcp.Client.Disconnect($true);$temp=$computername+\"\"\".lnk\"\"\";$Shortcut=$WshShell.CreateShortcut($temp);$Shortcut.TargetPath=\"\"\"\\\\\\\\\"\"\"+$computer;$Shortcut.Save();$null=[System.Runtime.Interopservices.Marshal]::ReleaseComObject($Shortcut)}}$null=[System.Runtime.Interopservices.Marshal]::ReleaseComObject($WshShell);$tcp.Close()"
	subprocess.Popen(temp, shell=True)