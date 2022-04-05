import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Widerstand R_1 = 1MOhm
data1 = 'Versuch_EL2/41-Data-1000kOhm.csv'
df1 = pd.read_csv(data1)

# Aufräumen der Tabelle
df1 = df1.sort_values(by='f/kHz', ascending=True)
df1.index = np.arange(1, len(df1)+1)

df1['f/Hz'] = df1['f/kHz'] * 1000
df1['s_a/Div'] = [0.1, 0.1, 0.1, 0.1, 0.1,
                  0.1, 0.1, 0.1, 0.1, 0.1,
                  0.1, 0.1, 0.1, 0.1, 0.1,
                  0.1, 0.1, 0.1, 0.1, 1,
                  1, 1, 1]

df1['U_a/mV'] = df1['U_a/Div']*df1['U_a(ein)/(mV/Div)']
df1['s_{U_a}/mV'] = df1['U_a(ein)/(mV/Div)'] * np.sqrt((0.03*df1['U_a/Div'])**2 + (df1['s_a/Div'])**2)

df1['U_e/Div'] = 5
df1['U_e(ein)/(mV/Div)'] = 20
df1['U_e/mV'] = df1['U_e/Div']*df1['U_e(ein)/(mV/Div)']
df1['s_{U_e}/mV'] = df1['U_e(ein)/(mV/Div)'] * np.sqrt((0.03*df1['U_e/Div'])**2 + (0.1)**2)

df1['v'] = df1['U_a/mV']/df1['U_e/mV']
df1['s_v'] = np.sqrt((df1['s_{U_a}/mV']/df1['U_e/mV'])**2 + ((df1['s_{U_e}/mV']*df1['U_a/mV']/(df1['U_e/mV']**2))**2))

df1 = df1.drop(columns=['f/kHz', 'U_e/Div', 'U_e(ein)/(mV/Div)', 'U_a(ein)/(mV/Div)', 'U_a/Div', 's_a/Div'])
df1 = df1.round({'U_e/mV':0, 's_{U_e}/mV':0, 'U_a/mV':0, 's_{U_a}/mV':0, 'v':2, 's_v':2})

#print(df1.to_latex())
#print(df1)

# Widerstand R_2 = 1MOhm
data2 = 'Versuch_EL2/41-Data-4700kOhm.csv'
df2 = pd.read_csv(data2)

# Aufräumen der Tabelle
df2 = df2.sort_values(by='f/kHz', ascending=True)
df2.index = np.arange(1, len(df2)+1)

df2['f/Hz'] = df2['f/kHz'] * 1000

df2['U_a/mV'] = df2['U_a/Div']*df2['U_a(ein)/(mV/Div)']
df2['s_{U_a}/mV'] = df2['U_a(ein)/(mV/Div)'] * np.sqrt((0.03*df2['U_a/Div'])**2 + (1)**2)

df2['U_e/Div'] = 4.0
df2['U_e(ein)/(mV/Div)'] = 5
df2['U_e/mV'] = df2['U_e/Div']*df2['U_e(ein)/(mV/Div)']
df2['s_{U_e}/mV'] = df2['U_e(ein)/(mV/Div)'] * np.sqrt((0.03*df2['U_e/Div'])**2 + (1)**2)

df2['v'] = df2['U_a/mV']/df2['U_e/mV']
df2['s_v'] = np.sqrt((df2['s_{U_a}/mV']/df2['U_e/mV'])**2 + ((df2['s_{U_e}/mV']*df2['U_a/mV']/(df2['U_e/mV']**2))**2))

df2 = df2.drop(columns=['f/kHz', 'U_e/Div', 'U_e(ein)/(mV/Div)', 'U_a(ein)/(mV/Div)', 'U_a/Div'])
df2 = df2.round({'U_e/mV':0, 's_{U_e}/mV':0, 'U_a/mV':0, 's_{U_a}/mV':0, 'v':1, 's_v':1})
df2 = df2.drop(index=[13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
#print(df2.to_latex())
#print(df2)

# Plot
anzahl = 10000

x1 = df1['f/Hz']
y1, y1_err = df1['v'], df1['s_v']

x2 = df2['f/Hz']
y2, y2_err = df2['v'], df2['s_v']

# Curve Fit
def objective(x, a, b):
	return a/np.sqrt(1+(x/b)**2)

popt, _ = curve_fit(objective, x1, y1)
a1, b1 = popt
x1_line = np.linspace(x1.min(), x1.max(), anzahl)
y1_line = objective(x1_line, a1, b1)
#print(a1, -b1)

def objective(x, a, b):
	return a/np.sqrt(1+(x/b)**2)

popt, _ = curve_fit(objective, x2, y2)
a2, b2 = popt
x2_line = np.linspace(x2.min(), x2.max(), anzahl)
y2_line = objective(x2_line, a2, b2)
#print(a2, b2)

# Grenzfrequenz
x1_fgr, x1_c = np.linspace(10, 33.3e3, anzahl), np.repeat(100/np.sqrt(2), anzahl)
y1_fgr, y1_c = np.linspace(0.9, 100/np.sqrt(2), anzahl), np.repeat(33.3e3, anzahl) 

x2_fgr, x2_c = np.linspace(10, 6.7e3, anzahl), np.repeat(470/np.sqrt(2), anzahl)
y2_fgr, y2_c = np.linspace(0.9, 470/np.sqrt(2), anzahl), np.repeat(6.7e3, anzahl) 

plt.errorbar(x1,y1, yerr=y1_err, fmt='.', capsize=5, label=r'Messreihe - $R_{2,1}$')
plt.plot(x1_line, y1_line, color='r', label=r'Curve-Fit - $R_{2,1}$')
plt.plot(x1_fgr, x1_c, linestyle='--', color='r', label=r'$f_{gr,1}$')
plt.plot(y1_c, y1_fgr, linestyle='--', color='r')

plt.errorbar(x2,y2, yerr=y2_err, fmt='.', capsize=5, label=r'Messreihe - $R_{2,2}$')
plt.plot(x2_line, y2_line, color='green', label=r'Curve-Fit - $R_{2,2}$')
plt.plot(x2_fgr, x2_c, linestyle='--', color='green', label=r'$f_{gr,2}$')
plt.plot(y2_c, y2_fgr, linestyle='--', color='green')

plt.xlabel(r'$f$ in Hz')
plt.xscale('log')
plt.ylabel(r'$v$')
plt.yscale('log')
plt.legend()
#plt.show()

# VB Produkt

df1['f/kHz'] = df1['f/Hz']/1000
df1 = df1.drop(index=[1,2,3,4,5], columns=['f/Hz','U_e/mV', 's_{U_e}/mV', 'U_a/mV', 's_{U_a}/mV',])
df1.index = np.arange(1, len(df1)+1)

df1['s_f/kHz'] = np.sqrt(0.01**2+(4e-4*df1['f/kHz']+0.01)**2)
df1['v_B/kHz'] = df1['v']*df1['f/kHz']
df1['s_{v_B}/kHz'] = np.sqrt((df1['v']*df1['s_f/kHz'])**2+(df1['s_v']*df1['f/kHz'])**2)

print(df1.to_latex())
print(df1['v_B/kHz'].mean(), df1['s_{v_B}/kHz'].mean())

df2['f/kHz'] = df2['f/Hz']/1000
df2 = df2.drop(index=[1,2,3,4,5], columns=['f/Hz','U_e/mV', 's_{U_e}/mV', 'U_a/mV', 's_{U_a}/mV',])
df2.index = np.arange(1, len(df2)+1)

df2['s_f/kHz'] = np.sqrt(0.01**2+(4e-4*df2['f/kHz']+0.01)**2)
df2['v_B/kHz'] = df2['v']*df2['f/kHz']
df2['s_{v_B}/kHz'] = np.sqrt((df2['v']*df2['s_f/kHz'])**2+(df2['s_v']*df2['f/kHz'])**2)

print(df2.to_latex())
print(df2['v_B/kHz'].mean(), df2['s_{v_B}/kHz'].mean())