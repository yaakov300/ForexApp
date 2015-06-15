__author__ = 'AVIRAM'


import sys
import json
import logging
from pprint import pprint


#sys.path.insert(0, 'lib')  #we need this line in order to make libraries imported from lib folder work properly
import requests  #Used for http requests

def getCurrencyResults(FROM,TO):
    URL="https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22"+ FROM +TO+\
        "%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
    request = requests.get(URL)
    data = request.json()#["query"]["results"]["rate"]["Rate"]
    return data, request.status_code

def getCommoditiesResults(COM):
    URL="https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22"+COM+"%22)" \
        "&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
    request = requests.get(URL)
    data = request.json()#["query"]["results"]["quote"]["Ask"]
    return data, request.status_code

def multiRequests():
    with open('../web/static/json/symbols.json') as data_file:
        data = json.load(data_file)

    stComm=""
    stCurr=""
    stDax=""
    line=0;
    for i in data["symbol"]:
        if (line<5):
            stComm=stComm+''+i["symbolName"]+','
        else:
            stCurr=stCurr+''+i["symbolName"]+','
        line=line+1
    stComm=stComm[:-1]
    stCurr=stCurr[:-1]

    URLComm="https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22"+stComm+"%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="

    URLCurr="https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22"+stCurr+\
        "%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="

    requestComm = requests.get(URLComm)
    dataComm = requestComm.json()#["query"]["results"]["quote"]["Ask"]

    requestCurr = requests.get(URLCurr)
    dataCurr = requestCurr.json()#["query"]["results"]["rate"]["Rate"]

    #print all Commodities
    for i in range(dataComm["query"]["count"]):
        if (i!=2):
            print (dataComm["query"]["results"]["quote"][i]["Ask"])
        else:#for Dax
            print (dataComm["query"]["results"]["quote"][i]["LastTradePriceOnly"])

    #print all Currency
    for i in range(dataCurr["query"]["count"]):
        print (dataCurr["query"]["results"]["rate"][i]["Rate"])



'''
FROM="usd"
TO="cad"
response, status_code = getCurrencyResults(FROM,TO)
print("The Rate of "+FROM+"/"+TO+ ": "+response["query"]["results"]["rate"]["Rate"])
'''

'''
COM="GCK15.CMX"
response, status_code = getCommoditiesResults(COM)
print ("The Rate of "+COM+": "+response["query"]["results"]["quote"]["Ask"])
'''
#multiRequests()

