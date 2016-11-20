import urllib2
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange



def grabQuandle(ticker):

    netIncomeAr=[]
    revAr=[]
    endLink = 'sort_order=asc'

    try:
        netIncome=urllib2.urlopen('https://www.quandl.com/api/v3/datasets/RAYMOND/'+ticker+'_NET_INCOME_Q.csv?api_key=EnsMMxcWJfz6mrzs3v6X').read()
        revenue=urllib2.urlopen('https://www.quandl.com/api/v3/datasets/RAYMOND/'+ticker+'_REVENUE_Q.csv?api_key=EnsMMxcWJfz6mrzs3v6X').read()

        splitNI=netIncome.split('\n')
        print 'Net Income'
        for eachNI in splitNI[1:-1]:
            print eachNI
            netIncomeAr.append(eachNI)
        print'_______________________'
        splitRev=revenue.split('\n')
        print 'Revenue:'
        for eachRev in splitRev[1:-1]:
            print eachRev
            revAr.append(eachRev)
        incomeDate, income = np.loadtxt(netIncomeAr, delimiter=',' , unpack=True,
                                   converters={0: mdates.strpdate2num('%Y-%M-%d')})

        revDate, revenue = np.loadtxt(revAr, delimiter=',', unpack=True,
                                        converters={0: mdates.strpdate2num('%Y-%M-%d')})
        fig=plt.figure()
        ax1=plt.subplot2grid((6,6), (0,0), rowspan=3, colspan=6)
        ax1.plot(incomeDate, income)
        plt.ylabel('Net Income')
        ax2 = plt.subplot2grid((6, 6), (3, 0), rowspan=3, colspan=6)
        ax2.plot(revDate, revenue)
        plt.ylabel('Revenue')

        ax1.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
        ax2.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

        plt.subplots_adjust(hspace=0.53)

        plt.show()

        print revAr
    except Exception, e:
        print 'failed the main quandle loop for reason of', str(e)

grabQuandle('YHOO')