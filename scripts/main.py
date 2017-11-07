import os
import time
import re

pythonLocation = '/boot/script/'
typeNeeded = '.py'
pythonCMD = 'python3'


# Finds the file
def findfile(directory, filetype):
    for file in os.listdir(directory):
        if file.endswith(filetype):
            file = (os.path.join(directory, file))
            print(file)
            return(file)


def execute(ver, file):
    cmd = (ver, ' ', file)
    cmd = str(cmd)
    cmd = re.sub('[\(\)\{\}\'\"\,<>]', '', cmd)
    print('Running ', cmd)
    os.system(cmd)


bashFile = findfile(pythonLocation, '.sh')
execute('bash', bashFile)
time.sleep(1)
pythonFile = findfile(pythonLocation, typeNeeded)
execute(pythonCMD, pythonFile)
exit()
