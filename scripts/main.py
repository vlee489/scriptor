import os
import time

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


def executepython(ver, file):
    cmd = (ver, ' ', file)
    print('Running python script ', file)
    os.system(cmd)


bashFile = findfile(pythonLocation, '.sh')
os.system('bash ', bashFile)
time.sleep(1)
pythonFile = findfile(pythonLocation, typeNeeded)
executepython(pythonCMD, pythonFile)
exit()
