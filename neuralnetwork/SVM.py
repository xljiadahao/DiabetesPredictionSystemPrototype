from sklearn import svm
from SVMData import *
import csv

class SVM:
    net = svm.SVC(kernel='linear')
    
    def __train__(self, filePath):
        temp = SVMData(filePath)
        x = temp.__data__()
        #print x
        y = temp.__target__()
        SVM.net.fit(x, y)
    
    def __setTest__(self,filePath):
        #print SVM.net
        temp = SVMData(filePath)
        a = temp.__data__()
        b = temp.__target__()
               
        cls = []
        for i in range(len(a)):
            print SVM.net.predict(a[i])
            if(SVM.net.predict(a[i])<0.5):
                cls.append(0)
            else: 
                cls.append(1)
                
        count = 0
        for i in range(len(cls)):
            if(cls[i]==b[i]):
                count = count + 1
        hitrate = (count*1.0)/len(b)
        print "Hit rate->", hitrate
        return hitrate
        
    def __setPredict__(self, infile, outfile):
        data = genfromtxt(infile, delimiter=',')
        #print SVM.net
        predictSet = []
        for i in range(len(data)):
            result = SVM.net.predict(data[i])
            #print(SVM.net.predict(data[i]))
            #print data[i]
            #if(SVM.net.predict(data[i])<0.5):
            #    result = 0
            #else: 
                #result = 1
            #print(data[i],result)
            resultStr = ""
            if result == 0:
                resultStr = "Negative"
            else:
                resultStr = "Positive"
            predictSet.append([round(data[i][0]), round(data[i][1]), round(data[i][2]), round(data[i][3],1), round(data[i][4],1), round(data[i][5],1), round(data[i][6],3), round(data[i][7]), resultStr])
        myfile = open(outfile, 'wb')
        a = csv.writer(myfile)
        a.writerows(predictSet)
        myfile.close()
        
    def __predict__(self,data):
        return SVM.net.predict(data)
