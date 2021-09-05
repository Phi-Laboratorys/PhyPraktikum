import numpy as np
import pandas as pd
import matplotlib.pylab as plt

data = "Versuch_Chaos/41-Test.csv"
df = pd.read_csv(data)

t0 = df['time [s]'][0]
U_max = df['U_a [V]'][0]

dt = []
i =  0

while i < len(df):
    
    if U_max < df['U_a [V]'][i]:
        U_max = df['U_a [V]'][i]
        
    if U_max > df['U_a [V]'][i]:
        dt.append(df['time [s]'][i-1] - t0)
        t0 = df['time [s]'][i-1]
        
    i += 1