# batch b = fifty files of less than a kilobyte in size split into five directories

import os

startingDir = ""
dirCount = 5
dirStep = 10
dirIndex = []

for dirNum in range(0, dirCount):
    startingNumber = dirNum*dirStep
    fileDir = startingDir + str(dirStep * dirNum)
    
    os.mkdir(fileDir)
    
    for fileNum in range(startingNumber, startingNumber + dirStep):
        fileName = "/" + str(fileNum) + ".txt"
        fileData = ''.join(format(ord(i), 'b') for i in str(fileNum))
        
        file = open(fileDir + fileName, 'wt')
        file.write(str(fileData))
        file.close()
        
        dirIndex.append(fileDir + fileName)

index = open('index', 'wt')
for dir in dirIndex:
    index.write(dir + '\n')
    
index.close()