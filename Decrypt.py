import os
import zipfile
import ftplib

filename = 'LogPython'
filenamedwg = 'LogPythondwg'
session = ftplib.FTP('YOURFTP', 'YOURLOGIN', 'YOURPASS')
files = session.nlst()
file_pwd = []
file_path = []
file_name = []
file_extract_patch = []
count = 0

local_filename = os.path.join(r"c:\\Temp", filenamedwg)
lf = open(local_filename, "wb")
session.retrbinary("RETR " + filename, lf.write)
lf.close()
lf = open("c:\\Temp\\" + filenamedwg)
for line in lf:
    instrTest = 0
    if (count%3 == 0):
        file_path.append(line)
        while(line.find('\\',instrTest ) != -1):
            instrTest += 1
        print instrTest
        print line[instrTest:]
        file_extract_patch.append(line[:instrTest])
        file_name.append(line[instrTest:])
    if (count % 3 == 2):
        file_pwd.append(line)
    count += 1

lf.close()
session.quit()

os.remove("c:\\Temp\\" + filenamedwg)
count = 0

for path in file_path:
    print path
    print file_name[count]
    print file_pwd[count]
    zf = zipfile.ZipFile(path.rstrip() + '.zip', mode='r')
    try:
        zf.setpassword(file_pwd[count].rstrip())
        zf.extract(file_name[count].rstrip(), file_extract_patch[count].rstrip(), )
    finally:
        zf.close()

    count += 1

print ("End")
