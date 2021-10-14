import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=15)



dataBuLo1 = 'Versuch_SRV/Daten/43/b/05_10_2021_15_02_04_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_Bu_Lopa_Or1_Uf1k.dat'

data = dataBuLo1
df = pd.read_csv(data, skiprows=3, sep='\s+')

'''Plot Signal
t = 1000
plt.figure(figsize=(12, 6), dpi=80)
plt.plot(df['time'].iloc[:t], df['y-generator'].iloc[:t], 'k-')
plt.xlabel('$t$ in s')
plt.ylabel('y')
plt.show()
#'''

#'''Plot Fourie
df = df.sort_values(by=['Fqscale-FFT'])
plt.figure(figsize=(12, 6), dpi=80)
plt.plot(df['Fqscale-FFT'], df['y-FFTcurve'], 'k-')
plt.xlabel('$f$ in Hz')
plt.ylabel('Amplitude (dBV) 1V $U_{eff}$ = 1 dBV')
plt.xscale('log')
plt.show()
#'''