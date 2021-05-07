import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data1 = 'Versuch_EL2/41-Data-1000kOhm.csv'
df1 = pd.read_csv(data1)

# Aufräumen der Tabelle
df1 = df1.sort_values(by='f/kHz', ascending=True)
df1.index = np.arange(1, len(df1)+1)

df1['U_e/mV'] = 100
df1['U_a/mV'] = df1['U_a/Div']*df1['U_a(ein)/(mV/Div)']
df1['v'] = df1['U_a/mV']/df1['U_e/mV']

x1 = df1['f/kHz']
y1 = df1['v']

plt.scatter(x1,y1)
plt.xscale('log')
plt.yscale('log')
plt.show()

data2 = 'Versuch_EL2/41-Data-4700kOhm.csv'
df2 = pd.read_csv(data2)

# Aufräumen der Tabelle
df2 = df2.sort_values(by='f/kHz', ascending=True)
df2.index = np.arange(1, len(df2)+1)

df2['U_e/mV'] = 20
df2['U_a/mV'] = df2['U_a/Div']*df2['U_a(ein)/(mV/Div)']
df2['v'] = df2['U_a/mV']/df2['U_e/mV']

x2 = df2['f/kHz']
y2 = df2['v']

plt.scatter(x2,y2)
plt.xscale('log')
plt.yscale('log')
plt.show()