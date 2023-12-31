from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras import layers
from keras import losses
from keras import metrics
import numpy as np
import lib.utils as utils

class StraightforwardApproach():
    # initialize and train model
    def train(self, dirList, dataList, epochs):
        self.dirList = dirList
        self.dataList = dataList
        self.epochs = epochs
        
        # tokenize directories
        tk = Tokenizer(filters='', lower=False)
        tk.fit_on_texts(self.dirList)
        self.dirTokens = tk.word_index

        # populate training data
        self.trainX = []
        self.trainY = []
        
        for fileNum in range(0, len(self.dirList)):
            for partNum in range(0, len(self.dataList[fileNum])):
                input = [self.dirTokens[self.dirList[fileNum]], partNum]
                output = utils.hexToOneHot(self.dataList[fileNum][partNum])
                
                self.trainX.append(input)
                self.trainY.append(output)

        self.trainX = np.asarray(self.trainX).astype('float32')
        self.trainY = np.asarray(self.trainY).astype('float32')

        # prepare model
        inputSpace = len(self.dirList) + max(map(len, self.dataList)) + 1
        
        self.model = Sequential()

        self.model.add(layers.Embedding(input_dim=inputSpace, output_dim=256))
        self.model.add(layers.Dropout(0.2))
        self.model.add(layers.GlobalAveragePooling1D())
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(128, activation='relu'))
        self.model.add(layers.Dropout(0.2))
        self.model.add(layers.Dense(16, activation='sigmoid'))

        self.model.compile(optimizer='adam',
            loss=losses.CategoricalCrossentropy(),
            metrics=metrics.CategoricalAccuracy())

        self.model.fit(self.trainX, self.trainY, epochs = self.epochs, verbose=1)

    # make a prediction from string, return string
    def predictStr(self, dir, strLength):
        length = strLength * 2
        input = []
        predictedData = [None] * length
        
        # tokenize and add index indicators to input directory
        for i in range(0, length):
            dirToken = self.dirTokens[dir]
            input.append([dirToken, i])
        
        # format input and predict
        formattedInput = np.asarray(input).astype('float32')
        prediction = self.model.predict(formattedInput)
        
        # decode prediction
        predictedData = list(map(utils.oneHotToHex, prediction))
        hexData = "".join(predictedData)
        return utils.decodeText(hexData)

    # evaluate model
    def evaluate(self, batch):
        score = self.model.evaluate(self.trainX, self.trainY, verbose=0)
        grades = [score[1]]

        # batchC needs to calculate the precision of duplicate files in different directories
        if batch == 'batchC':
            duplicateCount = 10     # how many duplicate files per set of duplicates
            inputLength = 14        # length of a file in hex
            comparison = [[], []]   # array of each set of predicted duplicate files
            
            # a side is a set of duplicate files; batchC has two sets of 10 duplicate files
            for side in range(0, round(len(self.dirList) / duplicateCount)):
                # inputDir is the index in the dirList of the file to predict
                for inputDir in range(duplicateCount * side, duplicateCount + (duplicateCount * side)):
                    input = []
                    predictedData = [None] * inputLength

                    # generate input data
                    for i in range(0, inputLength):
                        dir = self.dirTokens[self.dirList[inputDir]]
                        input.append([dir, i])

                    formattedInput = np.asarray(input).astype('float32')

                    # make prediction based on input data
                    prediction = self.model.predict(formattedInput)
                    predictedData = list(map(utils.oneHotToHex, prediction))
                    
                    comparison[side].append(predictedData)

            # duplicate file precision
            dupePrecision = 0
            # comparison has two indexes each with a different set of duplicate files
            for cmp in comparison:
                side = []
                # compare duplicate files in one directory with another
                for i in range(0, round(duplicateCount / 2)):
                    # check if each character of two files equals one another
                    numEqual = 0
                    for c in range(0, inputLength):
                        if cmp[i][c] == cmp[round(i + duplicateCount / 2)][c]:
                            numEqual += 1
                            
                    percentEqual = numEqual / inputLength
                    dupePrecision += percentEqual
            
            dupePrecision = dupePrecision / duplicateCount
            grades.append(dupePrecision)
            
        return grades