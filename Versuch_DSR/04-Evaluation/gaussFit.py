import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc
from scipy.optimize import curve_fit

rc('text', usetex=True)
rc('font', family='serif', size=18)

data = 'Versuch_DSR/Daten/Data_Trendless/allPeak/DataTrendless_allPeak_Temp24.csv'
df = pd.read_csv(data,index_col=0)

x,y = df['x(A/Hz/V/nm)'],df['yai3(V)']
x_data = [df['x(A/Hz/V/nm)'][0:450],df['x(A/Hz/V/nm)'][451:900],
          df['x(A/Hz/V/nm)'][901:1380],df['x(A/Hz/V/nm)'][1381:]]
y_data = [df['yai3(V)'][0:450],df['yai3(V)'][451:900],
          df['yai3(V)'][901:1380],df['yai3(V)'][1381:]]  
mean   = [119.4429,125.0267,131.8581,134.7829]

plt.figure(figsize=(12, 8), dpi=80)
plt.plot(x,y,color = 'black', label = 'reference beam')  

x_fit, y_fit = [],[]
n = 1

for i, j, m in zip(x_data, y_data, mean):
    
    def gaussian(x, amplitude, stddev):
        return amplitude * np.exp(-((x - m) / (np.sqrt(2) * stddev))**2)

    popt, _ = curve_fit(gaussian, i, j)

    print(*popt)

    plt.plot(x, gaussian(x, *popt), label='gaussian fit for peak '+str(n))
    plt.fill_between(x,0,gaussian(x, *popt),alpha=0.5)
    n += 1

plt.xlabel('laser current in mA')
plt.ylabel('amplitude in V')  
plt.legend()
plt.savefig('Versuch_DSR/Bilder/Aufg-3/gaussFit.pdf', bbox_inches='tight')
plt.show()