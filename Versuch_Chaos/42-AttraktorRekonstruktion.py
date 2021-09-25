import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc
from matplotlib.widgets import Slider

rc('text', usetex=True)
rc('font', family='serif', size=20)

data = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=70kO/06_09_2021_19_36_25_G11_shinriki_0.dat'
df = pd.read_csv(data, delim_whitespace=True, skiprows=7, decimal=',')

print(df.head())

#Rekostrucktion
n=70
v1=df['V1(V)']
v2=df['V1(V)'].shift(periods=n)
v3=df['V1(V)'].shift(periods=n*2)


#Ploting
fig = plt.figure()
ax1 = fig.add_subplot(projection='3d')
ax1.plot(v1, v2, v3, color='k')
ax1.set_xlabel('$V_1(x)$ in V')
ax1.set_ylabel('$V_1(x+n)$ in V')
ax1.set_zlabel('$V_1(x+2n)$ in V')
#ax1.view_init(azim=145, elev=40)
#ax1.set_xlim(-2.5,2.5)
#ax1.set_ylim(-0.5,0.5)
#ax1.set_zlim(-0.5,0.5)

#Slider
axstep = plt.axes([0.25,0.1,0.65,0.03], facecolor='r')
step_slider = Slider(ax=axstep, label='n', valmin=1, valmax=200, valinit=60, valstep=1)

def update(i):
    #ax1.set_xdata()
    #ax1.set_ydata(df['V1(V)'].shift(periods=i))
    ax1.set_3d_properties(df['V1(V)'].shift(periods=i*2))
    plt.draw()

step_slider.on_changed(update)
plt.show()