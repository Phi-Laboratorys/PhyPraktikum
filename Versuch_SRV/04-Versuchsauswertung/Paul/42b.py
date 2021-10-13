import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=15)

data = 'Versuch_SRV/Daten/42/b/05_10_2021_13_30_44_G11_sampling_42b_Dreieck_f3kHz_A1V_fs7kHz.dat'
df = pd.read_csv(data, skiprows=4, sep='\s+')

#print(df.head())

plt.plot(df['Fqscale-FFT'], df['y-FFTcurve'], 'k.')
plt.xlabel('$f$ in Hz')
plt.ylabel('Amplitude (dBV) 1V $U_{eff}$ = 1 dBV')
plt.show()