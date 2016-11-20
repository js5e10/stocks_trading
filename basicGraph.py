import time
import datetime
import numpy as np
import numpy as np
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick
import matplotlib
matplotlib.rcParams.update({'font.size' : 9})
import re



eachStock=  'AAPL','CMG' , 'GOOG'

def graphData(stock):
    try:
       stockFile=stock+'.txt'
#       date_bk=np.loadtxt(stockFile, dtype='string',delimiter=',', unpack=True)

       # for i in date_bk:
       #    print i

       #converters = {0: mdates.strpdate2num('%Y%m%d%H%M%S')}

       date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',' , unpack=True,
                                                         converters={ 0: mdates.strpdate2num('%Y%m%d')})


       #x=np.array(date)
      # x=np.asarray(x,dtype='datetime64[s]')
      # print x.tolist()
      # date_convert=x.tolist()
      # print date_convert[0]

       #time.sleep(30)
      # date_bk=[]
       #for i in date:
        #   number=datetime.datetime.fromtimestamp(i).strftime('%Y%m%d%H%M%S')
     #      convert=mdates.date2num(number)
     #      print convert
       #    date_bk.append(int(number))

      # print type(date_bk[0])
      #intDate=[int(eachDate) for eachDate in floatdate]
      # date=[datetime.datetime.fromtimestamp(eachDate).strftime('%Y%m%d%H%M%S') for eachDate in intDate]
       #print type(date[0])

      # dateConvert=[]
      # for d in  date:
      #     dateConvert.append(float(d))

      # print type(dateConvert[0])
       x=0
       y=len(date)


       candleAr = []
       #date_c=[]
       while x<y:
         # date_convert=int(date[x])
          appendLine= date[x], openp[x], closep[x], highp[x], lowp[x], volume[x]
          print (appendLine)
          candleAr.append(appendLine)

          #date_c.append(date_convert)
          x+=1

       # print x

       fig= plt.figure()
       ax1=plt.subplot2grid((5,4), (0,0), rowspan=3, colspan=4)
       ax1.plot(date, openp)
       ax1.plot(date, highp)
       ax1.plot(date, lowp)
       ax1.plot(date, closep)


       ax3=plt.subplot2grid((5,4), (3,0), rowspan=1,colspan=4)
       #candlestick(ax3, candleAr, width=1, colorup='g', colordown='r')
       #time.sleep(20)



       plt.ylabel('Stock Price')


       ax2 = plt.subplot2grid((5,4), (4,0), sharex=ax1, rowspan=1, colspan=4)
       ax2.bar(date, volume, width=0.1)
       ax2.axes.yaxis.set_ticklabels([])
       plt.ylabel('Volume')
       ax2.grid(True)


       ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
       ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))




       for label in ax1.xaxis.get_ticklabels():
           label.set_rotation(45)

      # for label in ax2.xaxis.get_ticklabels():
      #      label.set_rotation(45)


       plt.subplots_adjust(left=.09 , bottom=0.18, right=0.94, top=0.95, wspace=0.2, hspace=0)


       plt.xlabel('Date')
       plt.ylabel('stock Price')
       plt.suptitle(stock+' Stock Price')
       plt.setp(ax1.get_xticklabels(), visible=False)
       plt.show()
       fig.savefig('example.png')
    except Exception,e:
        print 'failed main loop', str(e)

for stock in eachStock:
    graphData(stock)
    time.sleep(555)
