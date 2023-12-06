# current results:
"""
Straightforward Approach: 
     batchA: 
             Epochs: 100
             Accuracy: 97.826087474823
     batchB:
             Epochs: 50
             Accuracy: 88.98147940635681
     batchC:
             Epochs: 10
             Accuracy: 75.71428418159485
             Duplicate Precision: 62.142857142857146
     batchD:
             Epochs: 5
             Accuracy: 97.27280139923096
Directory Optimization Approach:
     batchA:
             Epochs: 100
             Accuracy: 96.7391312122345
     batchB:
             Epochs: 50
             Accuracy: 88.14814686775208
     batchC:
             Epochs: 100
             Accuracy: 96.42857313156128
             Duplicate Precision: 100.0
     batchD:
             Epochs: 5
             Accuracy: 98.62837791442871
Fourier Features Approach:
     batchA:
             Epochs: 5
             Accuracy: 98.36956262588501
     batchB:
             Epochs: 5
             Accuracy: 91.4814829826355
     batchC:
             Epochs: 5
             Accuracy: 76.42857432365417
             Duplicate Precision: 62.857142857142854
     batchD:
             Epochs: 3
             Accuracy: 92.41597652435303
"""

import lib.utils as utils

# import models
from models.StraightforwardApproach import StraightforwardApproach
from models.DirectoryOptimizationApproach import DirectoryOptimizationApproach
from models.FourierFeaturesApproach import FourierFeaturesApproach

# run model return results dict of each batch's results
def runModel(modelConfig, batches):
    scores = {}
    model = modelConfig["model"]()

    for batch in batches:
        # generate list of file directories and file data for current batch
        dirList = []  # list of complete directories for data collection
        dirIndex = [] # shortened directories for user input
        for dir in open('batches/' + batch + '/index', 'rt'):
            lineBreakIndex = len(dir) - 1
            dirList.append('batches/' + batch + '/' + dir[:lineBreakIndex])
            dirIndex.append(dir[:lineBreakIndex])

        dataList = list(map(utils.getFileData, dirList))
        
        model.train(dirIndex, dataList, modelConfig[batch])
        scores[batch] = {
            "scores": model.evaluate(batch),
            "epochs": modelConfig[batch]
        }
        
    return scores

# generate and display approach results
def generateResults():
    # batch and model configuration
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
        "batchD": 3
    }
    modelConfigs = [
        StraightforwardApproachConfig,
        DirectoryOptimizationApproachConfig,
        FourierFeaturesApproachConfig
    ]

    # get results for each approach given each batch
    results = {}
    for modelConfig in modelConfigs:
        results[modelConfig["title"]] = runModel(modelConfig, batches)
    
    # print results from each approach
    for approach in results.keys():
        batchScores = results[approach]
        
        print(approach + ": ")
        # print results from each batch of current approach
        for batch in batchScores.keys():
            print("     " + batch + ": ")
            print("             " + "Epochs: " + str(batchScores[batch]["epochs"]))
            print("             " + "Accuracy: " + str(batchScores[batch]["scores"][0] * 100))
            if(batch == "batchC"):
                print("             " + "Duplicate Precision: " + str(batchScores[batch]["scores"][1] * 100))
            
generateResults()