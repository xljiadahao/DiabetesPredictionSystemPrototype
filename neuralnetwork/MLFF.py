from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import SigmoidLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.supervised.trainers import RPropMinusTrainer
from MLFFData import *
import csv


class MLFF:
    net = buildNetwork(8, 10, 1, bias=True, hiddenclass=SigmoidLayer)
    
    def __train__(self, filePath, lr=0.1, mt=0.1):
        temp = MLFFData()
        dataset = temp.__trans__(filePath)
        trainer = BackpropTrainer(MLFF.net, dataset, learningrate = lr, momentum=mt, weightdecay=0.0, verbose=True)
        trainer.trainEpochs(epochs=80)

    def __setTest__(self, filePath):
        temp = MLFFData()
        dataset = temp.__trans__(filePath)
        output = MLFF.net.activateOnDataset(dataset)
        cls = []
        for i in range(len(output)):
            if(output[i]<0.5):
                cls.append(0)
            else: 
                cls.append(1)
        target = dataset.data.get("target")
        count = 0
        for i in range(len(cls)):
            if(cls[i]==target[i]):
                count = count + 1
        hitrate = (count*1.0)/len(target)
        print "Hit rate->", hitrate
        return hitrate
    
    def __setPredict__(self, infile, outfile):
        data = genfromtxt(infile, delimiter=',')
        predictSet = []
        for i in range(len(data)):
            result = 0
            #print(MLFF.net.activate(data[i]))
            if(MLFF.net.activate(data[i])<0.5):
                result = 0
            else: 
                result = 1
            #print(data[i],result)
            predictSet.append([data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], result])
        myfile = open(outfile, 'wb')
        a = csv.writer(myfile)
        a.writerows(predictSet)
        myfile.close()

    def __predict__(self, data):
        result = 0
        if(MLFF.net.activate(data)<0.5):
            result = 0
        else: 
            result = 1
        print 'MLFF single prediction result', result
        return result
    
        
