import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

x = df['f/Hz']
y = df['v']

plt.scatter(x,y)
plt.xscale('log')
plt.yscale('log')
plt.show()