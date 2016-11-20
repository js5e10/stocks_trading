import urllib2
import time
import datetime
import re
import numpy as np
import matplotlib.dates as mdates
stockToPull = 'AAPL','GOOG', 'MSFT', 'CMG', 'AMZN', 'EBAY', 'TSLA'

def pullData(stock):
    try:
        print 'Currently pulling', stock
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
        urlToVisit='http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
        saveFileline=stock+'.txt'


        try:
            readExistingData = open(saveFileline,'r').read()
            splitExisting=readExistingData.split('\n')
            mostRecentLine=splitExisting[-2]
            lastUnix=mostRecentLine.split(',')[0]

        except Exception,e:
            print str(e)
            lastUnix = 0
        saveFile= open(saveFileline, 'a')
        sourceCode=urllib2.urlopen(urlToVisit).read()
        splitSource=sourceCode.split('\n')


        for eachLine in splitSource:
            if 'values' not in eachLine:
               splitLine = eachLine.split(',')
               if len(splitLine)==6:

                 if int(splitLine[0])>int(lastUnix):
                        date=str(datetime.datetime.fromtimestamp(int(splitLine[0])).strftime('%Y-%m-%d'))
                        #print str(date)
                        re.sub(splitLine[0],date,eachLine)
                        #eachLine.split(',')[0]=datetime.datetime.fromtimestamp(int(splitLine[0])).strftime('%Y-%m-%d %H: %M: %S')
                       # print eachLine.split(',')[0] + '=================='

                        line = datetime.datetime.fromtimestamp(int(splitLine[0])).strftime('%Y%m%d')
                        line=int(line)
                        print line
                        lineTowrite = eachLine + '\n'
                        saveFile.write(lineTowrite)

        saveFile.close()
        print 'Pulled', stock
        print 'sleeping'
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
        time.sleep(300)





    except Exception,e:
        print 'main loop', str(e)

while True:
  for eachStock in stockToPull:
      pullData(eachStock)

pullData(stockToPull)