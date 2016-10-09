from numpy import genfromtxt

class SVMData:
    file = None
    def __init__(self, filePath):
        SVMData.file = filePath
    
    def __data__(self):
        data = genfromtxt(SVMData.file, delimiter=',')
        x = []
        for i in range(len(data)):
            x.append([data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7]])
        return x
            
    def __target__(self):
        data = genfromtxt(SVMData.file, delimiter=',')
        y = []
        for i in range(len(data)):
            y.append(data[i][8])
        return y
        