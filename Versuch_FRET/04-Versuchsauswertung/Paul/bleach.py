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
data = [path + '/' + i for i in data_files]
data.sort()
#print(data)