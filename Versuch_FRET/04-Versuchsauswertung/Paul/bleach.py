import numpy as np
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=20)

# Data import
path = 'Versuch_FRET/Daten/bleach-data/csv/'
data_files = os.listdir(path)
data_files.sort()
data_files.remove('.DS_Store')
#print(data_files)

df = pd.DataFrame(columns=['Name', ''])

string = 'S'

for d in data_files:
    
    if d.find(string) == -1:
        print(d)
        #data = [path + '/' + i for i in data_files]
        #df = pd.read_csv(d, skiprows=1)

    
    
