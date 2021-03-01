# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:18:05 2021

@author: JAB
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import scipy as sp

# Valores en tiempo para graficar
t=np.arange(0,2,0.01)
# Definición de un periodo del tren de pulsos por partes
x1=lambda t:np.piecewise(t,t>=0,[1,0])
x2=lambda t:np.piecewise(t,t>=0.5,[0,1])
x3=lambda t:np.piecewise(t,t>=1.5,[1,0])
#Grafica de x(t) en un solo periodo
fig=plt.figure()
plt.grid()
plt.plot(t,x3(t)+x2(t-2)-x1(t-0.5))
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Tren de pulsos (un solo periodo)')

# Periodo de la señal
T=2

# Cálculo de los coeficientes de la serie de Fourier por partes, para a0
a01, err01=integrate.quad(x1,0,0.5)
a02, err02=integrate.quad(x2,0.5,1.5)
a03, err03=integrate.quad(x3,1.5,2)
a0=(1/2)*(a01+a02+a03)

# Inicio de la suma de fourier incluyendo a0
xaprox=a0*(2/T)
#xaprox=(2/T)
# Valores en tiempo para graficar
z=np.arange(0,2,0.01);
# N es el número de máximo de coeficientes de la Serie de Fourier
N=50
# Valor de inicio de la serie k=1
k=1  
# Inicio de listas para guardar los valores de ak y bk
ak=[]
bk=[]

fig=plt.figure()    
plt.grid()

while(k<=N):
    # Cálculo de los coeficientes de la serie de Fourier por partes, para ak
    ak1, errak1=integrate.quad(lambda t:np.cos(2*k*t*sp.pi/T),0,0.5)
    ak3, errak3=integrate.quad(lambda t:np.cos(2*k*t*sp.pi/T),1.5,2)
    ak.append(ak1+ak3)
    # Cálculo de los coeficientes de la serie de Fourier por partes, para bk
    bk1, errbk1=integrate.quad(lambda t:np.sin(2*k*t*sp.pi/T),0,0.5)
    bk3, errbk3=integrate.quad(lambda t:np.sin(2*k*t*sp.pi/T),1.5,2)
    bk.append(bk1+bk3)
    # Acumulación en la suma de fourier incluyendo ak y bk 
    xaprox += ak[k-1]*np.cos(k*z*sp.pi)+bk[k-1]*np.sin(k*z*sp.pi)
    k=k+1
    plt.plot(z,xaprox)
    #plt.show()
plt.xlabel('t')
plt.ylabel('xaprox(t)')
plt.title('Serie de Fourier para x(t) con k componentes')
  
fig=plt.figure()    
plt.plot(z,xaprox)
plt.grid()
plt.xlabel('t')
plt.ylabel('xaprox(t)')
plt.title('Tren de pulsos aproximado')
plt.show()


