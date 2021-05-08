import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = 'Versuch_EL2/43-Data.csv'
df = pd.read_csv(data)

# Aufräumen der Tabelle
df = df.sort_values(by='f/kHz', ascending=True)
df.index = np.arange(1, len(df)+1)
df = df.drop(index=[1]) # Messwert 1 zu klein (Grund Ablesen schwierig)

df['U_e/V'] = 2.8
df['U_a/V'] = df['U_a/Div']*df['U_a(ein)/(V/Div)']
df['v'] = df['U_a/V']/df['U_e/V']

print(df)

x = df['f/kHz']
y = df['v']
fehler0 = df['v']*np.sqrt(2)*0.03

data = 'Versuch_EL2/42-Data.csv'
df = pd.read_csv(data)

# Aufräumen der Tabelle
df = df.sort_values(by='f/Hz', ascending=True)
df.index = np.arange(1, len(df)+1)
df = df.drop(index=[1]) # Messwert 1 zu klein (Grund Ablesen schwierig)

df['U_e/V'] = 0.05
df['U_a/V'] = df['U_a/Div']*df['U_a(ein)/(V/Div)']
df['v'] = df['U_a/V']/df['U_e/V']

print(df)

x1 = df['f/Hz']
y1 = df['v']
fehler1 = df['v']*np.sqrt(2)*0.03


plt.xlim(3,100000)
plt.scatter(x*1000,y, label = 'Umkehrdifferenzierer')
plt.scatter(x1,y1, label = 'Umkehrintegrator')
plt.errorbar(x*1000, y, yerr =fehler0*1000, fmt='None', color = 'b')
plt.xscale('log')
plt.yscale('log')


#Labeling
plt.title('Verstärkung des Umkehrintegrator/Differierer')
plt.xlabel('Frequenz in ')
plt.ylabel('Verstärkung $v$')
plt.legend()


plt.show()