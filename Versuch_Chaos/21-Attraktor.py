# Source: http://jupiter-online.net/roessler-attraktor-zeichnen-mit-matplotlib/
# Module importieren
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D

'''Roessler Attraktor'''
# Funktion zur Berechnung des Rössler Attraktors
def roessler(x, y, z, a=0.2, b=0.2, c=5.7):
    dx = -(y + z)
    dy = x + a * y
    dz = b + z * (x - c)
    return dx, dy, dz

# Schrittweite und Anzahl der Schritte definieren
dt = 0.01
numSteps = 20000
 
# Arrays für x, y und z Werte initialisieren
X = np.zeros(numSteps + 1)
Y = np.zeros(numSteps + 1)
Z = np.zeros(numSteps + 1)
 
# Starwerte festlegen
X[0], Y[0], Z[0] = (0, 0, 0)

# x, y und z Positionen Schrittweise berechnen
for i in range(numSteps):
    dx, dy, dz = roessler(X[i], Y[i], Z[i])
    X[i + 1] = X[i] + (dx * dt)
    Y[i + 1] = Y[i] + (dy * dt)
    Z[i + 1] = Z[i] + (dz * dt)
    
# Figur erzeugen und 3D Projektion aktivieren
rc('text', usetex=True)
rc('font', family='serif')

fig = plt.figure()
#fig.suptitle("Seltsame Attraktoren")
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
       
# Diagram beschriften
ax1.plot(X, Y, Z, lw=0.5)
ax1.set_xlabel("X Achse")
ax1.set_ylabel("Y Achse")
ax1.set_zlabel("Z Achse")
ax1.set_title("Rössler Attraktor")

'''Lorentz Attraktor'''
# Source: http://jupiter-online.net/lorenz-attraktor-zeichnen-mit-matplotlib/
# Schrittweite und Anzahl der Schritte definieren
step = 0.01
numSteps = 10000
 
# Konstanten für Berechnung der Ableitungen definieren
a, b, c = 10, 28, 8/3
 
# Arrays für x, y und z Werte initialisieren
x = np.zeros(numSteps+1)
y = np.zeros(numSteps+1)
z = np.zeros(numSteps+1)
 
# Starwerte festlegen
x[0], y[0], z[0] = 1.0, 1.0, 1.0

# x, y und z Positionen berechnen
for i in range(numSteps):
    x[i+1] = x[i] + (step * (a * (y[i] - x[i])))
    y[i+1] = y[i] + (step * (b * x[i] - y[i] - x[i] * z[i]))
    z[i+1] = z[i] + (step * (x[i]*y[i] - c*z[i]))
 
# 3D Projektion aktivieren
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# Diagramm beschriften
ax2.plot(x, y, z, lw=1.0)
ax2.set_xlabel("X Achse")
ax2.set_ylabel("Y Achse")
ax2.set_zlabel("Z Achse")
ax2.set_title("Lorenz Attraktor")
 
# Bild anzeigen
plt.show()