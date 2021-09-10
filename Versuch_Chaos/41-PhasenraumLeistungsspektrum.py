import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')

data = ['Versuch_Chaos/Daten/Pendel/3.3a/0,165Hz/06_09_2021_17_14_32_Richter_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,198Hz/06_09_2021_17_12_04_Richter_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,233Hz/06_09_2021_17_09_31_Richter_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,411Hz/06_09_2021_16_59_35_Richter_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,411Hz/06_09_2021_17_01_56_Richter_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,733Hz/06_09_2021_16_44_55_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,847Hz/06_09_2021_16_00_06_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,882Hz/06_09_2021_15_56_30_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,939Hz/06_09_2021_16_36_11_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/1,000Hz/06_09_2021_16_31_30_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/1,201Hz/06_09_2021_15_48_53_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/1,499Hz/06_09_2021_16_18_06_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/1,702Hz/06_09_2021_16_15_44_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/1,802Hz/06_09_2021_16_13_46_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/2,100Hz/06_09_2021_16_11_42_G11_pendel_0.dat']

for i in data:
    df = pd.read_csv(i, delim_whitespace=True, skiprows=7, decimal=',')
    df = df.dropna()
    
    x_p, y_p = df['Ua(V)'], df['-dUa/dt(V)']
    x_s, y_s1, y_s2 = df.loc[(df>0).any(axis=1)].index, df.loc[(df>0).any(axis=1)]['DFT-Ua(V)'], df.loc[(df>0).any(axis=1)]['DFT-dUa/dt(V)']
    
    print(df)

    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.plot(x_p, y_p)
    ax2.scatter(x_s, y_s1)
    plt.show()
