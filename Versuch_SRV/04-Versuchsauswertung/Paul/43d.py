import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=15)

data5 = 'Versuch_SRV/Daten/43/a/05_10_2021_14_49_52_G11_filtering_43a_Sinus_f100Hz_A1V_Rau_BW20MHz_AMD120pc_Fil_Bu_Lopa_Or5_Uf1k.dat'
data2 = 'Versuch_SRV/Daten/43/a/05_10_2021_14_50_05_G11_filtering_43a_Sinus_f100Hz_A1V_Rau_BW20MHz_AMD120pc_Fil_Bu_Lopa_Or2_Uf1k.dat'
data10 = 'Versuch_SRV/Daten/43/a/05_10_2021_14_50_57_G11_filtering_43a_Sinus_f100Hz_A1V_Rau_BW20MHz_AMD120pc_Fil_Bu_Lopa_Or10_Uf1k.dat'
data7 = 'Versuch_SRV/Daten/43/a/05_10_2021_14_51_17_G11_filtering_43a_Sinus_f100Hz_A1V_Rau_BW20MHz_AMD120pc_Fil_Bu_Lopa_Or7_Uf1k.dat'
data1 = 'Versuch_SRV/Daten/43/a/05_10_2021_14_49_03_G11_filtering_43a_Sinus_f100Hz_A1V_Rau_BW20MHz_AMD120pc_Fil_Bu_Lopa_Or1_Uf1k.dat'

df1 = pd.read_csv(data1, skiprows=3, sep='\s+')
df2 = pd.read_csv(data2, skiprows=3, sep='\s+')
df5 = pd.read_csv(data5, skiprows=3, sep='\s+')
df7 = pd.read_csv(data7, skiprows=3, sep='\s+')
df10 = pd.read_csv(data10, skiprows=3, sep='\s+')

dname = '43dOrdnung'
dateipfad = 'Versuch_SRV/Bilder/Paul/'

'''Plot Signal
t = 277
plt.figure(figsize=(12, 6), dpi=80)
plt.plot(df['time'].iloc[:t], df['y-generator'].iloc[:t], 'g--', label='Ungefiltert')
plt.plot(df['time'].iloc[:t], df['y-behind'].iloc[:t], 'k-', label='Gefiltert')
plt.xlabel('$t$ in ms')
plt.ylabel('y')
plt.legend()
#plt.savefig(dateipfad+dname+'S.pdf', bbox_inches = 'tight')
plt.show()
#'''

#'''Plot Fourie
df1 = df1.sort_values(by=['Fqscale-FFT'])
df2 = df2.sort_values(by=['Fqscale-FFT'])
df5 = df5.sort_values(by=['Fqscale-FFT'])
df7 = df7.sort_values(by=['Fqscale-FFT'])
df10 = df10.sort_values(by=['Fqscale-FFT'])
plt.figure(figsize=(12, 6), dpi=80)
plt.plot(df1['Fqscale-FFT'], df1['y-FFTcurve'], 'b-', label='1. Ordnung')
plt.plot(df2['Fqscale-FFT'], df2['y-FFTcurve'], 'g-', label='2. Ordnung')
plt.plot(df5['Fqscale-FFT'], df5['y-FFTcurve'], 'r-', label='5. Ordnung')
plt.plot(df7['Fqscale-FFT'], df7['y-FFTcurve'], 'm-', label='7. Ordnung')
plt.plot(df10['Fqscale-FFT'], df10['y-FFTcurve'], 'k-', label='10. Ordnung')
plt.xlabel('$f$ in Hz')
plt.ylabel(r'Amplitude (dBV) 1V $U_\mathrm{eff}$ = 1 dBV')
plt.xscale('log')
plt.legend()
plt.savefig(dateipfad+dname+'F.pdf', bbox_inches = 'tight')
plt.show()
#'''