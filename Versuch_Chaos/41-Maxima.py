import numpy as np
import pandas as pd
import matplotlib.pylab as plt

data = "Versuch_Chaos/Daten/Pendel/3.2a/06_09_2021_14_41_30_G11_pendel_0.dat"
df = pd.read_csv(data, delim_whitespace=True, skiprows=7)
df = df.dropna()
print(df)

plt.plot(df['t(s)'],df['Ua(V)'],'.')
plt.show()

'''
t0 = df['time [s]'][0]
U_max = df['U_a [V]'][0]

dt = []
i =  0

while i < len(df):
    
    if U_max < df['U_a [V]'][i]:
        U_max = df['U_a [V]'][i]
        
    if U_max > df['U_a [V]'][i]:
        t0 = df['time [s]'][i-1]
        
    i += 1
'''