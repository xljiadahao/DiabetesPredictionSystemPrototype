from numpy import genfromtxt
from pybrain.datasets import SupervisedDataSet

class MLFFData:
    def __trans__(self, filePath):
        data = genfromtxt(filePath, delimiter=',')
        trainData = SupervisedDataSet(8, 1)
        for i in range(len(data)):
            trainData.addSample((data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7]), (data[i][8],))
        return trainData
