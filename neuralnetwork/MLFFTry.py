from MLFF import *
from MLFFData import *

a = MLFF()
a.__train__("Diabetes.csv",0.0005,0.1)
a.__setTest__("Diabetes_test.csv")
#a.__setPredict__("D:\ISS\software prototyping\project\data\Diabetes_predict.csv","D:\ISS\software prototyping\project\data\Diabetes_predict_result.csv")
