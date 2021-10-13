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

plt.plot(df['$f_{Abtast}$ in kHz'], df['$f_{Mes} in kHz$'], 'k.', label='Messpunkte')
plt.plot([40,40], [0,21], linestyle='--', color='gray', label='$f_{crit}$')
plt.xlabel('$f_{Abtast}$ in kHz')
plt.ylabel('$f_{Mes}$ in kHz')
plt.legend()
plt.show()