import urllib2
import time
import datetime



stockToPull = 'AAPL','GOOG', 'MSFT', 'CMG', 'AMZN', 'EBAY', 'TSLA'

def pullData(stock):
    try:
        file=stock+'.txt'

        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
        sourceCode=urllib2.urlopen(urlToVisit).read()
        print 'success get data'
        splitSource=sourceCode.split('\n')

        for eachLine in splitSource:
            print eachLine
            splitline=eachLine.split(',')
            if len(splitline)==6:
                if 'values' not in eachLine:
                    saveFile=open(file, 'a')
                    lineToWrite = eachLine+'\n'
                    saveFile.write(lineToWrite)
        print 'Pulled', stock
        print 'sleeping'
        time.sleep(5)

    except Exception,e:
        print 'main loop', str(e)


for eachStock in stockToPull:
    pullData(eachStock)

pullData(stockToPull)