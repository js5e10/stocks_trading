import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick
import matplotlib
matplotlib.rcParams.update({'font.size': 9})
eachStock= 'AAPL', 'AMZN'

def movingaverage(values, window):
    weights = np.repeat(1.0, window)/window
    smas=np.convolve(values, weights, 'valid')
    return smas


def graphData(stock, MA1, MA2):
    try:
        stockFile=stock+'.txt'

        date, closep, highp, lowp, openp, volume=np.loadtxt(stockFile, delimiter=',', unpack=True,
                                                             converters={ 0: mdates.strpdate2num('%Y%m%d')})

        x=0
        y=len(date)
        candleAr=[]

        while x<y:
            appendLine=date[x],openp[x],closep[x],highp[x], lowp[x], volume[x]
            candleAr.append(appendLine)
            x+=1

        Av1 = movingaverage(closep, MA1)
        Av2 = movingaverage(closep, MA2)
        sp = len(date[MA2-1:])
        label1=str(MA1) + 'SMA'
        label2=str(MA2) + 'SMA'

        fig=plt.figure(facecolor='#07000d')
        ax1=plt.subplot2grid((5,4),(0,0), rowspan=4, colspan=4, axisbg='#07000d')
        candlestick(ax1, candleAr[-sp:], width=1, colorup='#9eff15', colordown='#ff1717')
        ax1.plot(date[-sp:], Av1[-sp:], '#5998ff', label=label1, linewidth=1.5)
        ax1.plot(date[-sp:], Av1[-sp:], '#e1edf9', label=label2, linewidth=1.5)
        ax1.plot(date[-sp:], Av2[-sp:])

        #ax1.plot(date, openp)
        #ax1.plot(date, highp)
        #ax1.plot(date, lowp)
        #ax1.plot(date, closep)
        plt.ylabel('Stock price', color='w')
        plt.legend(loc=3, prop={'size' : 7}, fancybox=True)
        ax1.grid(True, color='w')

        volumeMin = 0
        ax2=plt.subplot2grid((5,4),(4,0), sharex=ax1, rowspan=1, colspan=4,axisbg='#07000d')
        ax2.plot(date, volume, '#00ffe8', linewidth=.8)
        ax2.fill_between(date, volumeMin, volume, facecolor='#00ffe8', alpha=.5)

        #ax2.bar(date, volume)
        ax2.axes.yaxis.set_ticklabels([])
        plt.ylabel('Volume', color='w')
        ax2.grid(True)






        #put xaxis 1 after last graph
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax1.yaxis.label.set_color('w')
        ax1.spines['bottom'].set_color("#5998ff")
        ax1.spines['top'].set_color("#5998ff")
        ax1.spines['right'].set_color("#5998ff")
        ax1.spines['left'].set_color("#5998ff")
        ax1.tick_params(axis='y', colors='w')



        ax2.spines['bottom'].set_color("#5998ff")
        ax2.spines['top'].set_color("#5998ff")
        ax2.spines['right'].set_color("#5998ff")
        ax2.spines['left'].set_color("#5998ff")
        ax2.tick_params(axis='x', colors='w')
        ax2.tick_params(axis='y', colors='w')
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)
        plt.subplots_adjust(left = .09, bottom = 0.18, right = 0.94, top = 0.95, wspace = 0.2, hspace = 0)



        plt.xlabel('Date')

        plt.suptitle(stock+' Stock price', color='w')
        plt.setp(ax1.get_xticklabels(), visible=False)
        plt.show()
        fig.savefig('example.png', facecolor=fig.get_facecolor())


    except Exception,e:
        print 'failed main loop' + str(e)


for stock in eachStock:
   graphData(stock, 12, 24)
   time.sleep(30)