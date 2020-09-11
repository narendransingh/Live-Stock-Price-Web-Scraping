import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


plt.style.use('fivethirtyeight')
fig = plt.figure()
fig.patch.set_facecolor('xkcd:gray')
fig.suptitle("Live Stock Price Tracking 11/09/2020", fontsize=14)
fig.subplots_adjust(wspace=1.0, hspace=1.0)

ax1 = fig.add_subplot(2, 2, 1)
ax1.set_facecolor('gray')
#ax1.set_ylim([10000,50000])

ax2 = fig.add_subplot(2, 2, 2)
ax2.set_facecolor('gray')
ax3 = fig.add_subplot(2, 2, 3)
ax3.set_facecolor('gray')
ax4 = fig.add_subplot(2, 2, 4)
ax4.set_facecolor('gray')

#df = pd.read_csv('real_time_stock_data_obsolete.csv')

def animate(i):
    #global df
    df = pd.read_csv('real_time_stock_data_extract.csv')
    #for first graph
    #ys = df.iloc[1:, 2].values #pick the second value from the df.
    ys = df.iloc[1:, 2].sort_values()
    xs = list(range(1, len(ys)+1)) #list has step size of ys which is 100
    ax1.clear() #we clear the plot graph every load
    ax1.y
    ax1.plot(xs, ys, color = 'black')
    ax1.set_title('S&P BSE Sensex', fontsize=12)
    #for second graph
    ys = df.iloc[1:, 3].sort_values() #pick the third row value from the df.
    ax2.clear() #we clear the plot graph every load
    ax2.plot(xs, ys, color = 'black')
    ax2.set_title('NIFTY 50', fontsize=12)
    #for third graph
    ys = df.iloc[1:, 4].sort_values() #pick the second value from the df.
    ax3.clear() #we clear the plot graph every load
    ax3.plot(xs, ys, color = 'black')
    ax3.set_title('Dow Jones Industrial Average', fontsize=12)
    #for fourth graph
    ys = df.iloc[1:, 5].sort_values() #pick the second value from the df.
    ax4.clear() #we clear the plot graph every load
    ax4.plot(xs, ys, color = 'black')
    ax4.set_title('NASDAQ Composite', fontsize=12)

ani = animation.FuncAnimation(fig, animate, interval=1000) #animate function to refresh the graph every 1 sec.

#plt.interactive(True)
plt.tight_layout()
plt.show()



