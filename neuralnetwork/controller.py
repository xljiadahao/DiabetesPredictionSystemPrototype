import os.path
import glob
import datetime
import re
import urllib
from lxml import etree
from django.template.loader import get_template
from django.template import Context
 
from django.http import HttpResponse

import test
import rawData
import time
import json

from django.views.decorators.csrf import csrf_exempt

from MLFF import *
from MLFFData import *
from SVM import *
from SVMData import *

CLICK = 0
SVM = SVM()
MLFF = MLFF()
rateSVM = -1.0
rateMLFF = -1.0

def home(request):
    dt = datetime.datetime.now()
    html = '''
<html><body><h1>From django</h1>
<p>Time now: %s.
</body></html>''' % (dt,)
    return HttpResponse(html)
 
def main(request):
    global CLICK
    context = Context()
    html = get_template('neuralNetworkHtml/prototyping_main.html').render(context)
    print "CLICK: " + str(CLICK)
    CLICK = CLICK + 1
    return HttpResponse(html)

def dataProcessing(request):
    global CLICK
    context = Context()
    html = get_template('neuralNetworkHtml/prototyping_data_processing.html').render(context)
    print "CLICK: " + str(CLICK)
    CLICK = CLICK + 1
    return HttpResponse(html)

def showRawData(request):
    context = Context({'rawData':rawData.getRawData()})
    #test.process()
    html = get_template('neuralNetworkHtml/prototyping_show_raw_data.html').render(context)
    return HttpResponse(html)

def process(request):
    global CLICK
    context = Context({'dataProcessed':rawData.process()})
    html = get_template('neuralNetworkHtml/prototyping_processed.html').render(context)
    print "CLICK: " + str(CLICK)
    CLICK = CLICK + 1
    return HttpResponse(html)

def showDataProcessed(request):
    context = Context({'rawData':rawData.getDataProcessed()})
    html = get_template('neuralNetworkHtml/prototyping_show_raw_data.html').render(context)
    return HttpResponse(html)

def trainingAndTest(request):
    global SVM
    global MLFF
    global rateSVM
    global rateMLFF
    #SVM = SVM()
    SVM.__train__("neuralnetwork/templates/doc/Diabetes_Processed.csv")
    rateSVM = SVM.__setTest__("neuralnetwork/templates/doc/Diabetes_test.csv")
    #MLFF = MLFF()
    MLFF.__train__("neuralnetwork/templates/doc/Diabetes.csv",0.0005,0.1)
    rateMLFF = MLFF.__setTest__("neuralnetwork/templates/doc/Diabetes_test.csv")
    #context = Context({'rateSVM':rateSVM, 'rateMLFF':rateMLFF})
    #time.sleep(20)
    #html = get_template('neuralNetworkHtml/prototyping_main.html').render(context)
    return HttpResponse(json.dumps("true"), mimetype="application/json")

def testResult(request):
    rate = -1.0
    model = ""
    if rateSVM > rateMLFF:
        rate = rateSVM
        model = "SVM"
    else:
        rate = rateMLFF
        model = "MLFF"
    context = Context({'rateSVM':rateSVM, 'rateMLFF':rateMLFF, 'rate':rate, 'model':model})
    html = get_template('neuralNetworkHtml/prototyping_test_result.html').render(context)
    return HttpResponse(html)

def prediction(request):
    context = Context()
    html = get_template('neuralNetworkHtml/prototyping_prediction_choice.html').render(context)
    return HttpResponse(html)

def predictionMultiple(request):
    context = Context()
    html = get_template('neuralNetworkHtml/prototyping_multiple_predict.html').render(context)
    return HttpResponse(html)

@csrf_exempt
def uploadFileAndPredict(request):
    file_obj = request.FILES.get('file',None)
    if file_obj == None:
        return HttpResponse('File not exist')
    file_name = 'neuralnetwork/templates/doc/file_upload_for_prediction.csv'
    dest = open(file_name,'wb+')
    dest.write(file_obj.read())
    dest.close()
    print "uploadFile done"
    
    file_output_name = 'neuralnetwork/templates/doc/file_upload_for_prediction_output.csv'
    rate = -1.0
    model = ""
    if rateSVM > rateMLFF:
        SVM.__setPredict__(file_name, file_output_name)
        rate = rateSVM
        model = "SVM"
    else:
        MLFF.__setPredict__(file_name, file_output_name)
        rate = rateMLFF
        model = "MLFF"
    context = Context({'rawData':rawData.getData(file_output_name),'rate':rate,'model':model})
    html = get_template('neuralNetworkHtml/prototyping_multiple_predict_result.html').render(context)
    return HttpResponse(html)

def predictionSingle(request):
    context = Context()
    html = get_template('neuralNetworkHtml/prototyping_single_predict.html').render(context)
    return HttpResponse(html)

@csrf_exempt
def predictionSingleResult(request):
    print 'POST log: ' + request.POST.get('age')
    #print 'GET: ' + request.GET.get('age')
    name = request.POST.get('name')
    if name == "":
        name = "NOT PROVIDE"
    pregnantTimes = request.POST.get('pregnantTimes')
    plasmaGlucoseConcentration = request.POST.get('plasmaGlucoseConcentration')
    diastolicBloodPressure = request.POST.get('diastolicBloodPressure')
    tricepsSkinFoldThickness = request.POST.get('tricepsSkinFoldThickness')
    serumInsulin = request.POST.get('serumInsulin')
    bodyMassIndex = request.POST.get('bodyMassIndex')
    diabetesPedigreeFunction = request.POST.get('diabetesPedigreeFunction')
    age = request.POST.get('age')
    
    rate = -1.0
    model = ""
    result = -1
    resultStr = ""
    if rateSVM > rateMLFF:
        result = SVM.__predict__([pregnantTimes,plasmaGlucoseConcentration,diastolicBloodPressure,tricepsSkinFoldThickness,serumInsulin,bodyMassIndex,diabetesPedigreeFunction,age])
        rate = rateSVM
        model = "SVM"
    else:
        result = MLFF.__predict__([pregnantTimes,plasmaGlucoseConcentration,diastolicBloodPressure,tricepsSkinFoldThickness,serumInsulin,bodyMassIndex,diabetesPedigreeFunction,age])
        rate = rateMLFF
        model = "MLFF"
    if result == 0:
        resultStr = "Negative"
    elif result == 1:
        resultStr = "Positive"
    else:
        resultStr = "Error"

    context = Context({'name':name,'rate':rate,'model':model,'resultStr':resultStr})
    html = get_template('neuralNetworkHtml/prototyping_single_predict_result.html').render(context)
    return HttpResponse(html)

