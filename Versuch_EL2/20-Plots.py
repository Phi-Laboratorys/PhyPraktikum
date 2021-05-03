import numpy as np
import matplotlib.pyplot as plt


anzahl = 300
x = np.linspace(1/10, 10, anzahl)
#y0 = np.repeat(1/10, anzahl)

'''INTEGRATIONSSCHALTUNG'''

yi1 = 1/x
yi2 = 1/np.sqrt(1+x**2)

x_igrh = np.linspace(1/10, 1, anzahl)
y_igrh = np.repeat(1/np.sqrt(2), anzahl)
x_igrv = np.repeat(1, anzahl)
y_igrv = np.linspace(1/10, 1/np.sqrt(2), anzahl)

#plt.plot(x, y0)

plt.plot(x_igrh, y_igrh, color='r', linestyle='--', label=r'$\omega_\mathregular{i,gr}$')
plt.plot(x_igrv, y_igrv, color='r', linestyle='--')
plt.plot(x, yi1, Label=r'$\tilde{v}_\mathregular{i,1}$')
plt.plot(x, yi2, Label=r'$\tilde{v}_\mathregular{i,2}$')
plt.xscale('log')
plt.xlabel(r'$\tilde{\omega}_\mathregular{i}$')
plt.yscale('log')
plt.ylabel(r'$\tilde{v}$')
plt.legend()
plt.show()

'''DIFFERENZIERSCHALTUNG'''

yd1 = x
yd2 = x/np.sqrt(1+x**2)

x_dgrh = np.linspace(1, 10, anzahl)
y_dgrh = np.repeat(1/np.sqrt(2), anzahl)
x_dgrv = np.repeat(1, anzahl)
y_dgrv = np.linspace(1/10, 1/np.sqrt(2), anzahl)

#plt.plot(x, y0)

plt.plot(x_dgrh, y_dgrh, color='r', linestyle='--', label=r'$\omega_\mathregular{d,gr}$')
plt.plot(x_dgrv, y_dgrv, color='r', linestyle='--')
plt.plot(x, yd1, Label=r'$\tilde{v}_\mathregular{d,1}$')
plt.plot(x, yd2, Label=r'$\tilde{v}_\mathregular{d,2}$')
plt.xscale('log')
plt.xlabel(r'$\tilde{\omega}_\mathregular{d}$')
plt.yscale('log')
plt.ylabel(r'$\tilde{v}$')
plt.legend()
plt.show()

'''KOMBINATIONSSCHALTUNG'''
p = 2
R1, R2 = p, 1/p
C1, C2 = p, 1/p
wi, wd, w0 = 1/(R2*C2), 1/(R1*C1), 1
ywi, ywd, yw0 = 1/np.sqrt((R1/R2+C2/C1)**2+(wi*R1*C2-1/(wi*R2*C1))**2), 1/np.sqrt((R1/R2+C2/C1)**2+(wd*R1*C2-1/(wd*R2*C1))**2), 1/np.sqrt((R1/R2+C2/C1)**2+(w0*R1*C2-1/(w0*R2*C1))**2)
yk = 1/np.sqrt((R1/R2+C2/C1)**2+(x*R1*C2-1/(x*R2*C1))**2)

w_i, y_wi = np.repeat(wi, anzahl), np.linspace(1/10, ywi, anzahl)
w_d, y_wd = np.repeat(wd, anzahl), np.linspace(1/10, ywd, anzahl)
w_0, y_w0 = np.sqrt(w_i*w_d), np.linspace(1/10, yw0, anzahl)

#plt.plot(x, yi1, Label=r'$\tilde{v}_\mathregular{i,1}$', color='grey')
#plt.plot(x, yi2, Label=r'$\tilde{v}_\mathregular{i,2}$', color='grey')
#plt.plot(x, yd1, Label=r'$\tilde{v}_\mathregular{d,1}$', color='grey')
#plt.plot(x, yd2, Label=r'$\tilde{v}_\mathregular{d,2}$', color='grey')
plt.plot(x,yk)
plt.plot(w_d,y_wd, linestyle='--', label= r'$\omega_\mathregular{d,gr}$')
plt.plot(w_i,y_wi, linestyle='--', label= r'$\omega_\mathregular{i,gr}$')
plt.plot(w_0,y_w0, linestyle='--', label= r'$\omega_{0}$')
plt.xscale('log')
plt.xlabel(r'$\omega$ in $\frac{1}{\mathregular{s}}$')
plt.yscale('log')
plt.ylabel(r'$v_\mathregular{d,i}$')
plt.legend()
plt.show()