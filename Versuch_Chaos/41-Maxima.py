import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from scipy.signal import argrelextrema

data = "Versuch_Chaos/Daten/Pendel/3.2a/06_09_2021_14_41_30_G11_pendel_0.dat"
df = pd.read_csv(data, delim_whitespace=True, skiprows=7, decimal=',')
df = df.dropna()

n = 5  # number of points to be checked before and after
df['data'] = df['Ua(V)']
# Find local peaks

#df['min'] = df.iloc[argrelextrema(df.data.values, np.less_equal,order=n)[0]]['data']
df['max'] = df.iloc[argrelextrema(df.data.values, np.greater_equal,order=n)[0]]['data']

df = df.dropna()
df = df.drop(0)

df['dt(s)'] = df.diff(axis = 0, periods = 1)['t(s)']
#df = df.diff(axis = 0, periods = 1)
df = df.loc[(df>=0.1).any(axis=1)]
# Plot results
#plt.scatter(df.index, df['min'], c='r')
#plt.scatter(df['t(s)'], df['max'], c='g')
#plt.hist(df['t(s)'])
plt.scatter(df['Ua(V)'],df['dt(s)'])
plt.ylim(2,2.5)
plt.show()