import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=15)



dataRoh = 'Versuch_SRV/Daten/43/d/05_10_2021_15_48_11_G11_filtering_43d_Rechteck_f1kHz_A1V_Rau_BW20MHz_AMD70pc_Roh.dat'
dataLf500Hf1500 = 'Versuch_SRV/Daten/43/d/05_10_2021_15_49_43_G11_filtering_43d_Rechteck_f1kHz_A1V_Rau_BW20MHz_AMD70pc_DigiFil_Bu_Bapa_Or4_Lf500Hz_Uf1500Hz.dat'
dataLf700Hf1300 = 'Versuch_SRV/Daten/43/d/05_10_2021_15_52_43_G11_filtering_43d_Rechteck_f1kHz_A1V_Rau_BW20MHz_AMD70pc_DigiFil_Bu_Bapa_Or4_Lf700Hz_Uf1300Hz.dat'
dataLf10mHz55kHz = 'Versuch_SRV/Daten/43/d/05_10_2021_16_04_08_G11_filtering_43d_Rechteck_f1kHz_A1V_Rau_BW20MHz_AMD70pc_DigiFil_Bu_Bapa_Or4_Lf10mHz_Uf55kHz.dat'


data = dataLf10mHz55kHz
df = pd.read_csv(data, skiprows=3, sep='\s+')

dname = '43cLf10mHz55kHz'
dateipfad = 'Versuch_SRV/Bilder/Paul/'

#'''Plot Signal
t = 277
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