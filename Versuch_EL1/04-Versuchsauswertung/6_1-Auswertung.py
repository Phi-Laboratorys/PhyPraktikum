import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from scipy.optimize import curve_fit

data = 'Versuch_EL1/04-Versuchsauswertung/6_1-Messwerte.csv'

# Select Data1
df1 = pd.read_csv(data)
df1.index = np.arange(1, len(df1)+1)
df1 = df1.round({'s_(I_B)':2, 's_(U_BE)':3})

'''
# Plot Data1
x, x_err = df1['U_BE'], df1['s_(U_BE)']
y, y_err = df1['I_B'], df1['s_(I_B)']

# Interpolation
x_new = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=3)  # type: BSpline
y_smooth = spl(x_new)

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax.errorbar(x,y,yerr=y_err,fmt='o',capsize=5,label='Messreihe')
ax.plot(x_new, y_smooth, color='r', label='Spline-Interpolation 3. Grades')
#ax.set_title(r'$$-$\omega_*$-Diagramm')
ax.set_ylabel(r'$I_B$ in mA')
ax.set_xlabel(r'$U_{BE}$ in V')
ax.legend()
plt.show()
'''

# Select Data2
x, x_err = df1['I_B'], df1['s_(I_B)']
y, y_err = df1['U_BE'], df1['s_(U_BE)']

df2 = pd.DataFrame() 

# Fehler
i = 1
rBE, s_rBE = [], []
di, s_di = [], []
du, s_du = [], []

while i < len(x):
    rBE.append((y[i+1]-y[i])/(x[i+1]-x[i]))
    di.append(x[i+1]-x[i])
    du.append(y[i+1]-y[i])
    s_di.append(np.sqrt(x_err[i+1]**2+x_err[i]**2))
    s_du.append(np.sqrt(y_err[i+1]**2+y_err[i]**2))
    i += 1   

df2['d_(I_B)'] = di
df2['s_(d_(I_B))'] = s_di
df2['d_(U_BE)'] = du
df2['s_(d_(U_BE))'] = s_du
df2['r_BE'] = rBE
df2['s_(r_BE)'] = np.sqrt((df2['s_(d_(U_BE))']/df2['d_(I_B)'])**2 + 
                          ((df2['d_(U_BE)']/df2['d_(I_B)'])*(df2['s_(d_(I_B))']/df2['d_(I_B)']))**2)

df2.index = np.arange(1, len(df2)+1)
df1 = df1.drop([39]) 
df2['I_B'] = df1['I_B']

# Plot Data2
x, x_err = df1['I_B'], df1['s_(I_B)']
y, y_err = df2['r_BE'], df2['s_(r_BE)']

# Excluding oversized Data
y_err[0:4] = 0

# Curve Fit
def objective(x, a, b):
	return a/x + b

popt, _ = curve_fit(objective, x, y)
a, b = popt
x_line = np.linspace(x.min(), x.max(), 300)
y_line = objective(x_line, a, b)
print(a, b)

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax.errorbar(x,y,yerr=y_err,fmt='o',capsize=3,label='Messreihe')
ax.plot(x_line, y_line, color='r', 
        label='Curve-Fit\n' + r'$f(x)=\frac{a}{x}+b$' + '\n' +'a = 0.01891727051649630\nb = 0.02821377849572285')
#ax.set_title(r'$$-$\omega_*$-Diagramm')
ax.set_xlabel(r'$I_B$ in mA')
ax.set_ylabel(r'$r_{BE}$ in k$\Omega$')
ax.legend()
plt.show()
