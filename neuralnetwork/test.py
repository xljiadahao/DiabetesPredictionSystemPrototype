'''

Created on 2014/5/21

Algorithm: 1. Number of times pregnant   if >13 delete (Based on the Boxplot analysis, remove the outliers.)
           2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test   if ==0 replace by mean value 120.9
           3. Diastolic blood pressure (mm Hg)   if ==0 replace by mean value 69.1
           4. Triceps skin fold thickness (mm)   if ==0 replace by mean value 20.5 and if >63 (Based on the Boxplot analysis, remove the outliers.)
           5. 2-Hour serum insulin (mu U/ml)   if ==0 replace by mean value 79.8
           6. Body mass index (weight in kg/(height in m)^2)   if ==0 replace by mean value 32.0
           7. Diabetes pedigree function   no need to process
           8. Age (years)   no need to process

@author: Xu Lei, Li YiFeng

'''
def process():
    f = open("neuralnetwork/templates/doc/Diabetes.csv", "r")
    #w = open("Diabetes_Processed.csv", "w")
    line = f.readline()
    while (line != ""):
        paraArray = line.split(",")
        if int(paraArray[0]) > 13 or float(paraArray[3]) > 63: 
            print "delete: " + line
            line = f.readline()
            continue
        if float(paraArray[1]) == 0:
            paraArray[1] = str(120.9)
        if float(paraArray[2]) == 0:
            paraArray[2] = str(69.1)
        if float(paraArray[3]) == 0:
            paraArray[3] = str(20.5)
        if float(paraArray[4]) == 0:
            paraArray[4] = str(79.8)
        if float(paraArray[5]) == 0:
            paraArray[5] = str(32.0)
        newLine = paraArray[0] + "," + paraArray[1] + "," + paraArray[2] + "," + paraArray[3] + "," + paraArray[4] + "," + paraArray[5] + "," + paraArray[6] + "," + paraArray[7] + "," + paraArray[8]
        #w.writelines(newLine)
        line = f.readline()
    #w.close()
    f.close()
    print "Data Pre-processing done" 
