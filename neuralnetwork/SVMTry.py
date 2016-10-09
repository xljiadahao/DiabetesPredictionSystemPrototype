from SVM import *
from SVMData import *

a = SVM()
a.__train__("Diabetes.csv")
a.__setTest__("Diabetes_test.csv")
#a.__setPredict__("D:\ISS\software prototyping\project\data\Diabetes_predict.csv","D:\ISS\software prototyping\project\data\Diabetes_predict_result.csv")
a.__predict__([1,93,70, 31,0,30.4, 0.315,23])
