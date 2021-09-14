import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')

#Daten Aufg a)
datALoch = 'Versuch_REM/Daten/a/EDX/Loch.txt'
datAFlae = 'Versuch_REM/Daten/a/EDX/Oberflaeche.txt'
#Daten Aufg d)
datDD2 = 'Versuch_REM/Daten/d/EDX/Dunkel2.txt'
datDmW = 'Versuch_REM/Daten/d/EDX/DunklerfleckMitWei.txt'
datH1 = 'Versuch_REM/Daten/d/EDX/Hell1.txt'
datN1 = 'Versuch_REM/Daten/d/EDX/Normal1.txt'
#Daten Aufg e)
datE = 'Versuch_REM/Daten/e/EDX/chip.txt'



data = datALoch
df = pd.read_csv(data, delim_whitespace=True, skiprows=24)
#print(df.head())

fig, ax = plt.subplots()
ax.plot(df['Energie'], df['Impulse'], color='k')
ax.set(xlabel='Energie/keV', ylabel='cps/eV', xlim=(-0.49,10))
ax.grid()
plt.show()