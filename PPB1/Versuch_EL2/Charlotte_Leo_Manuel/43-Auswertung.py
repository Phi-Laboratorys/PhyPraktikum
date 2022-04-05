import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Messreihe Integrator
data1 = 'Versuch_EL2/42-Data.csv'
df1 = pd.read_csv(data1)

# Aufräumen der Tabelle
df1 = df1.sort_values(by='f/Hz', ascending=True)
df1.index = np.arange(1, len(df1)+1)
df1 = df1.drop(index=[1]) # Messwert 1 zu klein (Grund Ablesen schwierig)

#df['s_f/Hz'] = df['f/Hz']*0.0004 + 0.01
df1['s_a/Div'] = [0.1, 0.1, 0.1, 0.1, 
                 0.1, 0.1, 0.1, 0.1, 0.1, 
                 0.1, 0.1, 0.1, 0.1, 0.1, 
                 0.1, 0.1, 0.1, 0.5, 0.5,
                 0.5, 0.5, 0.5, 0.5, 0.5]

df1['U_a/V'] = df1['U_a/Div']*df1['U_a(ein)/(V/Div)']
df1['s_{U_a}/V'] = df1['U_a(ein)/(V/Div)'] * np.sqrt((0.03*df1['U_a/Div'])**2 + (df1['s_a/Div'])**2)

df1['U_e/Div'] = 5.0
df1['U_e(ein)/(V/Div)'] = 0.010
df1['U_e/V'] = df1['U_e/Div'] * df1['U_e(ein)/(V/Div)']
df1['s_{U_e}/V'] = df1['U_e(ein)/(V/Div)'] * np.sqrt((0.03*df1['U_e/Div'])**2 + (0.1)**2)

df1['v'] = df1['U_a/V']/df1['U_e/V']
df1['s_v'] = np.sqrt((df1['s_{U_a}/V']/df1['U_e/V'])**2 + ((df1['s_{U_e}/V']*df1['U_a/V']/(df1['U_e/V']**2))**2))

df1 = df1.drop(columns = ['s_a/Div', 'U_e/Div', 'U_e(ein)/(V/Div)', 'U_a(ein)/(V/Div)', 'U_a/Div'])
df1 = df1.round({'U_e/V':3, 's_{U_e}/V':3, 'U_a/V':3, 's_{U_a}/V':3, 'v':2, 's_v':2})

#print(df.to_latex())

#Theorie
anzahl = 100000
R1, R2, C2, w = np.repeat(10e3, anzahl), np.repeat(1e6, anzahl), np.repeat(10e-9, anzahl), np.linspace(1, 100000, anzahl)
v = R2/R1 * 1/np.sqrt(1+(2*np.pi*w*R2*C2)**2)

x1_T, y1_T = w, v
x_fgr, x_c = np.linspace(1, 1/(10e3*10e-9*2*np.pi), anzahl), np.repeat(1, anzahl)
y_fgr, y_c = np.linspace(0.005, 1, anzahl), np.repeat(1/(10e3*10e-9*2*np.pi), anzahl) 

x1 = df1['f/Hz']
y1, y1_err = df1['v'], df1['s_v']

# Messreihe Bandpass
data2 = 'Versuch_EL2/43-Data.csv'
df2 = pd.read_csv(data2)

# Aufräumen der Tabelle
df2 = df2.sort_values(by='f/kHz', ascending=True)
df2.index = np.arange(1, len(df2)+1)

df2['f/Hz'] = df2['f/kHz'] * 1000

df2['U_a/V'] = df2['U_a/Div']*df2['U_a(ein)/(V/Div)']
df2['s_{U_a}/V'] = df2['U_a(ein)/(V/Div)'] * np.sqrt((0.03*df2['U_a/Div'])**2 + (0.1)**2)

df2['U_e/Div'] = 2.8
df2['U_e(ein)/(V/Div)'] = 1.0
df2['U_e/V'] = df2['U_e/Div']*df2['U_e(ein)/(V/Div)']
df2['s_{U_e}/V'] = df2['U_e(ein)/(V/Div)'] * np.sqrt((0.03*df2['U_e/Div'])**2 + (0.1)**2)

df2['v'] = df2['U_a/V']/df2['U_e/V']
df2['s_v'] = np.sqrt((df2['s_{U_a}/V']/df2['U_e/V'])**2 + ((df2['s_{U_e}/V']*df2['U_a/V']/(df2['U_e/V']**2))**2))

df2 = df2.drop(columns=['f/kHz', 'U_e/Div', 'U_e(ein)/(V/Div)', 'U_a(ein)/(V/Div)', 'U_a/Div'])
df2 = df2.round({'f/Hz':0 , 'U_e/V':2, 's_{U_e}/V':2, 'U_a/V':3, 's_{U_a}/V':3, 'v':3, 's_v':3})

#print(df2.to_latex())
#Theorie
R1, R2, C1, C2, f = np.repeat(1e3, anzahl), np.repeat(10e3, anzahl), np.repeat(10e-9, anzahl),  np.repeat(1e-9, anzahl), np.linspace(10, 1000000, anzahl)
v = 1/np.sqrt((R1/R2+C2/C1)**2+(2*np.pi*f*R1*C2-1/(2*np.pi*f*R2*C1))**2)

x2_T, y2_T = f, v

x2 = df2['f/Hz']
y2 , y2_err = df2['v'], df2['s_v']

plt.errorbar(x1, y1, yerr=y1_err, fmt='.', capsize=5, label = 'Messreihe - Integrator')
plt.plot(x1_T, y1_T, label='Theorie - Integrator')

plt.errorbar(x2, y2, yerr=y2_err, fmt='.', capsize = 5, label='Messreihe - Bandpass')
plt.plot(x2_T, y2_T, label='Theorie - Bandpass', color='purple')

plt.plot(x_fgr, x_c, linestyle = '--', label = r'$f_{T}$', color ='r')
plt.plot(y_c, y_fgr, linestyle = '--', color = 'r')

plt.xlabel(r'$f$ in Hz')
plt.xscale('log')
plt.ylabel(r'$v$')
plt.yscale('log')
plt.legend()
plt.show()