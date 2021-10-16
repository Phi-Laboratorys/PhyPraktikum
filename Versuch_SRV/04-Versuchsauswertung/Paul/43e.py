import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=15)

dataASin = 'Versuch_SRV/Daten/43/c/05_10_2021_15_26_32_G11_filtering_43c_Sinus_f2kHz_A1V_AnalFil_Bu_Bapa_Or1_Lf1kHz_Uf4kHz.dat'
dataDSin = 'Versuch_SRV/Daten/43/c/05_10_2021_15_28_23_G11_filtering_43c_Sinus_f2kHz_A1V_DigiFil_Bu_Bapa_Or1_Lf1kHz_Uf4kHz.dat'
dataARe = 'Versuch_SRV/Daten/43/c/05_10_2021_15_27_23_G11_filtering_43c_Rechteck_f2kHz_A1V_AnalFil_Bu_Bapa_Or1_Lf1kHz_Uf4kHz.dat'
dataDRe = 'Versuch_SRV/Daten/43/c/05_10_2021_15_28_55_G11_filtering_43c_Rechteck_f2kHz_A1V_DigiFil_Bu_Bapa_Or1_Lf1kHz_Uf4kHz.dat'

df1 = pd.read_csv(dataDRe, skiprows=3, sep='\s+')
df2 = pd.read_csv(dataARe, skiprows=3, sep='\s+')


dname = '43eAD'
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

plt.figure(figsize=(12, 6), dpi=80)
#plt.plot(df1['Fqscale-filter'], df1['y-filtercurve'], 'k--', label='digitale Filterung Simu')
plt.plot(df1['Fqscale-FFT'], df1['y-FFTcurve'], 'k-', label='digitale Filterung')
plt.plot(df2['Fqscale-FFT'], df2['y-FFTcurve'], 'b-', label='analoge Filterung')

plt.xlabel('$f$ in Hz')
plt.ylabel(r'Amplitude (dBV) 1V $U_\mathrm{eff}$ = 1 dBV')
plt.xscale('log')
plt.legend()
plt.savefig(dateipfad+dname+'F.pdf', bbox_inches = 'tight')
plt.show()
#'''