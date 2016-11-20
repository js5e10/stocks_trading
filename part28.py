import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
    pullData=open('sampleText.txt', 'r').read()
    dataArray = pullData.split('\n')
    xar=[]
    yar=[]
    for eachline in dataArray:
        if len(eachline)>1:
            x,y=eachline.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar, yar)

ani=animation.FuncAnimation(fig, animate, interval=1000)
plt.show()