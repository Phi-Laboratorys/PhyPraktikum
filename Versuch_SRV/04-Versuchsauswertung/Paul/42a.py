import numpy as np
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=15)

data1 = 'Versuch_SRV/04-Versuchsauswertung/Paul/42a1.csv'
data2 = 'Versuch_SRV/04-Versuchsauswertung/Paul/42a2.csv'
data = data1
df = pd.read_csv(data)

#print(df.head())
plt.figure(figsize=(12, 6), dpi=80)
plt.plot(df['$f_{Abtast}$ in kHz'], df['$f_{Mes} in kHz$'], 'k.', label='Messpunkte')
plt.plot([40,40], [0,21], linestyle='--', color='gray', label='r$f_\mathrm{crit}$')
plt.xlabel(r'$f_\mathrm{Abtast}$ in kHz')
plt.ylabel(r'$f_\mathrm{Mess}$ in kHz')
plt.legend()
plt.savefig('Versuch_SRV/Bilder/Paul/42a1.pdf', bbox_inches = 'tight')
plt.show()