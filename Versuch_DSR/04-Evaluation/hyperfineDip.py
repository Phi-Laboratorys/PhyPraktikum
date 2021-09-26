import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc
from scipy.signal import argrelextrema
from scipy.optimize import curve_fit
import scipy.constants as const

rc('text', usetex=True)
rc('font', family='serif', size=18)

data = 'Versuch_DSR/Daten/Data_Trendless/allPeak/DataTrendless_allPeak_Temp24.csv'
df = pd.read_csv(data,index_col=0)

x = [df['x(A/Hz/V/nm)'][0:450],df['x(A/Hz/V/nm)'][450:900],
          df['x(A/Hz/V/nm)'][1100:1380],df['x(A/Hz/V/nm)'][1380:1650]]
yai3 = [df['yai3(V)'][0:450],df['yai3(V)'][450:900],
          df['yai3(V)'][1100:1380],df['yai3(V)'][1380:1650]] 
yai1 = [df['yai1(V)'][0:450],df['yai1(V)'][450:900],
          df['yai1(V)'][1100:1380],df['yai1(V)'][1380:1650]]  
yai4 = [df['yai4(V)'][0:450],df['yai4(V)'][450:900],
          df['yai4(V)'][1100:1380],df['yai4(V)'][1380:1650]]  
'''
n = 1
for i,j,k,q in zip(x,yai1,yai3,yai4):
    plt.figure(figsize=(12, 8), dpi=80)
    plt.plot(i,j,label='sample beam')
    plt.plot(i,k,label='reference beam')
    plt.plot(i,q,label='fabry-pérot')
    
    plt.xlabel('laser current in mA')
    plt.ylabel('amplitude in V')  
    plt.legend()
    plt.savefig('Versuch_DSR/Bilder/Aufg-4/hyperfine'+str(n)+'.pdf', bbox_inches='tight')
    plt.legend()
    plt.show()
    
    n += 1
'''

# data of peak 3
data3 = 'Versuch_DSR/Daten/Data_Raw/3Peak/21092021_12_54_07_group11_Mes4_Temp24_3Peak.dat'
df = pd.read_csv(data3, delim_whitespace=True, skiprows=4)
df = df[:][1100:len(df)-300]

# offset to other data
df['yai1(V)'] = df['yai1(V)'] - 0.04

n = 30
df['y3_max(V)'] = df.iloc[argrelextrema(df['yai1(V)'].values, np.greater_equal,order=n)[0]]['yai1(V)']

x, y = df['x(A/Hz/V/nm)'], df['yai1(V)']

# transform data in wavelength mit current tuning 
cu_data = 'Versuch_DSR/Daten/currentTuning_points.csv'
cu = pd.read_csv(cu_data)
    
x_cu, y_cu = cu['current(mA)'], cu['lambda(nm)']

# create linear function between data points
i = 0
m, t = [], []
while i < len(x_cu)-1:
    m.append((y_cu[i+1]-y_cu[i])/(x_cu[i+1]-x_cu[i]))
    t.append(y_cu[i]-m[i]*x_cu[i])
    i += 1

# transformation
x1 = x.loc[(x >= x_cu[0]) & (x < x_cu[1])]
result1 = x1.transform(func = lambda x : m[0]*x + t[0])
x2 = x.loc[(x >= x_cu[1]) & (x < x_cu[2])]
result2 = x2.transform(func = lambda x : m[1]*x + t[1])
x3 = x.loc[(x >= x_cu[2]) & (x < x_cu[3])]
result3 = x3.transform(func = lambda x : m[2]*x + t[2])

result = result1.append(result2).append(result3)

df['lambda(nm)'] = result
df['freq(THz)'] = const.c/(1000*df['lambda(nm)'])

df_peak = df[['x(A/Hz/V/nm)','lambda(nm)','freq(THz)','y3_max(V)']].drop_duplicates(subset=['y3_max(V)'], keep='first').dropna()[1:6]

x_data = [df['x(A/Hz/V/nm)'][100:210], df['x(A/Hz/V/nm)'][210:315],
          df['x(A/Hz/V/nm)'][315:380],df['x(A/Hz/V/nm)'][380:420],
          df['x(A/Hz/V/nm)'][420:480]]
y_data = [df['yai1(V)'][100:210], df['yai1(V)'][210:315],
          df['yai1(V)'][315:380], df['yai1(V)'][380:420],
          df['yai1(V)'][420:480]]

amp = df_peak['y3_max(V)']
mean = df_peak['x(A/Hz/V/nm)']


plt.figure(figsize=(12, 8), dpi=80)

n = 1
for i,j,m,a in zip(x_data, y_data, mean, amp):
    
    def lorentz(x, c):
        return (a*c**2/((x-m)**2 + c**2))

    popt, _ = curve_fit(lorentz, i, j)

    print(*popt)
    
    y_lor = lorentz(x, *popt) - 0.032

    plt.plot(x, y_lor, label = 'lorentzian fit for dip'+str(n))
    plt.fill_between(x,-0.032,y_lor,alpha=0.5)

    n += 1


plt.plot(x,y - 0.032, color='black', label = 'absorption spectrum peak 3')
#plt.plot(df_peak['x(A/Hz/V/nm)'], df_peak['y3_max(V)'], 'o')
plt.xlabel('laser current in mA')
plt.ylabel('amplitude in V')  
plt.legend(loc='upper left')
plt.savefig('Versuch_DSR/Bilder/Aufg-4/hyperfinePeak3.pdf', bbox_inches='tight')
plt.show()