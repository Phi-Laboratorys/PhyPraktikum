import numpy as np
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
from scipy.signal import argrelextrema

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=18)

# Data import
path = 'Versuch_DSR/Daten/Data_Raw/allPeak'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files]
data.sort()

#cut = [70, 468, 285]
#dis = [200, 60, 100]
#fit = [1000, 550, 750]
#temp = [24,38,56]

#for i, j, k, f, t in zip(data,cut,dis, fit, temp):
df = pd.read_csv(data[0], delim_whitespace=True, skiprows=4)
df = df[:][70:len(df)-70]
x = df['x(A/Hz/V/nm)']
yai0, yai1, yai3, yai4 = df['yai0(V)'], df['yai1(V)'], df['yai3(V)'], df['yai4(V)']

yai3 = yai3+abs(yai1[70+200]-yai3[70+200])

# Fit for Spektrum
x_fit = [x[70],x[70+1],x[70+1000]]
y_fit = [yai3[70],yai3[70+1], yai3[70+1000]]
model, cov = np.polyfit(x_fit,y_fit,1,cov=True)
predict = np.poly1d(model)
y_lin = predict(x)

yai3 = yai3-y_lin
yai1 = yai1-y_lin

# Fit for signal
model, cov = np.polyfit(x,yai4,1,cov=True)
predict = np.poly1d(model)
y_sig = predict(x)

yai4 = yai4-y_sig

df['yai0(V)'], df['yai1(V)'], df['yai3(V)'], df['yai4(V)'] = yai0, yai1, yai3, yai4
n = 5
df['data'] = df['yai3(V)']
df['mini'] = df.iloc[argrelextrema(df.data.values, np.less_equal,order=n)[0]]['data']

plt.figure(figsize=(12, 8), dpi=80)
#plt.plot(x, yai0)
plt.plot(x, yai1, label='sample beam')
plt.plot(x, yai3, label='reference beam')
plt.plot(x, yai4, label='fabry-pérot')

#plt.plot(x,y_sig)
#plt.plot(x, y_lin, label='linear fit')

x_mini = df[df.mini < -0.003]['x(A/Hz/V/nm)']
y_mini = df[df.mini < -0.003]['mini']

print(df[df.mini < -0.003])

#plt.plot(x_mini, y_mini, 'o')

plt.xlabel('laser current in mA')
plt.ylabel('amplitude in V')
plt.legend()
plt.savefig('Versuch_DSR/Bilder/Aufg-1/alltrendless'+str(24)+'.pdf', bbox_inches='tight')
plt.show()