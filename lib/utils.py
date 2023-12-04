import numpy as np

# convert binary text string into hex string
def encodeText(input):
    hexStr = bytes.hex(input)
    
    return hexStr

# convert hex string into plain text string
def decodeText(input):
    binStr = bytes.fromhex(input)
    
    plainStr = ''
    for i in range(0, len(binStr)):
        plainStr = plainStr + chr(binStr[i])
    
    return plainStr

# convert single digit hex string to one hot array representation
def hexToOneHot(hex):
    arr = np.arange(16)
    arr.fill(0)
    arr[int(hex, 16)] = 1
    
    return arr

# convert one hot array to single digit hex string
def oneHotToHex(oneHot):
    largest = 0
    
    for i in range(0, len(oneHot)):
        if(oneHot[i] > oneHot[largest]):
            largest = i
    
    hexStr = str(hex(largest))[-1]
    
    return hexStr

# pass a directory and an index, return hex character
def getFileData(dir):
    file = open(dir, 'rb')
    
    return encodeText(file.read())