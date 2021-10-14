import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=15)



dataBuLo1 = 'Versuch_SRV/Daten/43/b/05_10_2021_15_02_04_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_Bu_Lopa_Or1_Uf1k.dat'
dataBuHi1 = 'Versuch_SRV/Daten/43/b/05_10_2021_15_02_51_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_Bu_Hipa_Or1_Uf1k.dat'
dataInChLo1 = 'Versuch_SRV/Daten/43/b/05_10_2021_15_06_57_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_InCh_Lopa_Or1_Uf1k.dat'
dataInChHi1 = 'Versuch_SRV/Daten/43/b/05_10_2021_15_07_48_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_InCh_Hipa_Or1_Uf1k.dat'

data = dataInChHi1
df = pd.read_csv(data, skiprows=3, sep='\s+')

dname = '43bInChHi1'
dateipfad = 'Versuch_SRV/Bilder/Paul/'

#'''Plot Signal
t = 2500
plt.figure(figsize=(12, 6), dpi=80)
plt.plot(df['time'].iloc[:t], df['y-generator'].iloc[:t], 'g--', label='Ungefiltert')
plt.plot(df['time'].iloc[:t], df['y-behind'].iloc[:t], 'k-', label='Gefiltert')
plt.xlabel('$t$ in ms')
plt.ylabel('y')
plt.legend()
plt.savefig(dateipfad+dname+'S.pdf', bbox_inches = 'tight')
plt.show()
#'''

#'''Plot Fourie
df = df.sort_values(by=['Fqscale-FFT'])
plt.figure(figsize=(12, 6), dpi=80)
plt.plot(df['Fqscale-FFT'], df['y-FFTcurve'], 'k-')
plt.xlabel('$f$ in Hz')
plt.ylabel(r'Amplitude (dBV) 1V $U_\mathrm{eff}$ = 1 dBV')
plt.xscale('log')
plt.savefig(dateipfad+dname+'F.pdf', bbox_inches = 'tight')
plt.show()
#'''