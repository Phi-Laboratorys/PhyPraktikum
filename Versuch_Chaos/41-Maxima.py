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
df = df.drop_duplicates(subset=['max'], keep='last')

df['dt(s)'] = df.diff(axis = 0, periods = 1)['t(s)']


#Mittelwerte für gleiche Zeiten
df2 = df[['dt(s)', 'max']]
df2 = df2.groupby(['dt(s)']).mean()
print(df2.keys())








#df = df.drop_duplicates(subset=['dt(s)'], keep='last')
#print(df)
#df = df.diff(axis = 0, periods = 1)
#df = df.loc[(df>=0.1).any(axis=1)]
# Plot results
#plt.scatter(df['t(s)'], df['min'], c='r')
#plt.scatter(df['t(s)'], df['max'], c='g')
#plt.plot(df['t(s)'], df['Ua(V)'])
#plt.hist(df['dt(s)'])
#plt.plot(df['Ua(V)'],df['dt(s)'],'.')
#plt.ylim(2,2.5)
plt.scatter(df2['max'], df2.index)
plt.show()