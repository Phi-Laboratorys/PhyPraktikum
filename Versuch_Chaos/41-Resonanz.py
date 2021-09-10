import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')

data = 'Versuch_Chaos/Daten/Pendel/3.2b/06_09_2021_14_30_52_06_09_2021_14_30_52_G11_pendel_resonanz__0.dat'
df = pd.read_csv(data, delim_whitespace=True, skiprows=6, decimal=',')
df = df.dropna()

#x_up, y_up = df['xup(f)'][0:1153], df['yup(V)'][0:1153]
#x_do, y_do = df['xdown(f)'][0:1125], df['ydown(V)'][0:1125]

x_up, y_up = df['xup(f)'], df['yup(V)']
x_do, y_do = df['xdown(f)'], df['ydown(V)']

plt.plot(2*np.pi*x_up,y_up,'.',label=r'$0$ Hz $\rightarrow 1,1$ Hz')
plt.plot(2*np.pi*x_do,y_do,'.',label=r'$1,1$ Hz $\rightarrow 0$ Hz')
plt.xlabel(r'$\omega = 2 \pi f$ in Hz',size=12)
plt.ylabel(r'$b$ in V',size=12)
plt.legend()
plt.show()