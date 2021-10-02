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

'''Single Exponential Fit'''
'''
# Data import
path = 'Versuch_FRET/Daten/TCSPC-data/Aufg-1'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files]
data.sort()

data_CFP = [i for i in data if 'CFP' in i]
data_YFP = [i for i in data if 'YFP' in i]
data_CY  = [i for i in data if 'CY'  in i]

def fitSingleExp(data, picname, start, end, t_dead): 
    
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
        print(j, x0, amp, *popt)

        plt.figure(figsize=(12, 8), dpi=80)
        plt.plot(x,y, label = 'Messreihe')
        plt.plot(df_fit['Time[ns]'], singleExp(df_fit['Time[ns]'], *popt), label = 'Exponentieller Fit', lw=2)
        plt.xlabel('$t$ in ns')
        plt.ylabel('Intensität')
        plt.legend()
        plt.savefig('Versuch_FRET/Bilder/Lebenszeit/SingleExp/'+i+'.pdf',bbox_inches='tight')
        #plt.show()

filename = ['CFP1-c1','CFP2-c1','CFP3-c1']
fitSingleExp(data_CFP, filename, 90, 1550, 5)
filename = ['YFP1-c2','YFP2-c2','YFP3-c2']
fitSingleExp(data_YFP, filename, 90, 1550, 5)
filename = ['CY1-c1','CY1-c2','CY2-c1','CY2-c2','CY3-c1','CY3-c2','CY4-c1','CY4-c2','CY5-c1','CY5-c2']
fitSingleExp(data_CY, filename, 90, 1550, 5)
'''


'''Double Exponential Fit'''
'''
path = 'Versuch_FRET/Daten/TCSPC-data/Aufg-2'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files]
data.sort()

def fitDoubleExp(data, picname, start, end, t_dead, amp, amp_guess, k): 
    
    # Fitting Functions
    def doubleExp(x, t1, t2):
        return amp*(np.exp(-x/t1)+amp_guess*np.exp(-x/t2)) # b = A2/A1, a = A1
    
    df = pd.read_csv(data, delim_whitespace=True, skiprows=11, encoding='Windows 1252')
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df[:][start:end].reset_index()

    x = df['Time[ns]']
    y = df['Decay']

    n = 200
    df['max'] = df.iloc[argrelextrema(df['Decay'].values, np.greater_equal,order=n)[0]]['Decay']

    fit_start = df['max'].dropna().index.values[0]

    df_fit = df[['Time[ns]','Decay','Fit']]
    df_fit = df_fit[df_fit['Time[ns]']>=t_dead].reset_index()

    popt, _ = curve_fit(doubleExp, df_fit['Time[ns]'], df_fit['Decay'])

    plt.figure(figsize=(12, 8), dpi=80)
    plt.plot(x,y, label = 'Messreihe')
    plt.plot(df_fit['Time[ns]'], doubleExp(df_fit['Time[ns]'], *popt), label = 'Doppel Exponentieller Fit', lw=2)
    plt.xlabel('$t$ in ns')
    plt.ylabel('Intensität')
    plt.legend()
    
    plt.savefig('Versuch_FRET/Bilder/Lebenszeit/DoubleExp/'+picname+str(k)+'.pdf',bbox_inches='tight')
    #plt.show()
    
    delta_yq = (df_fit['Decay'] - doubleExp(df_fit['Time[ns]'], *popt))**2
    return delta_yq.sum(), *popt
    
        
filename = 'CY5-c12'
Amp_guess = np.linspace(0, 30, 50)

list_delta_y = []
list_t1, list_t2 = [], []
k = 1

for i in Amp_guess:
    delta_y, t1, t2 = (fitDoubleExp(data[4], filename, 90, 1550, 5, 22002, i, k))
    list_delta_y.append(delta_y)
    list_t1.append(t1)
    list_t2.append(t2)
    k += 1

d = {'Amp':Amp_guess,  'delta_y':list_delta_y, 't1':list_t1, 't2':list_t2}
df_opt = pd.DataFrame(d)

df_opt['delta_y'] = df_opt['delta_y']/1e10
df_opt = df_opt[:][0:41]

mini = df_opt.iloc[[df_opt[['delta_y']].idxmin()[0]]]

print(df_opt.to_latex())

plt.figure(figsize=(12, 8), dpi=80)
plt.plot(df_opt['Amp'], df_opt['delta_y'], 'o', label = 'Berechnete Werte')
plt.plot(mini['Amp'], mini['delta_y'], 'o', label = 'Minimum', color = 'r')
plt.xlabel(r'$\frac{N_2}{N_1}$')
plt.ylabel(r'$\sum(\Delta y)^2$')
plt.legend()
plt.savefig('Versuch_FRET/Bilder/Lebenszeit/DoubleExp/Optimize.pdf', bbox_inches='tight')
plt.show()
'''

'''Convolution'''
def gaussian(x, amplitude, stddev, mean):
    return amplitude * np.exp(-((x - mean) / (np.sqrt(2) * stddev))**2)


for i in data_IRF:
    df = pd.read_csv(i, delim_whitespace=True)
    df = df['N(t)'][70:200]