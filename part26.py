import urllib2
import time
import datetime
import numpy
__all__=['numpy']
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick
import matplotlib
matplotlib.rcParams.update({'font.size': 9})
eachStock= 'AAPL', 'AMZN'
#relative stengh indicator

def rsiFunc(prices, n=14):
    deltas=np.diff(prices)
    seed=deltas[:n+1]
    down=-seed[seed<0].sum()/n
    up=seed[seed>0].sum()/n
    rs=up/down
    rsi=np.zeros_like(prices)
    rsi[:n]=100.-100./(1.+rs)
    for i in range(n, len(prices)):
        delta=deltas[i-1]
        if delta > 0:
            upval=delta
            downval=0.
        else:
            upval=0.
            downval=-delta

        up=(up*(n-1)+upval)/n
        down = (down*(n-1)+downval)/n

        rs=up/down
        rsi[i]=100. - 100./(1.+rs)
    return rsi

def movingaverage(values, window):
    weights = np.repeat(1.0, window)/window
    smas=np.convolve(values, weights, 'valid')
    return smas

def ExpMoveingAverage(values, window):
    weight=np.exp(np.linspace(-1., 0., window))
    weight/=weight.sum()
    a=np.convolve(values, weight, mode='full')[:len(values)]
    a[:window]=a[window]
    return a

def computeMACD(x, slow=26, fast=12):
    '''
    macd line =12ema -26 ema
    signal line=9ema of the macd line
    histogram = macd line- signal line
    :param x:
    :param slow:
    :param fast:
    :return:
    '''
    emaslow = ExpMoveingAverage(x, slow)
    emafast = ExpMoveingAverage(x, fast)

    return emaslow, emafast, emafast-emaslow

def graphData(stock, MA1, MA2):
    try:
        try:
         print 'pullling data on', stock
         urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=1y/csv'
         stockFile=[]

         try:
            sourceCode=urllib2.urlopen(urlToVisit).read()
            splitSource =sourceCode.split('\n')
            for eachLine in splitSource:
                splitLine=eachLine.split(',')
                if len(splitLine)==6:
                    if 'value' not in eachLine:
                        stockFile.append(eachLine)


         except Exception, e:
            print str(e), 'failed to orgnize price data'
        except Exception,e:
         print str(e),' failed to pull price data'


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


        rsiClol='#00ffe8'
        posCol='#386d13'
        negCol='#6f2020'


        ax1=plt.subplot2grid((7,4),(1,0), rowspan=4, colspan=4, axisbg='#07000d')
        candlestick(ax1, candleAr[-sp:], width=1, colorup='#9eff15', colordown='#ff1717')
        ax1.plot(date[-sp:], Av1[-sp:], '#5998ff', label=label1, linewidth=1.5)
        ax1.plot(date[-sp:], Av1[-sp:], '#e1edf9', label=label2, linewidth=1.5)
        ax1.plot(date[-sp:], Av2[-sp:])

        #ax1.plot(date, openp)
        #ax1.plot(date, highp)
        #ax1.plot(date, lowp)
        #ax1.plot(date, closep)
        plt.ylabel('Stock price and Volume', color='w')
        maLeg=plt.legend(loc=9, ncol=2, prop={'size' : 7}, fancybox=True)
        maLeg.get_frame().set_alpha(0.4)
        ax1.grid(True, color='w')
        ax0 = plt.subplot2grid((7, 4), (0, 0), sharex=ax1,rowspan=1, colspan=4, axisbg='#07000d')

        rsi = rsiFunc(closep)

        ax0.plot(date[-sp:], rsi[-sp:], '#00ffe8', linewidth=1.5)
        ax0.axhline(70, color=posCol)
        ax0.axhline(30, color=negCol)
        ax0.fill_between(date[-sp:], rsi[-sp:], 70, where=(rsi[-sp:] >= 70), facecolor=posCol, edgecolor=rsiClol)
        ax0.fill_between(date[-sp:], rsi[-sp:], 30, where=(rsi[-sp:] <=30), facecolor=negCol, edgecolor=negCol)
        ax0.set_ylim(0, 100)
        ax0.spines['bottom'].set_color("#5998ff")
        ax0.spines['top'].set_color("#5998ff")
        ax0.spines['right'].set_color("#5998ff")
        ax0.spines['left'].set_color("#5998ff")
        ax0.tick_params(axis='x', colors='w')
        ax0.tick_params(axis='y', colors='w')
        ax0.set_yticks([30, 70])
        ax0.yaxis.label.set_color("w")
        ax0.text(0.0015, 0.95, 'RSI (14)', va='top', color='w', transform=ax0.transAxes)
        plt.setp(ax0.get_xticklabels(), visible=False)
        # plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='lower'))
        plt.ylabel('RSI', color='w')
        volumeMin = 0




        #put xaxis 1 after last graph




        ax1v = ax1.twinx()
        ax1v.fill_between(date[-sp:], volumeMin, volume[-sp:], facecolor='#00ffe8', alpha=.5)


        ax1.yaxis.label.set_color('w')

        ax1.spines['bottom'].set_color("#5998ff")
        ax1.spines['top'].set_color("#5998ff")
        ax1.spines['right'].set_color("#5998ff")
        ax1.spines['left'].set_color("#5998ff")
        ax1.tick_params(axis='x', colors='w')
        ax1.tick_params(axis='y', colors='w')
        plt.setp(ax1.get_xticklabels(), visible=False)

        # ax2.bar(date, volume)
        ax1v.axes.yaxis.set_ticklabels([])
        plt.ylabel('Volume', color='w')
        ax1v.grid(True)
        ax1v.spines['bottom'].set_color("#5998ff")
        ax1v.spines['top'].set_color("#5998ff")
        ax1v.spines['right'].set_color("#5998ff")
        ax1v.spines['left'].set_color("#5998ff")
        ax1v.set_ylim(0, 5*volume.max())
        ax1v.tick_params(axis='x', colors='w')
        ax1v.tick_params(axis='y', colors='w')















        ax2=plt.subplot2grid((7,4), (5,0), sharex=ax1, rowspan=2, colspan=4, axisbg='#07000d')
        nslow=26
        nfast=12
        nema=9

        emaslow, emafast, macd = computeMACD(closep)
        ema9 = ExpMoveingAverage(macd,nema)
        fillcolor='#00ffe8'
        ax2.plot(date[-sp:], macd[-sp:], color='#4ee6fd', lw=2)
        ax2.plot(date[-sp:],ema9[-sp:], color='#e1edf9',lw=1)
        ax2.fill_between(date[-sp:], macd[-sp:]-ema9[-sp:], 0, alpha=0.5, facecolor=fillcolor, edgecolor=fillcolor )
        plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
        ax2.text(0.015, 0.95, 'MACD 12,26,9', va='top',color='w', transform=ax2.transAxes)
        ax2.xaxis.set_major_locator(mticker.MaxNLocator(8))
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax2.spines['bottom'].set_color("#5998ff")
        ax2.spines['top'].set_color("#5998ff")
        ax2.spines['right'].set_color("#5998ff")
        ax2.spines['left'].set_color("#5998ff")

        ax2.tick_params(axis='x', colors='w')
        ax2.tick_params(axis='y', colors='w')
        plt.ylabel('MACD', color='w')

        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)
        #for label in ax2.xaxis.get_ticklabels():
        #    label.set_rotation(45)
        plt.subplots_adjust(left = .09, bottom = 0.18, right = 0.94, top = 0.95, wspace = 0.2, hspace = 0)



        plt.xlabel('Date')

        plt.suptitle(stock, color='w')
       # plt.setp(ax1.get_xticklabels(), visible=True)

        ax1.annotate('Big news!', (date[210], Av1[210]), xytext=(0.8,0.8),
                     textcoords='axes fraction', arrowprops=dict(facecolor='white', shrink=0.05),
                     fontsize='14', color='w',
                     horizontalalignment='right', verticalalignment='top')





        plt.show()
        fig.savefig('example.png', facecolor=fig.get_facecolor())


    except Exception,e:
        print 'failed main loop' + str(e)


while True:
    stockToUse=raw_input('Stock to Chart:')
    graphData(stockToUse,20,200)
