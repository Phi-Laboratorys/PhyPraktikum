# Auswertung 6.2 über Python zum reinkommen für später

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

df = pd.read_csv('Versuch_KRE/04-Versuchsauswertung/6_2-Nutation.csv')

# Interpolation Just for Fun
'''
x_new = np.linspace(df['w3 [1/s]'].min(), df['w3 [1/s]'].max(), 300)
spl = make_interp_spline(df['w3 [1/s]'], df['wn/w3'], k=3)  # type: BSpline
y_smooth = spl(x_new)
plt.plot(x_new, y_smooth)
'''
df['u_f3'] = u_f3 = 0.25
df['u_tn'] = 0.01/np.sqrt(2)
df['Tn'] = df['tn']/10
df['u_Tn'] = u_Tn = df['u_tn']/np.sqrt(10)
df['w3'] = 2*np.pi*df['f3']
df['u_w3'] = 2*np.pi*u_f3
df['wn'] = 2*np.pi/df['Tn']
df['wN'] = -1/(df['Tn']*df['f3'])
df['u_wN'] = np.sqrt((u_Tn/((df['Tn']**2)*df['f3']))**2+(u_f3/((df['f3']**2)*df['Tn']))**2)

df = df.round({'u_tn':3, 'Tn':3, 'u_Tn':3, 'w3':2, 'u_w3':2,
       'wn':2, 'wN':4, 'u_wN':4})
df = df[['tn','u_tn','Tn','u_Tn','w3','wn','wN','u_wN']]
df.index = np.arange(1, len(df)+1)

x        = df['w3']
y, y_err = df['wN'], df['u_wN']
x_lin = np.linspace(x.min(), x.max(), 300)
y_mean = np.repeat(y.mean(),300)   
y_mean_err = y_err.mean()

print(y.mean(),y_err.mean())
'''
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax.plot(x_lin,y_mean,linestyle='-',label='Mittelwert',color='r')
ax.plot(x_lin,y_mean+y_mean_err,linestyle='--',color='r')
ax.plot(x_lin,y_mean-y_mean_err,linestyle='--',color='r')
ax.fill_between(x_lin,y_mean+y_mean_err,y_mean-y_mean_err,color='r',alpha=0.1)
ax.errorbar(x, y, yerr=y_err, fmt='o' ,marker='o', capsize=5,label='Messreihe')
#ax.set_title(r'$\omega_3$-$\omega_*$-Diagramm')
ax.set_xlabel(r'$\omega_3$ $[\frac{1}{s}]$')
ax.set_ylabel(r'$\omega_N$')
ax.legend()
plt.show()
'''