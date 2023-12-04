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
        dirList = []
        dirIndex = open('batches/' + batch + '/index', 'rt')
        for dir in dirIndex:
            lineBreakIndex = len(dir) - 1
            dirList.append('batches/' + batch + '/' + dir[:lineBreakIndex])

        dataList = list(map(utils.getFileData, dirList))
        
        model.train(dirList, dataList, modelConfig[batch])
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
        "batchD": 2
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