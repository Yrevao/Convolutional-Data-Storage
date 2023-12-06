import sys
import numpy as np
import lib.utils as utils

# import models
from models.StraightforwardApproach import StraightforwardApproach
from models.DirectoryOptimizationApproach import DirectoryOptimizationApproach
from models.FourierFeaturesApproach import FourierFeaturesApproach

# train model, make predictions from user input
def inputLoop(modelConfig, batch):
    model = modelConfig["model"]()
    epochCount = modelConfig[batch]
    
    # generate list of file directories and file data for current batch
    dirList = []  # list of complete directories for data collection
    dirIndex = [] # shortened directories for user input
    for dir in open('batches/' + batch + '/index', 'rt'):
        lineBreakIndex = len(dir) - 1
        dirList.append('batches/' + batch + '/' + dir[:lineBreakIndex])
        dirIndex.append(dir[:lineBreakIndex])

    dataList = list(map(utils.getFileData, dirList))

    # train model
    model.train(dirIndex, dataList, epochCount)
    
    # start input loop
    while True:
        # get user input
        inputStr = input("File Dir|Length: ")
        
        # check for exit command
        if inputStr.lower() == "exit":
            return
        
        # try except to keep loop from exiting due to input processing error
        try:
            # break up user input into dir and length
            indexedInput = inputStr.split('|')
            inputDir = indexedInput[0]
            inputLength = int(indexedInput[1])
            
            # make prediction
            dataStr = model.predictStr(inputDir, inputLength)
            print(dataStr)
        except:
            # catch-all error
            print("\nFailed to process input")

# arguments: model id, batch
def processArgs():
    batches = ["batchA", "batchB", "batchC", "batchD"]
    StraightforwardApproachConfig = {
        "title": "Straightforward Approach",
        "model": StraightforwardApproach,
        "batchA": 100,
        "batchB": 50,
        "batchC": 10,
        "batchD": 5
    }
    DirectoryOptimizationApproachConfig = {
        "title": "Directory Optimization Approach",
        "model": DirectoryOptimizationApproach,
        "batchA": 100,
        "batchB": 50,
        "batchC": 100,
        "batchD": 5
    }
    FourierFeaturesApproachConfig = {
        "title": "Fourier Features Approach",
        "model": FourierFeaturesApproach,
        "batchA": 5,
        "batchB": 5,
        "batchC": 5,
        "batchD": 2
    }
    modelConfigs = [
        StraightforwardApproachConfig,
        DirectoryOptimizationApproachConfig,
        FourierFeaturesApproachConfig
    ]
    
    inputLoop(modelConfigs[int(sys.argv[1])], batches[int(sys.argv[2])])

processArgs()