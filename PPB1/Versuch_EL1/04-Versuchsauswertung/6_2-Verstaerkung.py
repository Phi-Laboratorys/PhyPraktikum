import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = 'Versuch_EL1/04-Versuchsauswertung/6_2-Verstaerkung.csv'
df = pd.read_csv(data)

x = df['I_B']
y, y_err = df['B'], df['s_B']
#z = df['I_C']

print(df.keys())

plt.errorbar(x, y, yerr=y_err, fmt='o', capsize=5)
plt.xlabel(r'$I_B$ in mA')
plt.ylabel(r'$B$')
plt.show()