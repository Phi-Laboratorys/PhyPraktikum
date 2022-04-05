# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:43:12 2020

@author: froes
"""


import numpy as np # import des numeric python modules
import scipy as sc # import des scientific python modules
import math # import des math modules, including math constants
import matplotlib.pyplot as plt # import des plot modules
import scipy.constants as scc # hier sind physikalische Konstanten definiert

data_file = "Messung.txt"
CK=[1.82,1.89,1.92,2.01,2.08,2.21,2.31,2.44,2.60,2.80,3.02,3.29]


Count, Values = np.genfromtxt(data_file,skip_header=1,unpack=True,usecols=(0,1))
file = open("Evaluation.txt","w")

l=len(Values)

def Statistical_Calculations():
    print("Werte")
    print(Values)
    Average=np.mean(Values)
    Variance=np.var(Values)
    SdiM=np.std(Values)
    SdaM=SdiM/np.sqrt(l)
    print("Anzahl der Werte")
    print("n = "+str(l))
    print("Mittelwert: ")
    print(Average)
    print("Varianz: ")
    print("\u03C3\u00b2 = "+str(Variance))
    print("Standartabweichung der Einzelmessung: ")
    print("\u03C3 = "+str(SdiM))
    print("Standartabweichung des Mittelwerts: ")
    print("s = "+str(SdaM))   
    file.write("-----Statistical Calculations-----\n")
    file.write("Anzahl der Werte: n = "+str(l)+"\n")
    file.write("Mittelwert: t= "+str(Average)+"\n")
    file.write("Varianz: sig^2 = "+str(Variance)+"\n")
    file.write("Standartabweichung der Einzelmessung: sig = "+str(SdiM)+"\n")
    file.write("Standartabweichung des Mittelwerts: s = "+str(SdaM)+"\n")
    return

def Histogramm():
    bins=math.ceil(5*np.log10(len(Values)))
    b=np.histogram(Values,bins)
    range=np.round(b[1],2)
    #print(range)
    plt.hist(Values,range)
    plt.title("Histogramm")
    plt.savefig('histo.png')
    file.write("\n")
    file.write("\n")
    file.write("-----Histogramm-----\n")
    file.write("Anzahl der Klassen: "+str(bins)+"\n")
    file.write("Klassenbreite: "+str(b[1])+"\n")
    return

def Chanvenetsche_Kriterium():
    ck=0
    file.write("\n")
    file.write("\n")
    file.write("-----Chanventsche Kriterium-----\n")
    if l<=3:
        ck=CK[0]
    elif l<=5:
        ck=CK[1]
    elif l<=6:
        ck=CK[2]
    elif l<=8:
        ck=CK[3]
    elif l<=10:
        ck=CK[4]
    elif l<=15:
        ck=CK[5]
    elif l<=20:
        ck=CK[6]
    elif l<=30:
        ck=CK[7]
    elif l<=50:
        ck=CK[8]
    elif l<=100:
        ck=CK[9]
    elif l<=200:
        ck=CK[10]
    else:
        ck=CK[11]
    xCh=ck*(np.std(Values))
    print(xCh)
    Average=np.mean(Values)
    delete=0
    deleteV=[]
    NValues = []
    for x in Values:
        if (abs(Average-x))>xCh:
           delete=delete+1
           deleteV.append(x)
        else:
            NValues.append(x)
    if delete!=0:
        print("Gelöschte Werte: "+str(delete))
        file.write("Anzahl gelöschter Werte: "+str(delete)+"\n")
        file.write("Gelöschte Werte: "+str(deleteV)+"\n")
        AvN=np.mean(NValues)
        VaN=np.var(NValues)
        SiMN=np.std(NValues)
        print(NValues)
        SaMN=SiMN/np.sqrt(len(NValues))
        print("Angepasste Werte")
        print("Anzahl der Werte")
        print("n = "+str(len(NValues)))
        print("Mittelwert: ")
        print(AvN)
        print("Varianz: ")
        print("\u03C3\u00b2 = "+str(VaN))
        print("Standartabweichung der Einzelmessung: ")
        print("\u03C3 = "+str(SiMN))
        print("Standartabweichung des Mittelwerts: ")
        print("s = "+str(SaMN))   
        file.write("\n")
        file.write("-----Statistical corrected Calculations-----\n")
        file.write("Anzahl der Werte: n = "+str(len(NValues))+"\n")
        file.write("Mittelwert: t= "+str(AvN)+"\n")
        file.write("Varianz: sig^2 = "+str(VaN)+"\n")
        file.write("Standartabweichung der Einzelmessung: sig = "+str(SiMN)+"\n")
        file.write("Standartabweichung des Mittelwerts: s = "+str(SaMN)+"\n")
        bins=math.ceil(5*np.log10(len(NValues)))
        b=np.histogram(NValues,bins)
        range=np.round(b[1],2)
        print(NValues)
        plt.hist(NValues,range)
        plt.title("Korrigiertes Histogramm")
        plt.savefig('histo_Ch.png')
        file.write("\n")
        file.write("\n")
        file.write("-----Histogramm corrected-----\n")
        file.write("Anzahl der Klassen: "+str(bins)+"\n")
        file.write("Klassenbreite: "+str(b[1])+"\n")
        #plt.show()
    return

def Test():
    sum=0
    for x in Values:
        sum=sum+x
    t=sum/len(Values)
    print("TEST")
    print(t)
    sum=0
    for x in Values:
        sum=sum+(x-t)**2
    v=np.sqrt(sum/(len(Values)-1))
    print(v)
    n=v/np.sqrt(len(Values))
    print(n)
    return

Statistical_Calculations()
Histogramm()
Chanvenetsche_Kriterium()
#Test()