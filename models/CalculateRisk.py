__author__ = 'AVIRAM'

#sys.path.insert(0, 'lib')  #we need this line in order to make libraries imported from lib folder work properly
import requests  #Used for http requests
import symbol

symbol2=["SP","NSDQ","DAX","GOLD","C.OIL"]
priceForIndex=[50,20,25,500,100]

def calculatingRisk(symbolInput,enterPri,stopPri,vol,type):#(type=1-long, type=0-short)
    if (type==1):#long
        sumPoint=enterPri-stopPri
    else:#short
        sumPoint=stopPri-enterPri

    priceForPoint=symbol.Symbol.getPrice(symbolInput)#get the price from date store

    '''
    for x in  range(len(symbol2)):
        if (symbol2[x]==symbolInput):
            risk=sumPoint*vol*priceForIndex[x]
    '''
    risk=sumPoint*vol*priceForPoint
    
    return risk

#print(calculatingRisk("SP",100,90,1,1))
