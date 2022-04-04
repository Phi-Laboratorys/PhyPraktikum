import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = "Versuch_POL/41-Data.csv"
df = pd.read_csv(data)
df.index = np.arange(1, len(df)+1)

df = df.sort_values(by='phi/grad', ascending=True)

x = df['phi/grad']
yp, ys = df['Up/mV'], df['Us/mV']

plt.plot(x, yp, 'o')
plt.plot(x, ys, 'o')
plt.show()