import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')


data37 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=37kO/06_09_2021_19_25_22_G11_shinriki_0.dat'
data39 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=39kO/06_09_2021_19_28_22_G11_shinriki_0.dat'
data40 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=40kO/06_09_2021_19_29_53_G11_shinriki_0.dat'
data45 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=45kO/06_09_2021_19_31_20_G11_shinriki_0.dat'
data60 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=60kO/06_09_2021_19_32_51_G11_shinriki_0.dat'
data66 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=66kO/06_09_2021_19_34_38_G11_shinriki_0.dat'
data70 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=70kO/06_09_2021_19_36_25_G11_shinriki_0.dat'
df = pd.read_csv(data, delim_whitespace=True, skiprows=7, decimal=',')

#print(df.head())

x=df['V1(V)'][0:100]
y=df['V2(V)'][0:100]
z=df['V3(V)'][0:100]

ax = plt.figure().add_subplot(projection='3d')
ax.plot(x, y, z, label='parametric curve')
ax.legend()
#ax.xlabel('$V_1$ in V')
#ax.ylabel('$V_2$ in V')
#ax.zlabel('$V_3$ in V')
#ax.subplots_adjust(bottom=0.5)



plt.show()