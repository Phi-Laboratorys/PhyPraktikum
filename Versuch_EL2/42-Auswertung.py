import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Messreihe
data = 'Versuch_EL2/42-Data.csv'
df = pd.read_csv(data)

# Aufräumen der Tabelle
df = df.sort_values(by='f/Hz', ascending=True)
df.index = np.arange(1, len(df)+1)
df = df.drop(index=[1]) # Messwert 1 zu klein (Grund Ablesen schwierig)

#df['s_f/Hz'] = df['f/Hz']*0.0004 + 0.01
df['s_a/Div'] = [0.1, 0.1, 0.1, 0.1, 
                 0.1, 0.1, 0.1, 0.1, 0.1, 
                 0.1, 0.1, 0.1, 0.1, 0.1, 
                 0.1, 0.1, 0.1, 0.5, 0.5,
                 0.5, 0.5, 0.5, 0.5, 0.5]

df['U_a/V'] = df['U_a/Div']*df['U_a(ein)/(V/Div)']
df['s_{U_a}/V'] = df['U_a(ein)/(V/Div)'] * np.sqrt((0.03*df['U_a/Div'])**2 + (df['s_a/Div'])**2)

df['U_e/Div'] = 5.0
df['U_e(ein)/(V/Div)'] = 0.010
df['U_e/V'] = df['U_e/Div'] * df['U_e(ein)/(V/Div)']
df['s_{U_e}/V'] = df['U_e(ein)/(V/Div)'] * np.sqrt((0.03*df['U_e/Div'])**2 + (0.1)**2)

df['v'] = df['U_a/V']/df['U_e/V']
df['s_v'] = np.sqrt((df['s_{U_a}/V']/df['U_e/V'])**2 + ((df['s_{U_e}/V']*df['U_a/V']/(df['U_e/V']**2))**2))

df = df.drop(columns = ['s_a/Div', 'U_e/Div', 'U_e(ein)/(V/Div)', 'U_a(ein)/(V/Div)', 'U_a/Div'])
df = df.round({'U_e/V':3, 's_{U_e}/V':3, 'U_a/V':3, 's_{U_a}/V':3, 'v':2, 's_v':2})

#print(df.to_latex())

#Theorie
anzahl = 10000
R1, R2, C2, w = np.repeat(10e3, anzahl), np.repeat(1e6, anzahl), np.repeat(10e-9, anzahl), np.linspace(1, 10000, anzahl)
v = R2/R1 * 1/np.sqrt(1+(2*np.pi*w*R2*C2)**2)

x_T, y_T = w, v
x_fgr, x_c = np.linspace(1, 1/(1e6*10e-9*2*np.pi), anzahl), np.repeat(100/np.sqrt(2), anzahl)
y_fgr, y_c = np.linspace(0.15, 100/np.sqrt(2), anzahl), np.repeat(1/(1e6*10e-9*2*np.pi), anzahl) 

x = df['f/Hz']
y, y_err = df['v'], df['s_v']

plt.errorbar(x, y, yerr=y_err, fmt='.', capsize=5, label = 'Messreihe')
plt.plot(x_T, y_T, label='Theorie')
plt.plot(x_fgr, x_c, linestyle = '--', label = r'$f_{i,gr}$', color ='r')
plt.plot(y_c, y_fgr, linestyle = '--', color = 'r')
plt.xlabel(r'$f$ in Hz')
plt.xscale('log')
plt.ylabel(r'$v$')
plt.yscale('log')
plt.legend()
plt.show()