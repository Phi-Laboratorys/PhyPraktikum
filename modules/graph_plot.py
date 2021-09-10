import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np 
import math as m
import scipy.constants as scc
from scipy.stats import norm, poisson
from scipy.optimize import curve_fit
from scipy.interpolate import make_interp_spline, BSpline

rc('text', usetex=True)
rc('font', family='serif')

def plot_fit(n, sheetname, x_werte, y_werte, unsicherheit, lin_x, lin_y, label_x, label_y, errorbars):
        
    fitFunc = fit.linear()
        
    #Linearisierung
    x_linear = []
    y_linear = []
        
    if lin_x == 'x_linear':
        x_linear = x_werte
    elif lin_x == 'x_quadrat':
        for i in x_werte:
            x_linear += [i**2]
    elif lin_x == 'x_log':
        for i in x_werte:
            x_linear += [m.log(i)]
                
    if lin_y == 'y_linear':
        y_linear = y_werte
    elif lin_y == 'y_quadrat':
        for i in y_werte:
            y_linear += [i**2]
    elif lin_y == 'y_log':
        for i in y_werte:
            y_linear += [m.log(i)]
        
    plt.rc('figure.subplot', bottom=0.10, top=0.90, left=0.22, right=0.95) 
    plt.rc('axes', facecolor='white', edgecolor='black', titlesize=16, labelsize=16, grid=False)
    plt.rc('legend', fontsize=16, frameon=False, numpoints=1, labelspacing=0.1, columnspacing=0)
    plt.rc('xtick', labelsize=16)	
    plt.rc('ytick', labelsize=16)
    plt.rc('font', family="serif") 
    plt.rc('text', usetex=False)
    
    fitParams, fitCovariances = curve_fit(fitFunc.function, x_linear, y_linear)
    
    x = np.linspace(x_linear[0], x_linear[n-1]) 

    fig, ax = plt.subplots(figsize = (10,8))
    ax.plot(x_linear, y_linear, 'o', color = 'orange', label='measured data')
    ax.plot(x,fitFunc.function(x, fitParams[0], fitParams[1]), 'k', color='red', label = fitFunc.label()
            +'|   a = ' + str(round(fitParams[0],6)) + ',  b = ' +  str(round(fitParams[1],6)) )
        
    legend = ax.legend(loc= 'upper left', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('#00FFCC')
        
    plt.title('fit of ' + sheetname)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    print("a = ",fitParams[0]) 
    print("b = ",fitParams[1]) 
    
        
    if errorbars == True:
        plt.errorbar(x_linear, y_linear, unsicherheit, fmt = 'none', ecolor = 'orange', capsize = 5)
        
    plt.show()
      
def plot_histogramm (sheetname, data, anzahl, mittelwert, varianz, normed, schrittweite, gauss):
    
    fig, ax = plt.subplots(figsize=(10,8))
    
    balken_anzahl = int((round(max(data),2)-round(min(data),2))/schrittweite)
    n, bins, p = plt.hist(data, bins = balken_anzahl , density = normed, alpha = 0.5, )

    if  normed == True:
        for item in p:
            item.set_height(item.get_height()/sum(n))
        
        if gauss == True:
            plt.plot(bins, norm.pdf(bins, mittelwert, varianz)/sum(n))
        
        plt.ylabel('Wahrscheinlichkeit')
        
        ax.set_ylim(0, max(n)/sum(n) + 0.1)
        ax.set_xlim(xmin=min(data)-10,xmax=max(data)+10)
        
        print(n/sum(n) , '\n')
        
        y = np.linspace(0, 1/sum(n), 50)
        
        for i in y:    
            ax.plot(mittelwert, i, 'r-o')
            ax.plot(mittelwert-varianz, i, 'b-o')
            ax.plot(mittelwert+varianz, i, 'b-o')
            ax.plot(mittelwert-2*varianz, i, 'g-o')
            ax.plot(mittelwert+2*varianz, i, 'g-o')
            ax.plot(mittelwert-3*varianz, i, 'y-o')
            ax.plot(mittelwert+3*varianz, i, 'y-o')
        
    else:
        plt.ylabel('Anzahl')
        #plt.plot(bins, norm.pdf(bins, mittelwert, varianz))
        print(n, '\n')
    
        y = np.linspace(0, 1, 50)
        ax.set_xlim(xmin=min(data)-10,xmax=max(data)+10)
    
        for i in y:    
            ax.plot(mittelwert, i, 'r-o')
            ax.plot(mittelwert-varianz, i, 'b-o')
            ax.plot(mittelwert+varianz, i, 'b-o')
            ax.plot(mittelwert-2*varianz, i, 'g-o')
            ax.plot(mittelwert+2*varianz, i, 'g-o')
            ax.plot(mittelwert-3*varianz, i, 'y-o')
            ax.plot(mittelwert+3*varianz, i, 'y-o')
        
    
    plt.title(sheetname)
    plt.show()
        
def plot_2D(x, y, style, labelx, labely):
    plt.plot(x,y, style)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.show()

def curvefit(x, y, labelx, labely, anzahl, function):
    def objective(x, a, b):
        return function
    print(x,y)    
    popt, _ = curve_fit(objective, x, y)
    a, b = popt
    x_line = np.linspace(x.min(), x.max(), anzahl)
    y_line = objective(x_line, a, b)
    print(a, b)
    plt.plot(x_line, y_line)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.show()