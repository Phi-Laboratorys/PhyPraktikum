import pandas as pd

daten = 'Versuch_Alpha_Gamma_Spektroskopie/Daten/Rohdaten/SchichtdickeLeer1.RPT'

#Daten importiernen
df = pd.read_csv(daten,delimiter='\\', skiprows= 10, names=['Kanal', 'Dump', 'Count'])
del df['Dump']

#Umwandlung Energie
new_col = df['Kanal']*1483093.9468923 -1386750.67404823
df.insert(loc = 0, column = 'Energie', value = new_col) 

del df['Kanal']


#Wieder schreiben
daten = daten.replace('RPT', 'csv')
df.to_csv(daten, index= False)


