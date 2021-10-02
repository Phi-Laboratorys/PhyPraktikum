import numpy as np
from numpy.core.numeric import moveaxis
from numpy.lib.function_base import append
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
from pandas.core.algorithms import diff
from scipy.signal import argrelextrema
from scipy.optimize.minpack import curve_fit
from scipy.signal import argrelextrema
import scipy.constants as const

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=18)

# Data import
path = 'Versuch_FRET/Daten/TCSPC-data/Aufg-1'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files]
data.sort()

data_CFP = [i for i in data if 'CFP' in i]
data_YFP = [i for i in data if 'YFP' in i]
data_CY  = [i for i in data if 'CY'  in i]
data_IRF = [i for i in data if 'IRF' in i]

# Fitting Functions
def singleExp(x, t):
    return amp*np.exp(-(x-x0)/t)

def doubleExp(x, a, b, t1, t2):
    return a*(np.exp(-x/t1)+b*np.sqrt(-x/t2)) # b = A2/A1, a = A1

def gaussian(x, amplitude, stddev, mean):
    return amplitude * np.exp(-((x - mean) / (np.sqrt(2) * stddev))**2)



for i in data_IRF:
    df = pd.read_csv(i, delim_whitespace=True)
    df = df['N(t)'][70:200]

def fitExp(data, picname, start, end, t_dead): 
    
    # Fitting Functions
    def singleExp(x, t):
        return amp*np.exp(-(x-x0)/t)
    
    for j,i in zip(data,picname):
        df = pd.read_csv(j, delim_whitespace=True, skiprows=11, encoding='Windows 1252')
        df = df.apply(pd.to_numeric, errors='coerce')
        df = df[:][start:end].reset_index()

        x = df['Time[ns]']
        y = df['Decay']

        n = 200
        df['max'] = df.iloc[argrelextrema(df['Decay'].values, np.greater_equal,order=n)[0]]['Decay']

        fit_start = df['max'].dropna().index.values[0]

        df_fit = df[['Time[ns]','Decay','Fit']]
        df_fit = df_fit[df_fit['Time[ns]']>=t_dead].reset_index()

        amp, x0 = df_fit['Decay'][0], df_fit['Time[ns]'][0]

        popt, _ = curve_fit(singleExp, df_fit['Time[ns]'], df_fit['Decay'])
        print(j, x0, *popt)

        plt.figure(figsize=(12, 8), dpi=80)
        plt.plot(x,y, label = 'Messreihe')
        plt.plot(df_fit['Time[ns]'], singleExp(df_fit['Time[ns]'], *popt), label = 'Exponentieller Fit', lw=2)
        plt.xlabel('$t$ in ns')
        plt.ylabel('Intensität')
        plt.legend()
        plt.savefig('Versuch_FRET/Bilder/Lebenszeit/'+i+'.pdf',bbox_inches='tight')
        #plt.show()

filename = ['CFP1-c1','CFP2-c1','CFP3-c1']
fitExp(data_CFP, filename, 90, 1550, 5)
filename = ['YFP1-c2','YFP2-c2','YFP3-c2']
fitExp(data_YFP, filename, 90, 1550, 5)
