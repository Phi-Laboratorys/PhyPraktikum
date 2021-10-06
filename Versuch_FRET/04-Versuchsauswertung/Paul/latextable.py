import numpy as np
import pandas as pd

dataKfCFP = 'Versuch_FRET/04-Versuchsauswertung/Paul/KF-CFP.csv'
dataKfYFP = 'Versuch_FRET/04-Versuchsauswertung/Paul/KF-YFP.csv'

data = dataKfCFP

df = pd.read_csv(data, decimal=',',sep=';')

#print(df.head())
print(df.to_latex(columns=['Zelle Nr.', 'D','S','beta'], index=False))