__author__ = 'AVIRAM'



symbol=["SP","NSDQ","DAX","GOLD","C.OIL"]
priceForIndex=[50,20,25,500,100]

def calculatingRisk(symbolInput,enterPri,stopPri,vol,type):#(type=1-long, type=0-short)
    if (type==1):#long
        sumPoint=enterPri-stopPri
    else:#short
        sumPoint=stopPri-enterPri

    for x in  range(len(symbol)):
        if (symbol[x]==symbolInput):
            risk=sumPoint*vol*priceForIndex[x]

    return risk

