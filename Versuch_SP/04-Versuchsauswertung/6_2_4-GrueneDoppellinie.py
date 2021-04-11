import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = ['Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_0,1mm.txt',
        'Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_0,2mm.txt',
        'Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_0,4mm.txt',
        'Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_0,6mm.txt',
        'Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_0,8mm.txt',
        'Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_1,0mm.txt',
        'Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_1,2mm.txt',
        'Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_1,4mm.txt',
        'Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_1,6mm.txt',
        'Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_1,8mm.txt',
        'Versuch_SP/04-Versuchsauswertung/6_2_4-Data/gruene_Hg-Linie_A4_2,0mm.txt']


df1 = pd.read_csv(data[0],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')
df2 = pd.read_csv(data[1],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')
df3 = pd.read_csv(data[2],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')
df4 = pd.read_csv(data[3],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')
df5 = pd.read_csv(data[4],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')
df6 = pd.read_csv(data[5],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')
df7 = pd.read_csv(data[6],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')
df8 = pd.read_csv(data[7],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')
df9 = pd.read_csv(data[8],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')
df10 = pd.read_csv(data[9],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')
df11 = pd.read_csv(data[10],sep='\t',encoding= 'Windows 1252', skiprows=(0,1), decimal=',')

#print(df1.keys())

# Verstärkung 316
x1, y1 = df1['Wellenlänge [Ä]  '], df1['Meßwert [mV]  ']*99.865/316
x2, y2 = df2['Wellenlänge [Ä]  '], df2['Meßwert [mV]  ']*99.865/316
x3, y3 = df3['Wellenlänge [Ä]  '], df3['Meßwert [mV]  ']*99.865/316
x4, y4 = df4['Wellenlänge [Ä]  '], df4['Meßwert [mV]  ']*99.865/316
x5, y5 = df5['Wellenlänge [Ä]  '], df5['Meßwert [mV]  ']*99.865/316
# Verstärkung 99,856
x6, y6 = df6['Wellenlänge [Ä]  '], df6['Meßwert [mV]  ']
x7, y7 = df7['Wellenlänge [Ä]  '], df7['Meßwert [mV]  ']
x8, y8 = df8['Wellenlänge [Ä]  '], df8['Meßwert [mV]  ']
x9, y9 = df9['Wellenlänge [Ä]  '], df9['Meßwert [mV]  ']
x10, y10 = df10['Wellenlänge [Ä]  '], df10['Meßwert [mV]  ']
x11, y11 = df11['Wellenlänge [Ä]  '], df11['Meßwert [mV]  ']


fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax.plot(x1,y1,label='0.1 mm')
ax.plot(x2,y2,label='0.2 mm')
ax.plot(x3,y3,label='0.4 mm')
ax.plot(x4,y4,label='0.6 mm')
ax.plot(x5,y5,label='0.8 mm')
ax.plot(x6,y6,label='1.0 mm')
ax.plot(x7,y7,label='1.2 mm')
ax.plot(x8,y8,label='1.4 mm')
ax.plot(x9,y9,label='1.6 mm')
ax.plot(x10,y10,label='1.8 mm')
ax.plot(x11,y11,label='2.0 mm')

#ax.set_title(r'$\omega_3$-$\omega_*$-Diagramm')
ax.set_xlabel(r'Wellenlänge in $\AA$')
ax.set_ylabel(r'Intensität$\cdot 10^{-3}$')
ax.legend()
plt.show()