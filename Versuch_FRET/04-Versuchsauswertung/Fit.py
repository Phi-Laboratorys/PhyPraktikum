import numpy as np
from numpy.lib.function_base import append
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
from pandas.core.algorithms import diff
from scipy.signal import argrelextrema
import scipy.constants as const

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=18)

# Data import
path = 'Versuch_FRET/Daten/TCSPC-data'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files]
data.sort()

data_CFP = [i for i in data if 'CFP' in i]
data_YFP = [i for i in data if 'YFP' in i]
data_CY = [i for i in data if 'CY' in i]
data_IRF = [i for i in data if 'IRF' in i]

for i in data_IRF:
    df = pd.read_csv(i, delim_whitespace=True)
    df = df['N(t)'][70:200]
    
for j in data_CFP:
    df = pd.read_csv(j, delim_whitespace=True, skiprows=11, encoding='Windows 1252')
    print(df)