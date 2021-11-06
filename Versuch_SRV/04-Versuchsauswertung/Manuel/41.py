import numpy as np
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
import matplotlib.cm as cm
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from matplotlib.patches import Rectangle
from scipy.signal import argrelextrema
from scipy.optimize import curve_fit
import scipy.constants as const

rc('text', usetex=True)
rc('font', family='serif', size=22)

'''
#############################
##                         ##
##      Teilaufgabe a      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/41/a'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]
data.sort()

#data_sinus = [i for i in data if 'Sinus' in i]
#data_sqare = [i for i in data if 'Rechteck' in i]
#data_tri  =  [i for i in data if 'Dreieck' in i]

plt.figure(figsize=(12,8), dpi=80)

for i in data:
    df = pd.read_csv(i, skiprows=4, delim_whitespace= True)
    df = df[:][:4500]
    
    n = 50
    df['max/dB'] = df.iloc[argrelextrema(df['y-FFTcurve'].values, np.greater_equal,order=n)[0]]['y-FFTcurve']
    
    x = df['Fqscale-FFT']
    y, y_max = df['y-FFTcurve'], df['max/dB']
    x_t, y_g = df['time'], df['y-generator']
    
    df_max = df[['Fqscale-FFT', 'max/dB']].dropna()
    df_max = df_max[:][:-1]
    #df_max['max/dB'] = df_max['max/dB'] + 120
    
    # df_max['diff'] = df_max['max'].diff().abs()
    
    df_max['max/V'] = 1 * 10**(df['max/dB']/20) * np.sqrt(2) 
        
    if 'Sinus' in i:
        print('Sinus')
        #df_max['max/V'] = 1000 * 10**(df['max/dB']/20) * np.sqrt(2)
        theo = [1.000000]
        k = 1
        while k < len(df_max):
            theo.append(0)
            k+=1
        
        df_max['Theo/V'] = theo
        
        df_max['diff/V'] = abs(-df_max['Theo/V'] + df_max['max/V'])
        df_max.index = np.arange(1, len(df_max) + 1)
            
        print(df_max[0:35].to_latex())
        
    if 'Rechteck' in i:
        print('Rechteck')
        #df_max['max/V'] = 1000 * 10**(df['max/dB']/20) * np.sqrt(1)
        theo = []
        k = 1
        while k < len(df_max)+1:
            theo.append(4/np.pi * 1/(2*k-1))
            k+=1
        
        df_max['Theo/V'] = theo
        
        df_max['diff/V'] = abs(-df_max['Theo/V'] + df_max['max/V'])
        df_max.index = np.arange(1, len(df_max) + 1)
            
        print(df_max[0:35].to_latex())
    
        plt.plot(df_max['Fqscale-FFT'][0:35]/1000,df_max['diff/V'][0:35]*1E6,'o',label='Rechteck')
        
    if 'Dreieck' in i:
        print('Dreieck')
        #df_max['max/V'] = 1000 * 10**(df['max/dB']/20) * np.sqrt(3)
        theo = []
        k = 1
        while k < len(df_max)+1:
            theo.append(8/(np.pi**2) * 1/((2*k-1)**2))
            k+=1
        
        df_max['Theo/V'] = theo
        
        df_max['diff/V'] = abs(-df_max['Theo/V'] + df_max['max/V'])
        df_max.index = np.arange(1, len(df_max) + 1)
            
        print(df_max[0:35].to_latex())
    
        plt.plot(df_max['Fqscale-FFT'][0:35]/1000,df_max['diff/V'][0:35]*1E6,'o',label='Dreieck')
    
plt.ylabel(r'$\Delta A$ in $\mu$V')
plt.xlabel(r'$f$ in kHz')        
plt.legend()
plt.savefig('Versuch_SRV/Bilder/Manuel/41/Residuum.pdf',bbox_inches='tight')
plt.show()
'''
'''
#############################
##                         ##
##      Teilaufgabe b      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/41/b'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]
data.sort()

df = pd.read_csv(data[1], skiprows=4, delim_whitespace= True)
#df = df[:][:4500]
df = df[:][:700]

print(df)

x, y = df['Fqscale-FFT']/1000, df['y-FFTcurve']
plt.figure(figsize=(12,8), dpi=80)
plt.plot(x,y, color = 'black')
plt.ylabel(r'$A$ in dB')
plt.xlabel(r'$f$ in kHz')
plt.savefig('Versuch_SRV/Bilder/Manuel/41/FourierSinus.pdf', bbox_inches='tight')
plt.show()
'''
'''
#############################
##                         ##
##      Teilaufgabe c      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/41/c'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]
data.sort()

n = [10, 100, 50, 0]
colors = ['blue', 'orange', 'red', 'black']
#print(data)

plt.figure(figsize=(12,8), dpi=80)
for i, n, c in zip(data, n, colors):
    df = pd.read_csv(i, skiprows=4, delim_whitespace= True)
    #df = df[:][:4500]
    df = df[:][:300]
    
    x, y = df['Fqscale-FFT']/1000, df['y-FFTcurve']
    
    plt.plot(x,y, label = '$N$= '+str(n), color = c)
    
plt.ylabel(r'$A$ in dB')
plt.xlabel(r'$f$ in kHz')
plt.legend()
plt.savefig('Versuch_SRV/Bilder/Manuel/41/Mittelung.pdf', bbox_inches='tight')
plt.show()
'''
#'''
#############################
##                         ##
##      Teilaufgabe d      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/41/d'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]
data.sort()

data = [data[2],data[1],data[3],data[0]]

n = ['10\%', '50\%', '100\%', '120\%']
colors = ['red', 'orange', 'black', 'blue']

fig, ax1 = plt.subplots(figsize=(12,8), dpi=80)

#rect = Rectangle((0.17, 0.22), 0.65, 0.47, facecolor='white', ec='none', alpha=1, transform=fig.transFigure, zorder=-1)

axins = inset_axes(ax1, 6,3 , loc='center') # insert pic
mark_inset(ax1,axins,loc1=2,loc2=1)

for i, n, c in zip(data, n, colors):
    df = pd.read_csv(i, skiprows=4, delim_whitespace= True)
    #df = df[:][:4500]
    df = df[:][:251]
    df_win = df[:][2:125]
    
    #x, y = df['Fqscale-FFT']/1000, df['y-FFTcurve']
    x, y = df['time'], df['y-generator']
    x_win, y_win = df_win['time'], df_win['y-generator']
    
    ax1.plot(x,y, label = '$d$ = '+n, color = c)
    axins.plot(x,y, label = '$d$ = '+n, color = c)

axins.set_xlim(x_win.min(),x_win.max())
axins.set_ylim(y_win.min(),y_win.max())

#axins.patch.set_facecolor('white')
#axins.patch.set_alpha(0.5)
#axins.patches.append(rect)

#axins.set_ylabel(r'$U$ in V')
#axins.set_xlabel(r'$f$ in kHz')
ax1.tick_params(direction = "in")
axT = ax1.secondary_xaxis('top')
axT.tick_params(direction = "in")
axT.xaxis.set_ticklabels([])
ax1.set_ylabel(r'$U$ in V')
ax1.set_xlabel(r'$f$ in kHz')

axins.legend(loc = (0.87,0.9)) 

#plt.savefig('Versuch_SRV/Bilder/Manuel/41/SignalRauschAbstandKomplett.pdf', bbox_inches='tight')
#plt.savefig('Versuch_SRV/Bilder/Manuel/41/SignalRauschAbstand.pdf', bbox_inches='tight')
plt.savefig('Versuch_SRV/Bilder/Manuel/41/SignalRauschAbstandAll.pdf', bbox_inches='tight')
plt.show()
#'''
'''
#############################
##                         ##
##      Teilaufgabe e      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/41/e'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]
data.sort()

n = ['20MHz', '5MHz', '10MHz', '100kHz', '10kHz', '1kHz']
colors = ['blue', 'orange', 'red', 'grey', 'purple', 'black']
#print(data)

plt.figure(figsize=(12,8), dpi=80)
for i, n, c in zip(data, n, colors):
    df = pd.read_csv(i, skiprows=4, delim_whitespace= True)
    #df = df[:][:4500]
    df = df[:][:252]
    #df = df[:][5:125]
    
    #x, y = df['Fqscale-FFT']/1000, df['y-FFTcurve']
    x, y = df['time'], df['y-generator']
    
    plt.plot(x,y, label = r'$f_\mathrm{Band}$ = '+n, color = c)
    
plt.ylabel(r'$U$ in V')
plt.xlabel(r'$f$ in kHz')
plt.legend()
plt.savefig('Versuch_SRV/Bilder/Manuel/41/BandbreiteKomplett.pdf', bbox_inches='tight')
#plt.savefig('Versuch_SRV/Bilder/Manuel/41/Bandbreite.pdf', bbox_inches='tight')
plt.show()
'''