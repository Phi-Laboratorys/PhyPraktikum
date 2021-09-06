import numpy as np
import pandas as pd
import matplotlib.pylab as plt

data = "Versuch_Chaos/Auswertung/Bifurkation1.csv"
df = pd.read_csv(data)

#Berechnung
df = df.sort_values(by='Masse [g]')
df["Delta^2"] = (df["UAl [V]"] - df["UAr [V]"])**2
print(df)

#Fehlerrechnung

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.errorbar(df["Masse [g]"][7:],df["Delta^2"][7:], yerr=df["sUA"][7:], fmt='x', capsize=5)
ax2.plot(df["Masse [g]"],df["UAl [V]"], 'o')
ax2.plot(df["Masse [g]"],df["UAr [V]"], 'o')
plt.show()




