import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

data = 'Versuch_Chaos/42-TeilauswertungPaul/AufgA.csv'
df = pd.read_csv(data)

def hyperbel(x,a,b,c):
    #return b((x**2)/(a**2)**0.5)
    return a/(c*x**3) + b

def fit(x,y):
    popt, _ = curve_fit(hyperbel, x, y)
    return popt


#print(df)
for i in range(0,7):
    x = [df['x1'][i], df['x2'][i],df['x3'][i]]
    y = [df['y1'][i], df['y2'][i],df['y3'][i]]
    #print(x)
    a, b, c = fit(x,y)
    x_line = np.linspace(10,100,100)
    y_line = hyperbel(x_line,a,b,c)
    plt.plot(x_line, y_line, label=df['Uebergang'][i])
    plt.plot(x,y,'.')

plt.ylim(6,20)
plt.legend()
plt.show()





print(df)