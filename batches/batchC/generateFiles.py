# batch c = five duplicate files of less than a kilobyte in size in each of five sub directories and five separate duplicate files in five more sub directories

import os

startingDir = ""
dirCount = 4
dirStep = 10
dirIndex = []

for dirNum in range(0, dirCount):
    startingNumber = dirNum*dirStep
    fileDir = startingDir + str(dirStep * dirNum)
    
    os.mkdir(fileDir)
    
    if(dirNum < dirCount / 2):
        for fileNum in range(0, 5):
            fileName = "/" + "ABC" + "-" + str(fileNum) + ".txt"
            fileData = "ABC-DEF"
            
            file = open(fileDir + fileName, 'wt')
            file.write(str(fileData))
            file.close()
            
            dirIndex.append(fileDir + fileName)
    else:
        for fileNum in range(0, 5):
            fileName = "/" + "123" + "-" + str(fileNum) + ".txt"
            fileData = "123-456"
            
            file = open(fileDir + fileName, 'wt')
            file.write(str(fileData))
            file.close()
            
            dirIndex.append(fileDir + fileName)

index = open('index', 'wt')
for dir in dirIndex:
    index.write(dir + '\n')

index.close()