import numpy as np
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
import matplotlib.cm as cm
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

data = 'Versuch_SRV/Daten/44/a/LockIn_Filter.csv'
df = pd.read_csv(data)

df[['Usin(V)','Usquare(V)','Utri(V)']] = df[['Usin(V)','Usquare(V)','Utri(V)']]*np.sqrt(2)

print(df.to_latex())
'''

#############################
##                         ##
##      Teilaufgabe b      ##
##                         ##
#############################

data = ['Versuch_SRV/Daten/44/b/Bandbreite_30ms_6dB.csv', 'Versuch_SRV/Daten/44/b/Bandbreite_30ms_18dB.csv']
name = ['6dB', '18dB']
color = ['#ff7f0e','#1f77b4']

def response(f,t,n):
    return (1 + (2*np.pi*t*(f - 1))**2)**(-n/2)

plt.figure(figsize=(12,8),dpi=80)

for i,q,c in zip(data,name,color):
    df = pd.read_csv(i)
    
    x, y = df['f(Hz)']/1000, df['Ueff(V)']
    
    y = y/y.max()
    
    popt, _ = curve_fit(response, x, y)
    print(*popt)
    
    x_fit = np.linspace(x.min(), x.max(), 1000)
    
    #plt.figure(figsize=(12,8),dpi=80)
    
    #plt.plot(x_fit, response(x_fit, *popt), label = 'Fit', lw=2,color=c)
    #plt.plot(x,y,'o',label='Messreihe',color=c)
    plt.plot(x_fit, response(x_fit, *popt), label = 'Fit '+q, lw=2,color=c)
    plt.plot(x,y,'o',label='Messreihe '+q,color=c)
    plt.xlabel(r'$f$ in kHz')
    plt.ylabel(r'A (normiert)')
    plt.legend()
    #plt.savefig('Versuch_SRV/Bilder/Manuel/44/'+q+'.pdf',bbox_inches='tight')
    #plt.show()

plt.savefig('Versuch_SRV/Bilder/Manuel/44/All.pdf',bbox_inches='tight')
plt.show()