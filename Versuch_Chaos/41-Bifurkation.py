import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')

data = "Versuch_Chaos/Daten/Pendel/3.1/BifurkationPendel.csv"
df = pd.read_csv(data)

#Berechnung
df = df.sort_values(by='Masse [g]')
df["Delta^2"] = (df["UAl [V]"] - df["UAr [V]"])**2

plt.plot(df["Masse [g]"],df["UAl [V]"], 'o', color='orange')
plt.plot(df["Masse [g]"],df["UAr [V]"], 'o', color='orange')
plt.xlabel(r'$M$ in g')
plt.ylabel(r'$U_a$ in V')
#plt.errorbar(df["Masse [g]"][7:],df["Delta^2"][7:], yerr=df["sUA"][7:], fmt='x', capsize=5)
plt.show()