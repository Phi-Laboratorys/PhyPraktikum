import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importieren der Daten
data = pd.read_csv("test.csv", header = 0)
print (data)



#Create axes and figure
a = np.array([[1,2,3],[4,5,6]])
aasarray = np.asarray(a)
fig, ax = plt.subplots()
ax.plot([1,2],aasarray)
plt.show()

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.


