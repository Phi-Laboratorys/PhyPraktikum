import pandas as pd
import matplotlib.pyplot as plt

pfmr2 = '/Users/paul/Documents/GitHub/PPB-Kre/Kreisel/6.3/Messreihe2.csv'
pfmr3 = '/Users/paul/Documents/GitHub/PPB-Kre/Kreisel/6.3/Messreihe3.csv'

mr2 = pd.read_csv(pfmr2, index_col='Rund Nr.')
mr3 = pd.read_csv(pfmr3, index_col='Rund Nr.')

#Fehler
omega3Err = 0.01 #Hz
TErr = 0.01      #s
#mr2.loc[:,'Err'] = TErr
#mr3.loc[:,'Err'] = TErr

#Berechnung
mr2.loc[:,'prod'] = mr2.loc[:,'omega3'] / mr2.loc[:,'T']
mr3.loc[:,'prod'] = mr3.loc[:,'omega3'] / mr3.loc[:,'T']

mr2.loc[:,'prodErr'] = ( (omega3Err*(1/mr2.loc[:,'T']))**2 + ((1/(mr2.loc[:,'T'])**2) * TErr * mr2.loc[:,'omega3'])**2)**0.5
mr3.loc[:,'prodErr'] = ( (omega3Err*(1/mr3.loc[:,'T']))**2 + ((1/(mr3.loc[:,'T'])**2) * TErr * mr3.loc[:,'omega3'])**2)**0.5

'''
print('Messreihe 2:')
print(mr2)

print('Messreihe 3:')
print(mr3)
#'''

alldata = pd.concat([mr2.loc[:,'prod'],mr3.loc[:,'prod']])
#print(type(mr2.loc[:,'prod']))
mw = alldata.mean()


alldata = pd.DataFrame(data={'prod':alldata})
#stat Fehler
alldata.loc[:,'qd'] = (alldata.loc[:,'prod'] - mw)**2   #Quadrat differenz
n = alldata.shape[0]                                    #Anzahl Messwerte
var = (1/(n-1)) * alldata.loc[:,'qd'].sum()             #Varianz
s = (var/n)**0.5
print('Mittelwert: m = ', mw)
print('Stanartabweichung: s = ', s)

fig, p2 = plt.subplots()
'''
p1.errorbar(mr2.loc[:,'omega3'], mr2.loc[:,'prod'], yerr=mr2.loc[:,'prodErr'], label='Messreihe 2', marker='.', linestyle='none', color='black')
p1.errorbar(mr3.loc[:,'omega3'], mr3.loc[:,'prod'], yerr=mr3.loc[:,'prodErr'], label='Messreihe 3', marker='.', linestyle='none', color='gray')
p1.legend()
p1.set_xlabel('$\omega_3$ in Hz')
p1.set_ylabel('$\omega_3$$\omega_p$ / Hz$^2$')
p1.set_title('$\omega_3$$\omega_p$ gegen $\omega_3$')
#'''

#'''
p2.hist(alldata.loc[:,'prod'],5, color='gray')
p2.set_xlabel('$\omega_3$$\omega_p$ / Hz$^2$')
p2.set_ylabel('# Messpunkte')
p2.set_title('Histogramm')
#'''
plt.show()