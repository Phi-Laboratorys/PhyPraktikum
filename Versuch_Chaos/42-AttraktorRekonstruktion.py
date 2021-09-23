import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc
from scipy.optimize import curve_fit

rc('text', usetex=True)
rc('font', family='serif', size=35)

data = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=70kO/06_09_2021_19_36_25_G11_shinriki_0.dat'
df = pd.read_csv(data, delim_whitespace=True, skiprows=7, decimal=',')

print(df.head())


n=60
v1 = 
#Ploting
#fig = plt.figure()

ax1 = fig.add_subplot(projection='3d')
ax1.plot(v1, v2, v3, color='k')
ax1.set_xlabel('$V_1(x)$ in V')
ax1.set_ylabel('$V_1(x+n)$ in V')
ax1.set_zlabel('$V_1(x+2n)$ in V')
ax1.view_init(azim=145, elev=40)
ax1.set_xlim(-2.5,2.5)
ax1.set_ylim(-0.5,0.5)
ax1.set_zlim(-0.5,0.5)