#MIDN Colin Duffy, m221812

import os, hashlib
from datetime import datetime

walk = os.walk("/")
noGoDir = ["dev", "proc", "run", "sys", "tmp", "var/lib", "var/run"]
fileLog = open("fileLog.txt", 'w')


for root, dirs, files in walk:
    for nope in noGoDir:
        if nope in dirs:
            dirs.remove(nope)

    if files != []:
        for file in files:
            filePath = os.path.join(root,file)
            #hash file
            try:
                with open(filePath, 'rb') as hashFile:
                    readFile = hashFile.read()
                    shaHash = hashlib.sha256(readFile)
                    finalHash = shaHash.hexdigest()
                    time = datetime.now()
                    #capture date/time
                    current = str(datetime.now())
                    #write to log file with fullpath, hash, and date/time to file for future events
                    information = "----------\n" + 'File: '+ filePath + "\n" + 'Hash: ' +finalHash+ '\n' + 'Date/Time: ' + current + '\n'
                    fileLog.write(information)
            except FileNotFoundError:
                continue

fileLog.close()
