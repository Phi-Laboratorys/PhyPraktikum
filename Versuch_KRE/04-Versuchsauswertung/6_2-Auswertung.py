# Auswertung 6.2 über Python zum reinkommen für später

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

df = pd.read_csv('./6_2-Nutation.csv')

x_new = np.linspace(df['w3 [1/s]'].min(), df['w3 [1/s]'].max(), 300)
#y_smooth = spline(df['w3 [1/s]'], df['wn/w3'],x_new)

spl = make_interp_spline(df['w3 [1/s]'], df['wn/w3'], k=3)  # type: BSpline
y_smooth = spl(x_new)

#plt.plot(df['w3 [1/s]'], df['wn/w3'])
plt.errorbar(df['w3 [1/s]'], df['wn/w3'], df['swn/w3'], fmt='o' ,marker='o', capsize=5)
plt.plot(x_new, y_smooth)
plt.show()