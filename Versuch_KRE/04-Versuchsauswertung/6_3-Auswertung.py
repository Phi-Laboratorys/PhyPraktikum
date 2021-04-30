import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = 'Versuch_KRE/04-Versuchsauswertung/6_3-Praezession.csv'
df = pd.read_csv(data)
df.index = np.arange(1, len(df)+1)

s = 0
t_sum = []

for i in df['T']:
    s += i
    t_sum.append(s)

df['T_sum'] = t_sum

'''
x = df['T_sum']
y = df['f3_start']
plt.plot(x, y, 'o')

# Fit
model = np.polyfit(x,y,1)
predict = np.poly1d(model)
x_lin = np.linspace(x.min(),x.max(),300)
y_lin = predict(x_lin)
#plt.title(r'$f_{3_{start}}$-$t$-Diagramm')
plt.xlabel('$t$ in s')
plt.ylabel(r'$f_\mathregular{{3_{start}}}$ in Hz')
plt.plot(x_lin,y_lin, 'r')
plt.show()
'''

# Fehler
df['u_f3'] = u_f3 = 0.25
df['u_T'] = u_T = 0.2
df['u_w3'] = u_w3 = np.sqrt(2)*np.pi*u_f3

df['w3'] = np.pi*(df['f3_start'] + df['f3_end'])

df['wp'] = 2*np.pi/df['T']
df['u_wp'] = 2*u_T*np.pi/(df['T']**2)

df['w*'] = df['wp']*df['w3']
df['u_w*'] = np.sqrt((df['wp']*u_w3)**2+(df['w3']*df['u_wp'])**2)

# Runden + Anordnung
df = df.round({'u_w3':2, 'w3':2, 'wp':2, 'w*':2, 'u_w*':2, 'u_wp':5})
df = df[['f3_start', 'f3_end','u_f3', 'T', 'u_T', 'T_sum', 'w3', 'u_w3', 'wp', 'u_wp', 'w*', 'u_w*']]
df = df.drop(columns=['f3_start', 'f3_end','u_f3', 'T', 'u_T', 'T_sum'])

'''
plt.hist(df['w*'])
#plt.title(r'$\omega_*$-Histogramm')
plt.ylabel('Anzahl Messwerte')
plt.xlabel(r'$\omega_*$ in $\mathregular{\frac{1}{s^2}}$')
plt.show()
'''

# Selcting Data
df1 = df.loc[[2,5,9,11,14,17,18,20,21,22]]
df1.index = np.arange(1, len(df1)+1)
x1, x1_err = df1['w3'], df1['u_w3']
y1, y1_err = df1['w*'], df1['u_w*']

df2 = df.loc[[1,4,7,10,13]]
df2.index = np.arange(1, len(df2)+1)
x2, x2_err = df2['w3'], df2['u_w3']
y2, y2_err = df2['w*'], df2['u_w*']

df3 = df.loc[[3,6,8,12,15,16,19]]
df3.index = np.arange(1, len(df3)+1)
x3, x3_err = df3['w3'], df3['u_w3']
y3, y3_err = df3['w*'], df3['u_w*']

df4 = df.loc[[23,24,25,26]]
df4.index = np.arange(1, len(df4)+1)
x4, x4_err = df4['w3'], df4['u_w3']
y4, y4_err = df4['w*'], df4['u_w*']

'''
print(df1.to_latex())
print(df2.to_latex())
print(df3.to_latex())
print(df4.to_latex())
'''
# Für Messreihe 4
x, x_err = df['w3'], df['u_w3']
x_lin_4 = np.linspace(x.min(),x.max(),300)

# Ausschließen der Messreihe 4
df = df.drop(index=[23,24,25,26])
x, x_err = df['w3'], df['u_w3']
y, y_err = df['w*'], df['u_w*']
x_lin = np.linspace(x.min(),x.max(),300)
y_mean = np.repeat(y.mean(),300)

print(y.mean())
s=0
k = 0
for i in df['u_w*']:
    s += i**2
    k += 1   
y_mean_err = np.sqrt(s)/k

print(y_mean_err)

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax.errorbar(x1,y1,yerr=y1_err,fmt='o',capsize=5,label='Messreihe 1')
ax.errorbar(x2,y2,yerr=y2_err,fmt='o',capsize=5,label='Messreihe 2')
ax.errorbar(x3,y3,yerr=y3_err,fmt='o',capsize=5,label='Messreihe 3')
'''
ax.plot(x_lin,y_mean,linestyle='-',label='Mittelwert',color='r')
ax.plot(x_lin,y_mean+y_mean_err,linestyle='--',color='r')
ax.plot(x_lin,y_mean-y_mean_err,linestyle='--',color='r')
ax.fill_between(x_lin,y_mean+y_mean_err,y_mean-y_mean_err,color='r',alpha=0.1)
'''
# Mit Messreihe 4
ax.errorbar(x4,y4,yerr=y4_err,fmt='o',capsize=5,label='Messreihe 4',color='purple')
ax.plot(x_lin_4,y_mean,linestyle='-',label='Mittelwert',color='r')
ax.plot(x_lin_4,y_mean+y_mean_err,linestyle='--',color='r')
ax.plot(x_lin_4,y_mean-y_mean_err,linestyle='--',color='r')
ax.fill_between(x_lin_4,y_mean+y_mean_err,y_mean-y_mean_err,color='r',alpha=0.1)

#ax.set_title(r'$\omega_3$-$\omega_*$-Diagramm')
ax.set_xlabel(r'$\mathregular{\omega_3}$ in $\mathregular{\frac{1}{s}}$')
ax.set_ylabel(r'$\mathregular{\omega_*}$ in $\mathregular{\frac{1}{s^2}}$')
ax.legend()
plt.show()

#print(df)
'''
plt.hist(df['w*'])
#plt.title(r'$\omega_*$-Histogramm')
plt.ylabel('Anzahl Messwerte')
plt.xlabel(r'$\omega_*$ in $\mathregular{\frac{1}{s^2}}$')
plt.show()
'''